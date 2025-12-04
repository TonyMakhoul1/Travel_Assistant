# 🌍 Travel Assistant – Multi-Agent AI Travel Planner

A smart AI-powered **Travel Assistant** that helps users plan their trips by providing:

* ✈️ Flight recommendations
* 🏨 Hotel suggestions
* 🗺️ Personalized tour plans
* ⚠️ Safety tips and travel advice

Built using **CrewAI multi-agent architecture**, **Streamlit UI**, and real-world travel APIs.

---

## 🚀 Project Overview

This project simulates a real-world AI travel assistant using **four specialized AI agents**, each responsible for a specific task:

| Agent            | Role                                     |
| ---------------- | ---------------------------------------- |
| ✈️ Flights Agent | Fetches available flight offers          |
| 🏨 Hotels Agent  | Recommends hotels at the destination     |
| 🗺️ Tour Agent   | Builds a tour plan for the city          |
| ⚠️ Advice Agent  | Provides safety tips and travel guidance |

All agents collaborate using **CrewAI** to generate a complete travel plan from a single user request.

---

## 🧱 Tech Stack

* **Python 3.10+**
* **CrewAI** – Multi-agent orchestration
* **Streamlit** – Web UI
* **SerpAPI** – Backup hotel & travel search
* **dotenv** – Environment variable management

---

## 📂 Project Structure

```
GenAI/
│
├── travel_assistant/
│   ├── agents/
│   │   ├── flight_agent.py
│   │   ├── hotel_agent.py
│   │   ├── tour_agent.py
│   │   └── advice_agent.py
│   │
│   ├── tools/
│   │   ├── get_flights.py
│   │   └── get_hotels.py
│   │
│   ├── tasks/
│   │   ├── flight_task.py
│   │   ├── hotel_task.py
│   │   ├── tour_task.py
│   │   └── advice_task.py
│   │
│   ├── crew.py
│   ├── app.py
│   └── main.py

---

## 🖥️ How It Works

1. User enters **departure city and destination** in the Streamlit UI.
2. Input is passed to the **CrewAI system**.
3. Each agent runs its task independently.
4. Final travel plan is generated and displayed to the user.

---

## 🔐 Environment Variables (.env)

Create a `.env` file inside the **GenAI/** folder:

```
GROQ_API_KEY=your_groq_api_key
SERP_API_KEY=your_serpapi_key
```

---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the App

```
streamlit run app.py
```

---

## ✅ Features

* ✅ City-to-airport automatic conversion
* ✅ Real-time flight search
* ✅ Real-time hotel recommendations
* ✅ Intelligent AI-generated tour plan
* ✅ Safety & travel tips
* ✅ Clean UI with Streamlit
* ✅ Modular agent-based architecture

---

## 🎯 Use Case

This project demonstrates:

* AI agent orchestration
* Real-world API integration
* LLM-based task automation
* Production-style project structuring

Perfect for:

* AI Engineer portfolios
* Applied GenAI projects
* Startup travel-tech demos

---

## 📌 Future Enhancements

* ✅ User authentication
* ✅ WhatsApp or Email notifications
* ✅ Emotion-based travel personalization
* ✅ Frontend deployment
* ✅ Mobile app integration

---

## 👨‍💻 Author

**Tony Makhoul**
Computer Engineering Student | AI Engineer | ML/DL Engineer
Lebanese International University

---
