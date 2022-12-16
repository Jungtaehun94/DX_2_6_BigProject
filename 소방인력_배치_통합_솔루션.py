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

df = pd.read_csv(r"./data.csv", encoding = 'cp949')
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

import altair as alt
df = pd.read_csv(r"./data.csv", encoding = 'cp949')
df['22년 실제 소방공무원'] = df['22년 실제 소방공무원'] + df['감원']
df['감원'] = df['감원'].abs()
order="{'22년 실제 소방공무원':0, '증원': 1, '감원': 2}"
column = "['#0000FF', '#00FF00', '#FF0000]"
bar_chart = alt.Chart(df).transform_fold(
  ['22년 실제 소방공무원', '증원', '감원'],
  as_=['column', 'value']
).mark_bar().encode(
    y='gu:N',
    x='value:Q',
    color=alt.Color('column:N',scale=alt.Scale(domain=['22년 실제 소방공무원', '증원', '감원'],range=['#264b96', 'green', 'red'])),
#     color=alt.Color('column:N',scale=alt.Scale(domain=['22년 실제 소방공무원', '증원', '감원'],range=['#264b96', '#006f3c', '#bf212f'])),%%!
    order="order:O"
)
cols[1].metric('','현재','증원')
cols[2].metric('','인력','-감소')
cols[3].metric('','현황','')
cols[3].text('')
metric_counter = 0
for dpt in df['출동소방서'].unique().tolist():
    temp_df = df.loc[df['출동소방서'] == dpt,:].reset_index()
    with cols[metric_counter%3+1]:
        st.metric(dpt, temp_df['22년 실제 소방공무원'][0], temp_df['오차'][0].astype(str))
    metric_counter +=1
#     with cols[1]:
#         st.write(dpt, temp_df['22년 실제 소방공무원'][0], temp_df['오차'][0].astype(str))
#         st.metric(dpt, temp_df['22년 실제 소방공무원'][0], temp_df['오차'][0].astype(str)abs)

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
# cols[2].metric("성북소방서","177")

with cols[0]:
    mapping_demo()
    st.altair_chart(bar_chart, use_container_width=True)


# show_code(mapping_demo)
with st.sidebar:
    st.title('119 종합 상황 센터')
add_selectbox = st.sidebar.selectbox('신고 유형을 선택하세요',
                                 ('재난','범죄','민원/상담'))
if add_selectbox == '재난':
    def 사고유형을선택해주세요():
        st.title('서울시 재난 종합 지휘 센터')
        st.image('https://gnews.gg.go.kr/OP_UPDATA/UP_DATA/_FILEZ/202010/20201030012201229929411.jpg')
        st.sidebar.title('-')
    def 화재():
        col1,col2,col3=st.columns(3)
        with col1:
            st.subheader('화재 상황 발생 지역')
            df = pd.DataFrame(
            np.random.randn(1, 2) / [40, 50] + [37.5642, 127.0016],
            columns=['lat', 'lon'])

            st.map(df)
#             st.pydeck_chart(pdk.Deck(
#           map_style=None,
#            initial_view_state=pdk.ViewState(
#         latitude=37.5642,
#         longitude=127.0016,
#         zoom=10,
#         pitch=50,)))
#             chart_data = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#    columns=['lat', 'lon'])
        with col2:
            st.subheader('실시간 현장CCTV')
            st.video('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0d6a70f9-efe0-45d4-8565-7a806625b310/%ED%85%90%ED%8A%B8_%EC%A0%84%EC%B2%B4%EA%B0%80_%EC%88%9C%EC%8B%9D%EA%B0%84%EC%97%90..._CCTV%EB%A1%9C_%EB%B3%B8_%EA%B0%95%ED%99%94%EB%8F%84_%EC%BA%A0%ED%95%91%EC%9E%A5_%ED%99%94%EC%9E%AC_%EC%83%81%ED%99%A9_-_YouTube_-_Chrome_2022-12-14_12-03-25.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T030513Z&X-Amz-Expires=86400&X-Amz-Signature=d77e45f4e0e06758f708bf1cec11239b9f25aa361b36c70aa3269d9d610687fc&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%27%25ED%2585%2590%25ED%258A%25B8%2520%25EC%25A0%2584%25EC%25B2%25B4%25EA%25B0%2580%2520%25EC%2588%259C%25EC%258B%259D%25EA%25B0%2584%25EC%2597%2590...%27%2520CCTV%25EB%25A1%259C%2520%25EB%25B3%25B8%2520%25EA%25B0%2595%25ED%2599%2594%25EB%258F%2584%2520%25EC%25BA%25A0%25ED%2595%2591%25EC%259E%25A5%2520%25ED%2599%2594%25EC%259E%25AC%2520%25EC%2583%2581%25ED%2599%25A9%2520-%2520YouTube%2520-%2520Chrome%25202022-12-14%252012-03-25.mp4%22&x-id=GetObject')
            st.video('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e44f7e08-b438-4d45-9bc9-8f4cd068c74d/Live_CAM%EC%8B%A4%EC%8B%9C%EA%B0%84_%EC%84%9C%EC%9A%B8_%ED%95%9C%EA%B0%95_63%EB%B9%8C%EB%94%A9_%EB%85%B8%EC%9D%84_%EB%A7%9B%EC%A7%91__Seoul_Hangang_63_Building___%ED%95%9C%EA%B0%95%EC%B2%A0%EA%B5%90_%EB%85%B8%EB%93%A4%EC%84%AC_63%EB%B9%8C%EB%94%A9_%EB%AC%BC%EB%A9%8D_%EC%95%BC%EA%B2%BD_%EB%85%B8%EC%9D%84%EB%A9%8D_%ED%9E%90%EB%A7%81%EB%B0%A9%EC%86%A1_%EC%97%AC%EC%9D%98%EB%8F%84_-_YouTube_-_Chrome_2022-12-14_11-56-06.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T113229Z&X-Amz-Expires=86400&X-Amz-Signature=83e9f46faacf0dfe12d95ef2c06548512ec69807b40630fe1036a6c3625d04b8&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%255BLive%2520CAM%255D%25EC%258B%25A4%25EC%258B%259C%25EA%25B0%2584%2520%25EC%2584%259C%25EC%259A%25B8%2520%25ED%2595%259C%25EA%25B0%2595%252063%25EB%25B9%258C%25EB%2594%25A9%2520%25EB%2585%25B8%25EC%259D%2584%2520%25EB%25A7%259B%25EC%25A7%2591_%2520Seoul%2520Hangang%252063%2520Building%2520_%2520%25ED%2595%259C%25EA%25B0%2595%25EC%25B2%25A0%25EA%25B5%2590%252C%2520%25EB%2585%25B8%25EB%2593%25A4%25EC%2584%25AC%252C%252063%25EB%25B9%258C%25EB%2594%25A9%252C%2520%25EB%25AC%25BC%25EB%25A9%258D%252C%2520%25EC%2595%25BC%25EA%25B2%25BD%252C%2520%25EB%2585%25B8%25EC%259D%2584%25EB%25A9%258D%252C%2520%25ED%259E%2590%25EB%25A7%2581%25EB%25B0%25A9%25EC%2586%25A1%252C%2520%25EC%2597%25AC%25EC%259D%2598%25EB%258F%2584%2520-%2520YouTube%2520-%2520Chrome%25202022-12-14%252011-56-06.mp4%22&x-id=GetObject')
#         with col3:
#             st.subheader("서울시 내 소방서 표시")
# #             st.pydeck_chart(pdk.Deck(
# #           map_style=None,
# #            initial_view_state=pdk.ViewState(
# #         latitude=37.5642,
# #         longitude=127.0016,
# #         zoom=10,
# #         pitch=50,)))
        
            
#             df = pd.DataFrame(
#     np.random.randn(25, 2) / [40, 50] + [37.56, 127.00],
#     columns=['lat', 'lon'])

#             st.map(df)
            
    def 구급():
        col1,col2,col3=st.columns(3)
        with col1:
            st.subheader('구급 상황 발생 지역')
            df = pd.DataFrame(
            np.random.randn(1, 2) / [40, 50] + [37.5642, 127.0016],
            columns=['lat', 'lon'])

            st.map(df)
        with col2:
            st.subheader('실시간 현장 CCTV')
#             st.image('https://cdn.kado.net/news/photo/202205/1126349_551566_0650.jpg')
            st.video('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/08e6be41-79bf-49a8-9fee-b3d5bde2c029/%EB%8B%A8%EB%8F%85%EC%9E%85%EC%88%98_%EB%8F%99%EB%8C%80%EB%AC%B8%EC%86%8C%EB%B0%A9%EC%84%9C_119%EA%B5%AC%EA%B8%89%EB%8C%80_%ED%99%9C%EB%8F%99_CCTV%EC%98%81%EC%83%81_1_-_YouTube_-_Chrome_2022-12-14_12-06-42.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T030916Z&X-Amz-Expires=86400&X-Amz-Signature=e3c110ae21c13fabad21d5e6be9005fdcc3acdfd4f303342515f9516b81e5447&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%255B%25EB%258B%25A8%25EB%258F%2585%25EC%259E%2585%25EC%2588%2598%255D%2520%25EB%258F%2599%25EB%258C%2580%25EB%25AC%25B8%25EC%2586%258C%25EB%25B0%25A9%25EC%2584%259C%2520119%25EA%25B5%25AC%25EA%25B8%2589%25EB%258C%2580%2520%25ED%2599%259C%25EB%258F%2599%2520CCTV%25EC%2598%2581%25EC%2583%2581%25201%2520-%2520YouTube%2520-%2520Chrome%25202022-12-14%252012-06-42.mp4%22&x-id=GetObject')
            st.video('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/743116e8-59f4-483a-83b3-f87172d3b8fb/%EB%82%A8%EC%82%B0%EC%84%9C%EC%9A%B8%ED%83%80%EC%9B%8C_%ED%8C%8C%EB%85%B8%EB%9D%BC%EB%A7%88_LIVE_-_YouTube_-_Chrome_2022-12-14_11-50-07.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T113430Z&X-Amz-Expires=86400&X-Amz-Signature=1625f525a1ff87651be68e40a756372326bdb224c35b20ed78ab68327603be9c&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25EB%2582%25A8%25EC%2582%25B0%25EC%2584%259C%25EC%259A%25B8%25ED%2583%2580%25EC%259B%258C%2520%25ED%258C%258C%25EB%2585%25B8%25EB%259D%25BC%25EB%25A7%2588%2520LIVE%2520-%2520YouTube%2520-%2520Chrome%25202022-12-14%252011-50-07.mp4%22&x-id=GetObject')
#         with col3:
#             st.subheader("서울시 내 소방서 표시")
#             df = pd.DataFrame(
#     np.random.randn(25, 2) / [40, 50] + [37.56, 127.00],
#     columns=['lat', 'lon'])

#             st.map(df)
    def 구조():
        col1,col2,col3=st.columns(3)
        with col1:
            st.subheader('구조 상황 발생 지역')
            df = pd.DataFrame(
            np.random.randn(1, 2) / [40, 50] + [37.5642, 127.0016],
            columns=['lat', 'lon'])

            st.map(df)
        with col2:
            st.subheader('실시간 현장 CCTV')
#             st.image('https://pip-thumb.zumst.com/api/v1/swyze_VC002_77445815_content.jpeg?w=880&h=495')
            st.video('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/991d5dc0-cd29-4947-a9f0-fd2d525ef40b/%EB%AC%BC%EC%97%90_%EC%9E%A0%EA%B8%B4_%EC%B0%A8%EB%9F%89_%EC%8B%9C%EB%AF%BC%EB%93%A4%EB%8F%84_%EA%B3%A0%EB%A6%BDCCTV%EB%A1%9C_%EB%B3%B8_%EB%8F%84%EB%A1%9C_%EC%B9%A8%EC%88%98_%EC%83%81%ED%99%A9___SBS_-_YouTube_-_Chrome_2022-12-14_12-17-32.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T031807Z&X-Amz-Expires=86400&X-Amz-Signature=6522627c69dc0075afc4e8156dfb0185634feb3f37a08bb5e582907ef6dc2f0e&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25EB%25AC%25BC%25EC%2597%2590%2520%25EC%259E%25A0%25EA%25B8%25B4%2520%25EC%25B0%25A8%25EB%259F%2589%252C%2520%25EC%258B%259C%25EB%25AF%25BC%25EB%2593%25A4%25EB%258F%2584%2520%25EA%25B3%25A0%25EB%25A6%25BD%25E2%2580%25A6CCTV%25EB%25A1%259C%2520%25EB%25B3%25B8%2520%25EB%258F%2584%25EB%25A1%259C%2520%25EC%25B9%25A8%25EC%2588%2598%2520%25EC%2583%2581%25ED%2599%25A9%2520_%2520SBS%2520-%2520YouTube%2520-%2520Chrome%25202022-12-14%252012-17-32.mp4%22&x-id=GetObject')
#         with col3:
#             st.subheader("서울시 내 소방서 표시")
#             df = pd.DataFrame(
#     np.random.randn(25, 2) / [40, 50] + [37.56, 127.00],
#     columns=['lat', 'lon'])

#             st.map(df)
    def 시위():
        col1,col2,col3=st.columns(3)
        with col1:
            st.subheader('시위 상황 발생 지역')
            df = pd.DataFrame(
            np.random.randn(1, 2) / [40, 50] + [37.5642, 127.0016],
            columns=['lat', 'lon'])

            st.map(df)
            with col2:
                st.subheader('🚨🚨실시간 현장 CCTV🚨🚨')
#                 st.image('https://ichef.bbci.co.uk/news/640/cpsprodpb/16EEF/production/_109053939_origin_100_3.jpg')
                st.video('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/aadcf001-1738-4d77-92c7-9c8a83e126ef/%EC%8A%A4%EB%B8%8C%EC%8A%A4%EB%89%B4%EC%8A%A4_%EB%9D%BC%EC%9D%B4%EB%B8%8C_16%EC%B0%A8_%EC%B4%9B%EB%B6%88%EC%A7%91%ED%9A%8C_%EA%B4%91%ED%99%94%EB%AC%B8_%ED%98%84%EC%9E%A5%EC%9E%85%EB%8B%88%EB%8B%A4%21_-_YouTube_-_Chrome_2022-12-14_12-21-28.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T032229Z&X-Amz-Expires=86400&X-Amz-Signature=f3146fe3070c78eb91d0a81de47533b9ac8a4375cf7d0b9676e6437fbfc962d8&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25EC%258A%25A4%25EB%25B8%258C%25EC%258A%25A4%25EB%2589%25B4%25EC%258A%25A4%2520%25EB%259D%25BC%25EC%259D%25B4%25EB%25B8%258C%252016%25EC%25B0%25A8%2520%25EC%25B4%259B%25EB%25B6%2588%25EC%25A7%2591%25ED%259A%258C%2520%25EA%25B4%2591%25ED%2599%2594%25EB%25AC%25B8%2520%25ED%2598%2584%25EC%259E%25A5%25EC%259E%2585%25EB%258B%2588%25EB%258B%25A4%21%2520-%2520YouTube%2520-%2520Chrome%25202022-12-14%252012-21-28.mp4%22&x-id=GetObject')
                st.video('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/49254c09-269e-4601-a2b0-5fd7c8e4caaa/%EC%84%9C%EC%9A%B8%EC%8B%A4%EC%8B%9C%EA%B0%84_%EA%B4%91%ED%99%94%EB%AC%B8%EA%B4%91%EC%9E%A5%EB%9D%BC%EC%9D%B4%EB%B8%8C_Live_Cam_I_Seoul__Gwanghwamun_Square__I_%EC%84%9C%EC%9A%B8%EB%9D%BC%EC%9D%B4%EB%B8%8C_%EA%B4%91%ED%99%94%EB%AC%B8%EA%B4%91%EC%9E%A5_%EC%84%9C%EC%9A%B8%EB%B9%9B%EC%B4%88%EB%A1%B1%EC%B6%95%EC%A0%9C_%EC%84%9C%EC%9A%B8%EB%9D%BC%EC%9D%B4%ED%8A%B8%EA%B4%91%ED%99%94_%EA%B4%91%ED%99%94%EB%AC%B8%ED%81%AC%EB%A6%AC%EC%8A%A4%EB%A7%88%EC%8A%A4%EB%A7%88%EC%BC%93_%EB%8C%80%ED%98%95%ED%8A%B8%EB%A6%AC_-_YouTube_-_Chrome_2022-12-14_11-23-35.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221214T113509Z&X-Amz-Expires=86400&X-Amz-Signature=5745367efde29152f3b938c36fbb9c8410e842cbe8b1c893e8cb0072050beb3c&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25EC%2584%259C%25EC%259A%25B8%25EC%258B%25A4%25EC%258B%259C%25EA%25B0%2584%2520%25EA%25B4%2591%25ED%2599%2594%25EB%25AC%25B8%25EA%25B4%2591%25EC%259E%25A5%25EB%259D%25BC%25EC%259D%25B4%25EB%25B8%258C%2520Live%2520Cam%2520I%2520Seoul%2520_Gwanghwamun%2520Square_%2520I%2520%25EC%2584%259C%25EC%259A%25B8%25EB%259D%25BC%25EC%259D%25B4%25EB%25B8%258C%2520%25EA%25B4%2591%25ED%2599%2594%25EB%25AC%25B8%25EA%25B4%2591%25EC%259E%25A5%2520%25EC%2584%259C%25EC%259A%25B8%25EB%25B9%259B%25EC%25B4%2588%25EB%25A1%25B1%25EC%25B6%2595%25EC%25A0%259C%2520%25EC%2584%259C%25EC%259A%25B8%25EB%259D%25BC%25EC%259D%25B4%25ED%258A%25B8%25EA%25B4%2591%25ED%2599%2594%2520%25EA%25B4%2591%25ED%2599%2594%25EB%25AC%25B8%25ED%2581%25AC%25EB%25A6%25AC%25EC%258A%25A4%25EB%25A7%2588%25EC%258A%25A4%25EB%25A7%2588%25EC%25BC%2593%2520%25EB%258C%2580%25ED%2598%2595%25ED%258A%25B8%25EB%25A6%25AC%2520-%2520YouTube%2520-%2520Chrome%25202022-12-14%252011-23-35.mp4%22&x-id=GetObject')
#         with col3:
#             st.subheader("서울시 내 소방서 표시")
#             df = pd.DataFrame(
#     np.random.randn(25, 2) / [40, 50] + [37.56, 127.00],
#     columns=['lat', 'lon'])

#             st.map(df)
    page_names_to_funcs = { '사고유형을선택해주세요':사고유형을선택해주세요,'화재': 화재,'구급':구급,'구조':구조,'시위':시위 }
    selected_page =st.sidebar.selectbox('아래 재난 유형을 선택하세요',page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()

elif add_selectbox =='범죄':
    st.sidebar.title('-----112로 이관하겠습니다-----서울 경찰청 종합상황실 : 02-6150-1155')
    st.title('112 종합상황실')
    st.image('https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F277323345630656E1A')
else:
    st.title('정부 민원 안내 콜센터')
    st.image('http://www.outsourcing.co.kr/news/photo/202211/95401_34878_5915.jpg')
    st.sidebar.title('----100으로 이관하겠습니다----정부합동민원센터 : 110')
