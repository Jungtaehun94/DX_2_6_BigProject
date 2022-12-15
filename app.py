import inspect
import textwrap
from urllib.error import URLError
import pandas as pd

import pandas as pd
import pydeck as pdk

import streamlit as st
from streamlit.hello.utils import show_code

df = pd.read_csv("data.csv", encoding = 'cp949')
df.head()

# df = r"C:\Users\User\Downloads\csvjson (1).json"
def mapping_demo():
    try:
        ALL_LAYERS = {
            "자치구별 인력 배치": pdk.Layer(
                "ColumnLayer",
                data=df,
                get_position=["lng", "lat"],
                get_elevation="val",
                radius=300,
                elevation_scale=10,
                pickable=True,
                elevation_range=[0, 400],
                get_fill_color=["출동건수_r", 0, 0, "출동건수_a"],
                extruded=True,
            ),
            "자치구별 출동건수": pdk.Layer(
                "ColumnLayer",
                data=df,
                get_position=["lng", "lat"],
                get_elevation="전체출동건수",
                radius=300,
                elevation_scale=10,
                pickable=True,
                elevation_range=[0, 400],
                get_fill_color=["val*0.71", 0, 0, "(val-100)*0.71"],
                extruded=True,
            )
        }
        st.sidebar.markdown("### Map Layers")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)
        ]
        if selected_layers:
            st.pydeck_chart(
                pdk.Deck(
                    map_style=None,
                    initial_view_state={
                        "latitude": 37.55,
                        "longitude": 126.99,
                        "zoom": 11,
                        "pitch": 50,
                    },tooltip={'html': '<b>{gu}</b><br>필요인원: {val}<br>평가기준<br>전체출동건수: {전체출동건수}<br>1인출동건수: {1인출동건수}<br>구급이송인원: {구급이송인원}<br>생존구조인원: {생존구조인원}<br>재산피해경감율: {재산피해경감율}<br>인구밀도: {인구밀도}<br>1인담당인구: {1인담당인구}<br>1인담당면적: {1인담당면적}<br>내년 소방공무원: {내년 소방공무원}<br>비고: {비고}','style': {'color': 'white'}},
                    layers=selected_layers,
                )
            )
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )


st.set_page_config(page_title="자치구별 필요 인력", page_icon="🌍")
st.markdown("# 자치구별 필요 인력")
st.sidebar.header("자치구별 필요 인력")
st.write()

mapping_demo()

# show_code(mapping_demo)
