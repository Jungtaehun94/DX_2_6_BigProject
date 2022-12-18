import streamlit as st
def add_logo():
    st.markdown(    
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "";
                background-image: url(https://w.namu.la/s/4c3eef0028388ac1c1de07d5dad05ee01c968eeb8325a1fcdaabafb811dcc073d1528f0d880b9930a37fd23f5a77527d3edf5a529bea27b2214366b3f978e951f474b7e3a82e6f5fe397c9ecedb11ba8);
                background-size:165px, 90px;
                background-repeat: no-repeat;
                width:165px;
                height:90px;
                display:inline-block;
                margin-left: 20px;
                font-size: 30px;
                position: relative;
                top: 30px;
            }
        </style>
        """,unsafe_allow_html=True)
