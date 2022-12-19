from PIL import Image
import streamlit as st
from io import BytesIO
from urllib import request
import time
from add_logo import add_logo

url = "https://nfds.go.kr/favicon.ico"
res = request.urlopen(url).read()

im = Image.open(BytesIO(res))
st.set_page_config(page_icon=im, layout="wide")
add_logo()

# Create a title for the collapsible section
title = "오늘자 화재 현황"

# Create the content that you want to hide/reveal
hidden_content = st.markdown("""<body><div style="frameBorder=0; overflow: hidden; margin: 15px auto; max-width: 1600px; "><iframe scrolling="no" src=https://nfds.go.kr/dashboard/quicklook.do style="border: 0px none; margin-left: 0px; height: 1380px; margin-top: -600px; width: 1200px;"></iframe></div></body>""", unsafe_allow_html = True)

# Use the collapsible function to create the fold/unfold button
expander = st.expander(title)

# Use an if statement to check the state of the expander
if expander:
    hidden_content
    
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
    
# http://nfds.go.kr/dashboard/monitor.do
# <div style="frameBorder=0; overflow: hidden; margin: 15px auto; max-width: 1600px;"></div>
