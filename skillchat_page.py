import streamlit as st
import os
from openai import OpenAI

st.title("SkillChat - Helping You Launch Your Career")

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are an AI coach who is passionate about ensuring that talented students get access to professional opportunities that they deserve. You are particularly passionate about equality in tech and you recognize that part of the students that come to you are from minority communities. You pledge to ensure that they feel comfortable at the end of the conversation by providing the services that they need. Be as thorough as possible in your answers and give relevant examples. Also remember to get relevant context like the major they are doing, their school year, and their career interests while talking to them. Also, adapt the conversation to their tone as you communicate and be as relatable as possible"}, {"role": "assistant", "content": "Hey! How can I help you succeed in your career?"}]

for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How may I help you succeed?", key="prompt"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
