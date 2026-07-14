from dotenv import load_dotenv
import streamlit as st
from google import genai
import os


# Load environment variables
load_dotenv()


# Get Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")


if not api_key:
    st.error("GEMINI_API_KEY missing. Add it in .env file")
    st.stop()


# Page configuration
st.set_page_config(
    page_title="Memory Vault Chatbot",
    page_icon="🌌"
)


# Title
st.title("🌌 Multiverse Chatbot - Memory Vault")


# Personality selection
personality = st.sidebar.selectbox(
    "Choose your chatbot personality",
    [
        "Expert Hacker",
        "Angry Ravi Shastri",
        "Crazy Ronaldo Fan",
        "Motivational Coach",
        "Sarcastic Programmer"
    ]
)


# Gemini client
client = genai.Client(api_key=api_key)




# Task 1: Initialize Memory Vault


if "messages" not in st.session_state:
    st.session_state.messages = []




# Task 2: Display Chat History


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])




# Task 3: New Chat Input


if user_message := st.chat_input("Say something..."):


    # Display user message immediately

    with st.chat_message("user"):
        st.markdown(user_message)



    # Task 4: Save User Message


    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )



    # Gemini instruction

    prompt = f"""

You are acting as {personality}.

Rules:
- Stay in character.
- Be creative.
- Answer naturally.
- Do not say you are an AI.

User message:

{user_message}

"""



    try:

        with st.spinner("Thinking..."):


            response = client.models.generate_content(

                model="gemini-2.5-flash",

                contents=prompt

            )



        assistant_response = response.text



        # Display assistant reply

        with st.chat_message("assistant"):

            st.markdown(assistant_response)



        # Save assistant reply

        st.session_state.messages.append(

            {
                "role": "assistant",
                "content": assistant_response
            }

        )



    except Exception as e:

        st.error("Something went wrong")

        st.write(e)