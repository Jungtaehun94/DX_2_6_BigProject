import streamlit as st
def add_logo():
    st.markdown(    
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "";
                background-image: url(./logo.png);
                background-size:139px, 76px;
                background-repeat: no-repeat;
                width:139px;
                height:76px;
                display:inline-block;
                margin-left: 20px;
                font-size: 30px;
                position: relative;
                top: 30px;
            }
        </style>
        """,unsafe_allow_html=True)
