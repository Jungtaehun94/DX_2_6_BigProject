import streamlit as st
import pandas as pd
import time
import numpy as np
import streamlit as st
import pydeck as pdk
from urllib.error import URLError
import base64
import altair as alt
from add_logo import add_logo

add_logo()
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
,'강북소방서'))
if add_selectbox == '마포소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('마포소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:
        
    
        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
        
if add_selectbox == '관악소방서':
    st.title('관악소방서')
    col1,col2,col3=st.columns(3)
    with col1:
        
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.markdown("""
                <video controls width = 450 autoplay="true" muted="true" loop="true">
                <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/OpenCV%20People%20Counting%20Demo%20%232-3iiodzoG80A.mp4" type="video/mp4"/>
                </video>
                """, unsafe_allow_html=True)
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:
    
    
        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '동작소방서':
    st.title('동작소방서')
    col1,col2,col3=st.columns(3)
    with col1:
        
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)
    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '양천소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('양천소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
        
if add_selectbox == '강서소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('강서소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
        
if add_selectbox == '노원소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('노원소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)
    with col2:
        st.subheader('센터 CCTV')
         st.markdown("""
                <video controls width = 450 autoplay="true" muted="true" loop="true">
                <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/OpenCV%20People%20Counting%20Demo%20%232-3iiodzoG80A.mp4" type="video/mp4"/>
                </video>
                """, unsafe_allow_html=True)
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '강동소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('강동소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '영등포소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('영등포소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '송파소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('송파소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '성북소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('성북소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '종로소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('종로소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)
    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '서초소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('서초소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:
 
        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '강남소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('강남소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '중부소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('중부소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '동대문소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('동대문소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '도봉소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('도봉소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)
    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '용산소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('용산소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:
        
        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '광진소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('광진소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)
    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '서대문소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('서대문소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)
    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '은평소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('은평소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)
    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:
 
        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '중랑소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('중랑소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '중랑소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('중랑소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
if add_selectbox == '강북소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.title('강북소방서')
        st.subheader('인력현황')
        source = pd.DataFrame(
    {"category": ["장비조작", "구조", "화재", "예방", "조사"], "value": [3,8, 9, 2, 2]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
        st.subheader('월별 출동현황')
        np.random.seed(1)

        source = pd.DataFrame({
    '월': np.arange(13),
    '화재': np.random.randn(13).cumsum(),
    '구급': np.random.randn(13).cumsum(),
    '구조': np.random.randn(13).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=1).transform_fold(
    fold=['화재', '구급', '구조'],
    as_=['category', '출동횟수']
).encode(
    alt.X('월:Q'),
    alt.Y('출동횟수:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('월', '출동횟수', groupby=['category']).mark_line(size=5)

    with col2:
        st.subheader('센터 CCTV')
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
    with col3:

        st.markdown('### 자치구별 생활인구')
        source = pd.DataFrame({'자치구': ['송파구', '용산구', '마포구', '성북구', '광진구', '관악구', '종로구', '서대문구', '동작구','서초구','은평구','양천구','강남구','중랑구','강서구','중부구','강북구','노원구','동대문구','강동구','도봉구','영등포구'],'인구수': [375678, 545678, 375678, 325678, 336678, 375678, 247678, 338567, 394678,365678,355678,152678,385678,375678,375678,378678,309678,316678,155678,375678,355678,438678]})
        bar = alt.Chart(source).mark_bar().encode(x='자치구',y='인구수')
        bar
#         source = pd.DataFrame({"category": ["a", "b", "c", "d", "e", "f"], "value": [4, 6, 10, 3, 7, 8]})
#         base = alt.Chart(source).encode(theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None))
#         pie = base.mark_arc(outerRadius=120)
#         text = base.mark_text(radius=140, size=20).encode(text="category:N")
#         pie + text
       
        
        
#         source = pd.DataFrame(
#     [
#         {"team": "Germany", "matchday": 1, "point": 0, "diff": -1},
#         {"team": "Germany", "matchday": 2, "point": 3, "diff": 0},
#         {"team": "Germany", "matchday": 3, "point": 3, "diff": -2},
#         {"team": "Mexico", "matchday": 1, "point": 3, "diff": 1},
#         {"team": "Mexico", "matchday": 2, "point": 6, "diff": 2},
#         {"team": "Mexico", "matchday": 3, "point": 6, "diff": -1},
#         {"team": "South Korea", "matchday": 1, "point": 0, "diff": -1},
#         {"team": "South Korea", "matchday": 2, "point": 0, "diff": -2},
#         {"team": "South Korea", "matchday": 3, "point": 3, "diff": 0},
#         {"team": "Sweden", "matchday": 1, "point": 3, "diff": 1},
#         {"team": "Sweden", "matchday": 2, "point": 3, "diff": 0},
#         {"team": "Sweden", "matchday": 3, "point": 6, "diff": 3},
#     ]
# )

#         color_scale = alt.Scale(
#     domain=["Germany", "Mexico", "South Korea", "Sweden"],
#     range=["#000000", "#127153", "#C91A3C", "#0C71AB"],
# )

#         alt.Chart(source).mark_line().encode(
#     x="matchday:O", y="rank:O", color=alt.Color("team:N", scale=color_scale)
# ).transform_window(
#         rank="rank()",
#         sort=[
#         alt.SortField("point", order="descending"),
#         alt.SortField("diff", order="descending"),
#     ],
#         groupby=["matchday"],
# ).properties(title="World Cup 2018: Group F Rankings")
