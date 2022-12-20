import streamlit as st
def autoplay_muted_video(filename, height=325):
    return st.markdown(f"""
    <video controls height=100%, width=460, autoplay="true" muted="true" loop="true">
    <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/{filename}" type="video/mp4" />
    </video>
    """, unsafe_allow_html=True)