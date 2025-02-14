document.addEventListener("DOMContentLoaded", function () {
    const chatbox = document.getElementById("chatbox");
    const userInput = document.getElementById("userInput");
    const sendBtn = document.getElementById("sendBtn");

    let chatHistory = []; // Store conversation history

    sendBtn.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") sendMessage();
    });

    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        appendMessage("You", message, "user-message");
        chatHistory.push({ role: "human", content: message }); // Add user message to history

        userInput.value = "";
        userInput.disabled = true;
        sendBtn.disabled = true;

        try {
            const response = await fetch("/chat/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ messages: chatHistory }) // Send full history
            });

            const data = await response.json();
            appendMessage("AI", data.response, "bot-message");

            chatHistory.push({ role: "assistant", content: data.response }); // Store bot's response
        } catch (error) {
            appendMessage("Error", "Failed to reach the AI server.", "bot-message");
        }

        userInput.disabled = false;
        sendBtn.disabled = false;
    }

    function appendMessage(sender, text, className) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("chat-message", className);
        messageDiv.innerHTML = `<strong>${sender}:</strong> ${text}`;
        chatbox.appendChild(messageDiv);
        chatbox.scrollTop = chatbox.scrollHeight;
    }
});
