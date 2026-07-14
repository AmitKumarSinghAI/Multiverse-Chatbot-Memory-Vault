# 🌌 The Multiverse of Chatbots - Memory Vault

## MirAI School of Technology - Virtual Summer Internship 2026  
## AI Builder Track - Assignment 3

This is my third assignment completed during the Virtual Summer Internship 2026 at MirAI School of Technology under the **"AI Builder" Track**.

The project is called **"The Memory Vault: Stateful Chatbot"**.

It is an upgraded version of the Multiverse of Chatbots application where the chatbot is enhanced from a **stateless chatbot** to a **stateful chatbot**. The application uses **Streamlit Session State (`st.session_state`)** to store and display previous conversations, allowing users to continue chatting without losing chat history after Streamlit reruns.

The chatbot is powered by the **Google Gemini API** and uses prompt engineering techniques to generate responses according to the selected AI personality.

---

# 🚀 Project Overview

The **Multiverse Chatbot - Memory Vault** is a Generative AI chatbot application built with Streamlit and Google Gemini API.

The main objective of this project is to solve the memory problem of traditional Streamlit chatbots. Since Streamlit reruns the complete script after every interaction, normal variables lose their values. 

To overcome this problem, the application uses:

- `st.session_state`
- `st.chat_input()`
- `st.chat_message()`

to maintain and display continuous conversations.

Users can select different chatbot personalities and have a conversation while the chatbot remembers previous messages during the active session.

---

# ✨ Features

## 🧠 Stateful Conversation Memory

- Stores user and assistant messages using Streamlit Session State.
- Maintains chat history during Streamlit reruns.
- Displays previous conversations automatically.

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
- Uses prompt engineering to control chatbot behavior and personality.

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- python-dotenv

---

# 🏗️ Project Architecture

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


---

# 🎥 Demo Video

Project demonstration showing the continuous 3-message conversation and Memory Vault functionality:

[Watch Demo Video] sha256:fb6487bd6c80b509e3c0a482a0c877fd6d389371eb41b94309d35d4bb5f17b6f

# 🧠 Memory Implementation

The chatbot uses Streamlit Session State as a temporary memory vault.

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

- Every user message and AI response is stored inside this list.

- During every Streamlit rerun, the stored messages are loaded and displayed again.

# 📂 Project Structure

Multiverse-Chatbot-Memory-Vault/

│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore

# ⚙️ Installation and Setup

1. Clone the repository
git clone https://github.com/AmitKumarSinghAI/Multiverse-Chatbot-Memory-Vault


2. Navigate to project folder
cd Multiverse-Chatbot-Memory-Vault


3. Install dependencies
pip install -r requirements.txt


4. Create .env file

Add your Gemini API key:

GEMINI_API_KEY=your_api_key_here


5. Run the application
streamlit run app.py

# 📸 Application Workflow
- User selects a chatbot personality from the sidebar.
- User enters a message using the chat input.
- User message is stored in Session State.
- Gemini generates a personality-based response.
- Assistant response is stored in Session State.
- Complete conversation history is displayed.

# 🎯 Learning Outcomes

Through this assignment, I learned:

- How Streamlit reruns applications.
- How to maintain application state using st.session_state.
- How to build conversational AI interfaces.
- How to integrate Gemini API with Streamlit.
- How prompt engineering controls AI personality behavior.


# 👨‍💻 Author

Amit Kumar Singh Kurmi

B.Tech Computer Science Engineering
AI Builder Track - Virtual Summer Internship 2026
MirAI School of Technology
