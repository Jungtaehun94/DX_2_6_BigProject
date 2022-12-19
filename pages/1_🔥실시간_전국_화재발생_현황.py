from PIL import Image
import streamlit as st
from io import BytesIO
from urllib import request
import time
from add_logo import add_logo
import numpy as np
import pandas as pd

url = "https://nfds.go.kr/favicon.ico"
res = request.urlopen(url).read()
im = Image.open(BytesIO(res))
st.set_page_config(page_icon=im, layout="wide")


add_logo()



ques = st.sidebar.radio(

    "선택하세요",

    ('한 눈에 보는 화재현황','전국출동현황','실시간 전국 화재발생 현황'))


if ques == '한 눈에 보는 화재현황':
    
    st.markdown("### 한 눈에 보는 화재 현황")
    st.markdown("""
<body>
    <div style="frameBorder=0; overflow: hidden; margin: 15px auto; max-width: 1600px; ">
        <iframe scrolling="no" src=https://nfds.go.kr/dashboard/quicklook.do style="border: 0px none; margin-left: 0px; height: 1380px; margin-top: -600px; width: 1200px;">
        </iframe>
    </div>
</body>
""", unsafe_allow_html = True)

elif ques =='전국출동현황':
    st.markdown("### 서울 출동 건수")
    st.sidebar.header("서울 출동 건수")
    st.write(
    """### 구조+화재+구급+재난""")
    st.markdown("### 화재 발생 현황")

 
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()
    st.markdown("### 화재 발생 원인")
    chart_data = pd.DataFrame(
    np.random.randn(20, 4),
    columns=['화재', '구조', '시위','구급'])

    st.area_chart(chart_data)


else :




    with st.spinner("Loading..."):
        
        st.markdown("""
    <body>
        <div style="border: 0px none; overflow: hidden; margin: 15px auto; max-width: 1600px; ">
            <iframe scrolling="no" src=https://nfds.go.kr/dashboard/monitor.do style="border: 0px none; margin-left: 0px; height: 2160px; width: 100%; margin-top: -550px; width: 1200px;">
            </iframe>
        </div>
    </body>
    """, unsafe_allow_html = True)
        time.sleep(3)
    


# else:
#     st.markdown("### 서울 출동 건수")
# st.sidebar.header("서울 출동 건수")
# st.write(
#     """### 구조+화재+구급+재난""")
# st.markdown("### 일별")

 
# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
    
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

#     progress_bar.empty()
#     st.markdown("### 사고별")
#     chart_data = pd.DataFrame(
#     np.random.randn(20, 4),
#     columns=['화재', '구조', '시위','구급'])

#     st.area_chart(chart_data)


# http://nfds.go.kr/dashboard/monitor.do
# <div style="frameBorder=0; overflow: hidden; margin: 15px auto; max-width: 1600px;"></div>
