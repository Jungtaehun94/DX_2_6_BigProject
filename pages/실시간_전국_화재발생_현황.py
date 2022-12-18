from PIL import Image
import streamlit as st

im = Image.open("https://nfds.go.kr/favicon.ico")
st.set_page_config(page_title="Hello world", page_icon=im, layout="wide")
st.markdown("""
<body>
	<div style="border: 3px solid rgb(255, 255, 255); overflow: hidden; margin: 15px auto; max-width: 1600px; ">
		<iframe scrolling="no" src=https://nfds.go.kr/dashboard/monitor.do style="border: 0px none; margin-left: 0px; height: 2160px; margin-top: -550px; width: 1200px;">
		</iframe>
	</div>
</body>
""", unsafe_allow_html = True)
# http://nfds.go.kr/dashboard/monitor.do
