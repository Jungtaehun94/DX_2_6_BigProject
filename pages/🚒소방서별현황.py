import streamlit as st
import pandas as pd
import time
import numpy as np
import streamlit as st
import pydeck as pdk
from urllib.error import URLError
import base64
import altair as alt


add_selectbox = st.sidebar.selectbox('소방서를 선택하세요',
                                 ('마포소방서','관악소방서',
'동작소방서'
,'양천소방서'
,'강서소방서'
,'노원소방서'
,'강동소방서'
,'영등포소방서'
,'송파소방서'
,'성북소방서'
,'종로소방서'
,'서초소방서'
,'강남소방서'
,'중부소방서'
,'동대문소방서'
,'도봉소방서'
,'용산소방서'
,'광진소방서'
,'서대문소방서'
,'은평소방서'
,'중랑소방서'
,'강북소방서'
,'성북소방서'))
if add_selectbox == '마포소방서':
    
    col1,col2,col3,col4=st.columns(4)
    with col1:
        np.random.seed(1)

        source = pd.DataFrame({
    'x': np.arange(100),
    'A': np.random.randn(100).cumsum(),
    'B': np.random.randn(100).cumsum(),
    'C': np.random.randn(100).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=0.5).transform_fold(
    fold=['A', 'B', 'C'],
    as_=['category', 'y']
).encode(
    alt.X('x:Q'),
    alt.Y('y:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('x', 'y', groupby=['category']).mark_line(size=4)
    with col2:
        st.video('Flood.mp4')
        st.video('Campsite Fire.mp4')
    with col3:
        st.video('candlelight vigil.mp4')
        st.video('paramedics.mp4')        
