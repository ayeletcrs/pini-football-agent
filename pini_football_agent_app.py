
import streamlit as st

st.set_page_config(page_title="Pini - Football Agent", page_icon="⚽")

st.markdown("# Hi brother, This is Pini")
st.markdown("Ask me anything about football players, transfers, stats, and more!")

user_input = st.text_input("Your question")

if user_input:
    # Simulate a response
    st.markdown(f"**Pini says:** Based on your question _'{user_input}'_... [insert professional football analysis here]")

    st.markdown("---")
    st.markdown("See you soon  
All the best, Pini")
