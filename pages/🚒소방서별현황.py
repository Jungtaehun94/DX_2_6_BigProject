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
        st.video('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0d6a70f9-efe0-45d4-8565-7a806625b310/%ED%85%90%ED%8A%B8_%EC%A0%84%EC%B2%B4%EA%B0%80_%EC%88%9C%EC%8B%9D%EA%B0%84%EC%97%90..._CCTV%EB%A1%9C_%EB%B3%B8_%EA%B0%95%ED%99%94%EB%8F%84_%EC%BA%A0%ED%95%91%EC%9E%A5_%ED%99%94%EC%9E%AC_%EC%83%81%ED%99%A9_-_YouTube_-_Chrome_2022-12-14_12-03-25.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T030513Z&X-Amz-Expires=86400&X-Amz-Signature=d77e45f4e0e06758f708bf1cec11239b9f25aa361b36c70aa3269d9d610687fc&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%27%25ED%2585%2590%25ED%258A%25B8%2520%25EC%25A0%2584%25EC%25B2%25B4%25EA%25B0%2580%2520%25EC%2588%259C%25EC%258B%259D%25EA%25B0%2584%25EC%2597%2590...%27%2520CCTV%25EB%25A1%259C%2520%25EB%25B3%25B8%2520%25EA%25B0%2595%25ED%2599%2594%25EB%258F%2584%2520%25EC%25BA%25A0%25ED%2595%2591%25EC%259E%25A5%2520%25ED%2599%2594%25EC%259E%25AC%2520%25EC%2583%2581%25ED%2599%25A9%2520-%2520YouTube%2520-%2520Chrome%25202022-12-14%252012-03-25.mp4%22&x-id=GetObject')
        st.video('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0d6a70f9-efe0-45d4-8565-7a806625b310/%ED%85%90%ED%8A%B8_%EC%A0%84%EC%B2%B4%EA%B0%80_%EC%88%9C%EC%8B%9D%EA%B0%84%EC%97%90..._CCTV%EB%A1%9C_%EB%B3%B8_%EA%B0%95%ED%99%94%EB%8F%84_%EC%BA%A0%ED%95%91%EC%9E%A5_%ED%99%94%EC%9E%AC_%EC%83%81%ED%99%A9_-_YouTube_-_Chrome_2022-12-14_12-03-25.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T030513Z&X-Amz-Expires=86400&X-Amz-Signature=d77e45f4e0e06758f708bf1cec11239b9f25aa361b36c70aa3269d9d610687fc&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%27%25ED%2585%2590%25ED%258A%25B8%2520%25EC%25A0%2584%25EC%25B2%25B4%25EA%25B0%2580%2520%25EC%2588%259C%25EC%258B%259D%25EA%25B0%2584%25EC%2597%2590...%27%2520CCTV%25EB%25A1%259C%2520%25EB%25B3%25B8%2520%25EA%25B0%2595%25ED%2599%2594%25EB%258F%2584%2520%25EC%25BA%25A0%25ED%2595%2591%25EC%259E%25A5%2520%25ED%2599%2594%25EC%259E%25AC%2520%25EC%2583%2581%25ED%2599%25A9%2520-%2520YouTube%2520-%2520Chrome%25202022-12-14%252012-03-25.mp4%22&x-id=GetObject')
    with col3:
        st.video('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0d6a70f9-efe0-45d4-8565-7a806625b310/%ED%85%90%ED%8A%B8_%EC%A0%84%EC%B2%B4%EA%B0%80_%EC%88%9C%EC%8B%9D%EA%B0%84%EC%97%90..._CCTV%EB%A1%9C_%EB%B3%B8_%EA%B0%95%ED%99%94%EB%8F%84_%EC%BA%A0%ED%95%91%EC%9E%A5_%ED%99%94%EC%9E%AC_%EC%83%81%ED%99%A9_-_YouTube_-_Chrome_2022-12-14_12-03-25.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T030513Z&X-Amz-Expires=86400&X-Amz-Signature=d77e45f4e0e06758f708bf1cec11239b9f25aa361b36c70aa3269d9d610687fc&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%27%25ED%2585%2590%25ED%258A%25B8%2520%25EC%25A0%2584%25EC%25B2%25B4%25EA%25B0%2580%2520%25EC%2588%259C%25EC%258B%259D%25EA%25B0%2584%25EC%2597%2590...%27%2520CCTV%25EB%25A1%259C%2520%25EB%25B3%25B8%2520%25EA%25B0%2595%25ED%2599%2594%25EB%258F%2584%2520%25EC%25BA%25A0%25ED%2595%2591%25EC%259E%25A5%2520%25ED%2599%2594%25EC%259E%25AC%2520%25EC%2583%2581%25ED%2599%25A9%2520-%2520YouTube%2520-%2520Chrome%25202022-12-14%252012-03-25.mp4%22&x-id=GetObject')
        st.video('https://www.youtube.com/embed/kRHL04ELytc?autoplay=1')        
