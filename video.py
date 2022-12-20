import streamlit as st
import random

elements = [
    '_Seoul fire station responding.mp4',
    'Campsite Fire.mp4',
    'candlelight vigil.mp4',
    'Flood.mp4',
    'paramedics.mp4',
    'Thermal.mp4',
    'X-mas.mp4',
    '바디캠1.mp4',
    '바디캠2.mp4',
    '바디캠3.mp4',
    ]

def autoplay_muted_video(filename, height=325):
    return st.markdown(f"""
    <video controls height=100%, width=460, autoplay="true" muted="true" loop="true">
    <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/{filename}" type="video/mp4" />
    </video>
    """, unsafe_allow_html=True)

def rand_video(n):
    for video in random.sample(elements, n):
        autoplay_muted_video(video)