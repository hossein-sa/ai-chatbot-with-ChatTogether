# AI Chatbot with FastAPI & ChatTogether

A chatbot built using **FastAPI**, **LangChain**, and **ChatTogether** (Llama-3-70B).  
Interactive UI powered by **HTML, CSS, and JavaScript**.

## Features
```
- Conversational memory (bot remembers previous messages in a session)
- FastAPI backend for high performance
- Simple and responsive chat UI
- Uses Llama-3-70B via ChatTogether API
- CORS enabled for frontend-backend communication
```

## Project Structure
```
ai-chatbot-with-ChatTogether/
│── backend/   
│   ├── main.py          # FastAPI backend
│── frontend/   
│   ├── index.html       # Chat UI
│   ├── styles.css       # Chat UI styling
│   ├── app.js           # JavaScript logic
│── .gitignore           # Ignore unnecessary files
│── .env                 # API key (DO NOT SHARE)
│── requirements.txt      # Python dependencies
│── README.md            # Project documentation
```

## Installation & Setup

### Clone the Repository
```
git clone https://github.com/hossein-sa/ai-chatbot-with-ChatTogether.git
cd ai-chatbot-with-ChatTogether
```

### Set Up Virtual Environment (Optional)
```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Set Up API Key
Create a `.env` file inside the project and add:
```
TOGETHER_API_KEY=your_actual_api_key_here
```

### Run the Backend (FastAPI)
```
uvicorn backend.main:app --reload
```
API will run at:
```
http://127.0.0.1:8000/
```
Interactive documentation available at:
```
http://127.0.0.1:8000/docs
```

### Run the Frontend (Chat UI)
No extra setup is needed. The UI is served automatically by FastAPI.

## ChatTogether API

ChatTogether provides **free access** to its **Llama-3-70B model**, but with **usage limitations**. You can use the API for free, but be aware of the following:

```
- Free API access is available with limitations on requests and usage.
- High-demand usage may require a paid plan.
- You can check the ChatTogether documentation for more details about usage and pricing.
```

## Deploying on Render
1. Create a **Render** account at `https://render.com`
2. Click on **New Web Service**
3. Connect your **GitHub repository**
4. Set the **Start Command**:
```
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```
5. Add an **environment variable**:
```
TOGETHER_API_KEY=your_actual_api_key_here
```
6. Click **Deploy** and wait for deployment to complete.

## Contributing
```
1. Fork the repository
2. Create a new branch: git checkout -b feature-branch
3. Commit your changes: git commit -m "Added new feature"
4. Push to the branch: git push origin feature-branch
5. Open a pull request
```

## License
```
This project is licensed under the MIT License.
```