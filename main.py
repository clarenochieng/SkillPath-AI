import streamlit as st

skillchat_page = st.Page("skillchat_page.py", title="SkillChat")
home_page = st.Page("streamlit.py", title="Home")
connect_page = st.Page("connect_page.py", title="Connect")
careers_page = st.Page("careers_page.py", title="Careers")

current_page = st.navigation([home_page, skillchat_page, connect_page, careers_page])
st.set_page_config(page_title="Find Your Dream Career")
current_page.run()
