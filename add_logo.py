import streamlit as st
def add_logo():
    st.markdown(    
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "";
                background-image: url(https://nfds.go.kr/images/common/logo_emb.png);
                background-size:139px, 36px;
                background-repeat: no-repeat;
                width:139px;
                height:36px;
                display:inline-block;
                margin-left: 20px;
                font-size: 30px;
                position: relative;
                top: 30px;
            }
        </style>
        """,unsafe_allow_html=True)