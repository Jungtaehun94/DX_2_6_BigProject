import inspect
import textwrap
from urllib.error import URLError
import pandas as pd
import pydeck as pdk

import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(layout="wide",
    page_title="2반6조빅프로젝트 ",
    page_icon="🚒")
st.markdown("# 자치구별 필요 인력")
st.sidebar.header("자치구별 필요 인력")
st.write()
df = pd.read_csv("./data.csv", encoding = 'cp949')
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
                get_fill_color=["val*0.71", 0, 0, "(val-100)*0.71"],
                extruded=True,
            ),
            "자치구별 출동건수": pdk.Layer(
                "ColumnLayer",
                data=df,
                get_position=["lng", "lat"],
                get_elevation="전체출동건수",
                radius=300,
                elevation_scale=0.1,
                pickable=True,
                elevation_range=[0, 400],
#                 get_fill_color=["전체출동건수*0.007", 1,"전체출동건수*0.7", 128],
                get_fill_color=["0", "0","전체출동건수*0.007", "128"],
                extruded=True,
            )
        }
        with st.sidebar:
            to_show = st.radio("지도 레이어 선택",('자치구별 인력 배치', '자치구별 출동건수'))
        st.sidebar.markdown("### Map Layers")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
            if to_show == layer_name
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
                        "height": 800
                    },tooltip={'html': '<b>{출동소방서}</b><br>전체출동건수: {전체출동건수}<br>1인출동건수: {1인출동건수}<br>구급이송인원: {구급이송인원}<br>생존구조인원: {생존구조인원}<br>재산피해경감율: {재산피해경감율}','style': {'color': 'white'}},
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
st.subheader(" 실시간 서울시 내 소방서")
cols =st.columns((12,1,1,1))
# cols[1].metric("","")
# cols[1].metric("12/29", "-4 ℃", "-1Ｆ")
# cols[1].metric("12/30", "0 ℃", "3Ｆ")
with cols[0]:
    mapping_demo()
import altair as alt
df = pd.read_csv(r"./data.csv", encoding = 'cp949')
df['총원'] = df['총원'] - df['가용인원'] - df['출동인원']
order="{'출동인원':0, '가용인원': 1, '총원': 2}"
bar_chart = alt.Chart(df).transform_fold(
  ['출동인원', '가용인원', '총원'],
  as_=['column', 'value']
).mark_bar().encode(
    y='gu:N',
    x='value:Q',
    color='column:N',
    order="order:O"
)

for dpt in df['출동소방서'].unique().tolist():
    temp_df = df.loc[df['출동소방서'] == dpt,:]
    cols[1].metric(dpt, temp_df['22년 실제 소방공무원'][0], temp_df['오차'][0])
# cols[3].metric("마포소방서","280","2")
# cols[3].metric("관악소방서","68","-4")
# cols[3].metric("동작소방서","280")
# cols[3].metric("양천소방서","280","5")
# cols[3].metric("강서소방서","340")
# cols[3].metric("노원소방서","350","-1")
# cols[3].metric("강동소방서","200")
# cols[3].metric("영등포소방서","262","2")
# cols[1].metric("송파소방서","262")
# cols[1].metric("성북소방서","264","2")
# cols[1].metric("종로소방서","302")
# cols[1].metric("서초소방서","166")
# cols[1].metric("강남소방서","269","-9")
# cols[1].metric("중부소방서","203")
# cols[1].metric("동대문소방서","165")
# cols[1].metric("도봉소방서","205")
# cols[2].metric("용산소방서","360","20")
# cols[2].metric("광진소방서","201")
# cols[2].metric("서대문소방서","206")
# cols[2].metric("은평소방서","155")
# cols[2].metric("중랑소방서","184","20")
# cols[2].metric("강북소방서","268","50")

st.altair_chart(bar_chart, use_container_width=True)



# show_code(mapping_demo)
