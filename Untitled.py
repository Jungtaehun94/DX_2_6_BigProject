import streamlit as st
import random
@st.cache
def run_function(value):
    # Do something with the value selected from the selectbox
    return f'You selected {value}', rand_video(2)
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
def rand_video(n):
    return [autoplay_muted_video(video) for video in random.sample(elements, 2)]
def autoplay_muted_video(filename, height=325):
    return st.markdown(f"""
    <video controls height=100%, width=460, autoplay="true" muted="true" loop="true">
    <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/{filename}" type="video/mp4" />
    </video>
    """, unsafe_allow_html=True)

# Create a selectbox
options = ['Option 1', 'Option 2', 'Option 3']
selected_option = st.selectbox('Choose an option', options)

# Display the output of the function in a separate area of the app

st.markdown(run_function(selected_option), unsafe_allow_html=True)
