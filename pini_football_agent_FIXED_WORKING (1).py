
import streamlit as st
import openai

st.set_page_config(page_title="Pini - Football Agent", page_icon="⚽")
st.title("⚽ Pini - Your Football Intelligence Agent")
st.markdown("Ask me about transfer values, contracts, injuries, or hidden gems!")

# ✅ הכניסי כאן את ה־API Key שלך
openai.api_key = "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"

with st.chat_message("assistant"):
    st.markdown("Hi brother, This is Pini")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": (
            "You are Pini Zehavi, a professional football business intelligence agent. "
            "Your job is to provide expert, data-driven answers on football players, their market value, salaries, "
            "contracts, transfer history, performance metrics, and injury risks. You also offer scouting insights and "
            "investment recommendations. Always answer in a precise, analytical tone. Use bullet points or tables if helpful. "
            "Start every answer with: 'Hi brother, This is Pini' and end with: 'See you soon\nAll the best, Pini'"
        )}
    ]

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask Pini anything about football players..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        client = openai.OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=st.session_state.messages,
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

with st.sidebar:
    st.info("Built with ❤️ by Ayelet and ChatGPT")
