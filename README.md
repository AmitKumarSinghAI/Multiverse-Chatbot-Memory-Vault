# 🌌 The Multiverse of Chatbots - Memory Vault

## MirAI School of Technology - Virtual Summer Internship 2026  
## AI Builder Track - Assignment 3

This is my third assignment completed during the **Virtual Summer Internship 2026** at **MirAI School of Technology** under the **"AI Builder" Track**.

The project is called **"The Memory Vault: Stateful Chatbot"**.

It is an upgraded version of the **Multiverse of Chatbots** application where the chatbot is transformed from a **stateless chatbot** into a **stateful chatbot**.

The application uses **Streamlit Session State (`st.session_state`)** to store and display previous conversations, allowing users to continue chatting without losing chat history during Streamlit reruns.

The chatbot is powered by the **Google Gemini API** and uses **prompt engineering techniques** to generate responses according to the selected AI personality.

---

# 🚀 Project Overview

The **Multiverse Chatbot - Memory Vault** is a Generative AI chatbot application built using **Streamlit** and **Google Gemini API**.

The main objective of this project is to solve the memory problem of traditional Streamlit chatbots. Since Streamlit reruns the complete script after every interaction, normal Python variables lose their values.

To overcome this problem, the application uses:

- `st.session_state`
- `st.chat_input()`
- `st.chat_message()`

to maintain and display continuous conversations.

Users can select different chatbot personalities and interact with an AI chatbot while the application remembers previous messages during the active session.

---

# ✨ Features

## 🧠 Stateful Conversation Memory

- Stores user and assistant messages using Streamlit Session State.
- Maintains chat history during Streamlit reruns.
- Automatically displays previous conversations.

## 🤖 Multiple AI Personalities

Users can interact with different chatbot characters:

- 👨‍💻 Expert Hacker
- 🏏 Angry Ravi Shastri
- ⚽ Crazy Ronaldo Fan
- 💪 Motivational Coach
- 👨‍💻 Sarcastic Programmer

## 💬 Modern Chat Interface

- Uses Streamlit native chat components.
- Replaces traditional text input and button system.
- Provides a ChatGPT-like conversation experience.

## 🔥 Gemini AI Integration

- Uses Google Gemini API for generating intelligent responses.
- Uses prompt engineering to control chatbot personality behavior.

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- python-dotenv

---

# 🏗️ Project Architecture

```
User Input
     |
     |
st.chat_input()
     |
     |
Save User Message
(st.session_state.messages)
     |
     |
Google Gemini API
     |
     |
Generate AI Response
     |
     |
Save Assistant Message
(st.session_state.messages)
     |
     |
Display Complete Chat History
```

---

# 🧠 Memory Implementation

The chatbot uses **Streamlit Session State** as a temporary memory vault.

Example:

```python
st.session_state.messages = [
    {
        "role": "user",
        "content": "Hello"
    },
    {
        "role": "assistant",
        "content": "Hi! How can I help?"
    }
]
```

Every user message and AI response is stored inside this list.

During every Streamlit rerun, the stored messages are loaded and displayed again using `st.chat_message()`.

---

# 🎥 Demo Video

Project demonstration showing the continuous 3-message conversation and Memory Vault functionality:

[Watch Demo Video] https://github.com/AmitKumarSinghAI/Multiverse-Chatbot-Memory-Vault/releases/download/v1.0.0/Multiverse.Chatbot.Memory.Vault.Demo.webm
---

# 📂 Project Structure

```
Multiverse-Chatbot-Memory-Vault/

│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# ⚙️ Installation and Setup

## 1. Clone the repository

```bash
git clone https://github.com/AmitKumarSinghAI/Multiverse-Chatbot-Memory-Vault
```

## 2. Navigate to project folder

```bash
cd Multiverse-Chatbot-Memory-Vault
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Create `.env` file

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## 5. Run the application

```bash
streamlit run app.py
```

---

# 📸 Application Workflow

1. User selects a chatbot personality from the sidebar.
2. User enters a message using the chat input.
3. User message is stored in Session State.
4. Gemini generates a personality-based response.
5. Assistant response is stored in Session State.
6. Complete conversation history is displayed.

---

# ✅ Assignment Requirements Completed

| Requirement | Status |
|------------|--------|
| Initialize Streamlit Session State | ✅ Completed |
| Store user messages | ✅ Completed |
| Store assistant responses | ✅ Completed |
| Display chat history | ✅ Completed |
| Replace text input with st.chat_input | ✅ Completed |
| Use st.chat_message | ✅ Completed |
| Continuous 3-message conversation demo | ✅ Completed |

---

# 🎯 Learning Outcomes

Through this assignment, I learned:

- How Streamlit reruns applications.
- How to maintain application state using `st.session_state`.
- How to build conversational AI interfaces.
- How to integrate Gemini API with Streamlit.
- How prompt engineering controls AI personality behavior.

---

# 👨‍💻 Author

**Amit Kumar Singh Kurmi**

B.Tech Computer Science Engineering  
AI Builder Track - Virtual Summer Internship 2026  
MirAI School of Technology