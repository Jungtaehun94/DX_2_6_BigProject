import streamlit as st
import random

elements = [
    'Seoul_fire_station_responding.mp4',
    'Flood.mp4',
    'paramedics.mp4',
    'Thermal.mp4',
    '바디캠1.mp4',
    '바디캠2.mp4',
    '바디캠3.mp4',
    ]

def autoplay_muted_video(filename, height=325, width=460):
    return st.markdown(f"""
    <video controls height=100%, width={width}, autoplay="true" muted="true" loop="true"><source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/{filename}" type="video/mp4" /></video>
    """, unsafe_allow_html=True)

def rand_video(n):
    vid_list = random.sample(elements, n)
    for video in vid_list:
        st.video("https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/"+video)
        print(video)
        
def pick_video():
    vid_list = random.sample(elements, 2)
    txt = 'st.write(\"\"\"<video controls height=100%, width=460, autoplay="true" muted="true" loop="true"><source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/'+f'{vid_list[0]}'+'" type="video/mp4" /></video>\"\"\", unsafe_allow_html=True)'
    txt = 'st.video("https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/'+f'{vid_list[0]}'+'")'
    return txt