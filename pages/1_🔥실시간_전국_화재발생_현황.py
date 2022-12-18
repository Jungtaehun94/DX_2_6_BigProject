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

<div class="holds-the-iframe"><iframe id = fire scrolling="no" src=https://nfds.go.kr/dashboard/monitor.do style="border: 0px none; margin-left: 0px; height: 2160px; margin-top: -550px; width: 1200px;"></iframe></div>

.holds-the-iframe {
  background:url(https://nfds.go.kr/favicon.ico) center center no-repeat;
}


# http://nfds.go.kr/dashboard/monitor.do
