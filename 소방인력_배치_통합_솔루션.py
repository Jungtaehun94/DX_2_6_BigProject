import inspect
import textwrap
from urllib.error import URLError
import pandas as pd
import pydeck as pdk
import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
from io import BytesIO
from urllib import request
from PIL import Image
from add_logo import add_logo
from up_down import up,down
from video import autoplay_muted_video

url = "https://nfds.go.kr/images/common/logo_emb.png"
res = request.urlopen(url).read()
logo_im = Image.open(BytesIO(res))

st.set_page_config(layout="wide",
    page_title="2반6조빅프로젝트 ",
    page_icon="🚒")

#     st.markdown('### 소방인력 배치 통합 솔루션')
add_logo()
# pages = st.source_util.get_pages('소방인력_배치_통합_솔루션.py')
# pages
# new_page_names = {
#   '사고발생현황': im,
#   '소방서별현황': im,
# }

# for key, page in pages.items():
#     if page['page_name'] in new_page_names:
#         page['icon'] = new_page_names[page['page_name']]

st.write()

df = pd.read_csv(r"./data.csv", encoding = 'cp949')
df_dpt = pd.read_csv(r"./data2.csv", encoding = 'cp949')

with st.sidebar:
            to_show = st.radio("지도 레이어 선택",('자치구별 인력 배치', '실시간 출동 현황'))
def mapping_demo():
    try:
        ALL_LAYERS = {
            "자치구별 인력 배치": pdk.Layer(
                "ScatterplotLayer",
#                 "ColumnLayer",
                data=df,
                get_position=["lng", "lat"],
                get_radius="(val-150)*1.5",
                get_elevation = 10,
#                 get_elevation="val",
#                 radius=300,
#                 elevation_scale=10,
                stroked=True,
                get_line_color=[255, 0, 0],
                radius_min_pixels=15,
                radius_max_pixels=100,
                line_width_min_pixels=1,
                radius_scale=6,
                pickable=True,
                elevation_range=[0, 400],
                get_fill_color=["val*0.71", 0, 0, "(val-100)*0.71"],
                extruded=True,
            ),
            "실시간 출동 현황": pdk.Layer(
                "ColumnLayer",
                data=df_dpt.sample(1),
                get_position=["lng", "lat"],
                get_elevation="deficiency*100",
                radius=300,
                elevation_scale=1,
                pickable=True,
                elevation_range=[0, 400],
#                 get_fill_color=["deficiency*0.07", 1,"deficiency*7", 128],
                get_fill_color=["deficiency*10", "0","0", "128"],
                extruded=True,
            )
        }
#         with st.sidebar:
#             to_show = st.radio("지도 레이어 선택",('자치구별 인력 배치', '실시간 출동 현황'))
        selected_layers = [layer for layer_name, layer in ALL_LAYERS.items() if to_show == layer_name]
        if selected_layers:
            st.pydeck_chart(
                pdk.Deck(map_style=None,
                    initial_view_state={
                        "latitude": 37.55,
                        "longitude": 126.99,
                        "zoom": 11,
                        "pitch": 55,
                        "width": '100%',
                        "height": 650,                        
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
if to_show == '자치구별 인력 배치':
    cols_title = st.columns((12,2,1))
    i = 0
    with cols_title[0]:
        st.markdown("## 서울시 소방서별 필요인력")
    with cols_title[1]:
        st.markdown("## 인력현황")
    with cols_title[2]:
        st.markdown("""<p style="font-size:10%;"/>""", unsafe_allow_html=True)
        st.markdown(up(), unsafe_allow_html=True)
        st.markdown(down(), unsafe_allow_html=True)
    cols =st.columns((12,1,1,1))
else:
    cols_title = st.columns((7,5,2,1))
    i = 1
    with cols_title[0]:
        st.markdown("## 화재 발생지역")
    with cols_title[1]:
        st.markdown("## 현장 카메라")
    with cols_title[2]:
        st.markdown("## 인력현황")
    with cols_title[3]:
        st.markdown("""<p style="font-size:10%;"/>""", unsafe_allow_html=True)
        st.markdown(up(), unsafe_allow_html=True)
        st.markdown(down(), unsafe_allow_html=True)
    cols =st.columns((7,5,1,1,1))


import altair as alt
df = pd.read_csv(r"./data.csv", encoding = 'cp949')
df['22년 실제 소방공무원'] = df['22년 실제 소방공무원'] + df['감원']
df['감원'] = df['감원'].abs()
order="{'22년 실제 소방공무원':0, '증원': 1, '감원': 2}"
column = "['#0000FF', '#00FF00', '#FF0000]"
bar_chart = alt.Chart(df, height = 500).transform_fold(
  ['22년 실제 소방공무원', '증원', '감원'],
  as_=['column', 'value']
).mark_bar(size=13).encode(
    y='gu:N',
    x='value:Q',
    color=alt.Color('column:N',scale=alt.Scale(domain=['22년 실제 소방공무원', '증원', '감원'],range=['#264b96', 'green', 'red'])),
#     color=alt.Color('column:N',scale=alt.Scale(domain=['22년 실제 소방공무원', '증원', '감원'],range=['#264b96', '#006f3c', '#bf212f'])),%%!
    order="order:O"
)
import pandas as pd
df3 = pd.read_csv("LOCAL_PEOPLE_20221211.csv", encoding = 'cp949', low_memory=False, index_col=False)

#     df3['TOT_LVPOP_CO'].astype(float)
df3 = df3.groupby(by = ['행정동코드', '기준일ID', '시간대구분'], as_index=False).sum()
df3 = df3.loc[df3["기준일ID"] == df3["기준일ID"].unique().tolist()[-1], :]

# 최종 데이터 시각
latest_time_hr = df3.loc[df3['총생활인구수'] != 0, :]["시간대구분"].unique().tolist()[-1]

# 실시간 데이터가 없으므로 일단 현재시각 덮어씌우기
import datetime
import pytz
kst = pytz.timezone('Asia/Seoul')
current_time = datetime.datetime.now(kst)
latest_time_hr = latest_time_ = current_time.hour

df3 = df3.loc[df3["시간대구분"] == latest_time_hr, :]
ampm = "오후" if latest_time_hr > 12 else "오전"
latest_time_hr = (latest_time_hr - 12) if latest_time_hr > 12 else latest_time_hr
df3['총생활인구수'].replace({0:np.NaN}, inplace = True)
chart_data = df3[["행정동코드", "총생활인구수"]]
# cols[1].metric('','현재','증원')
# cols[2].metric('','인력','-감소')
# cols[3].metric('','현황',' ')
# cols[3].markdown('###')
metric_counter = 0
for dpt in df['출동소방서'].unique().tolist():
    temp_df = df.loc[df['출동소방서'] == dpt,:].reset_index()
    with cols[metric_counter%3+i+1]:
        st.metric(dpt, temp_df['22년 실제 소방공무원'][0], temp_df['오차'][0].astype(str))
    metric_counter +=1
    if metric_counter > 17:
        break;

with cols[0]:
    mapping_demo()
if to_show == '실시간 출동 현황':
    with cols[1]:
        autoplay_muted_video('바디캠1.mp4')
        autoplay_muted_video('바디캠2.mp4')
        autoplay_muted_video('바디캠3.mp4')
    new_cols = st.columns((12,1,1,1))
    new_cols[0].markdown(f'### 자치구별 유동 인구 현황 ({ampm} {latest_time_hr}시 기준)')
    new_cols[0].bar_chart(chart_data, x="행정동코드", y="총생활인구수")
else:
    new_cols = st.columns((12,1,1,1))
    new_cols[0].altair_chart(bar_chart, use_container_width=True)
    
metric_counter = 0
for dpt in df['출동소방서'].unique().tolist()[17:]:
    temp_df = df.loc[df['출동소방서'] == dpt,:].reset_index()
    with new_cols[metric_counter%3+1]:
        st.metric(dpt, temp_df['22년 실제 소방공무원'][0], temp_df['오차'][0].astype(str))
    metric_counter +=1
    if metric_counter > 17:
        break;
        

if to_show == '실시간 출동 현황':
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
                st.markdown("""
                <video controls width = 450 autoplay="true" muted="true" loop="true">
                <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/Campsite%20Fire.mp4" type="video/mp4" />
                </video>
                """, unsafe_allow_html=True)
                st.markdown("""
                <video controls width = 450 autoplay="true" muted="true" loop="true">
                <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/Seoul_Night_View.mp4" type="video/mp4" />
                </video>
                """, unsafe_allow_html=True)
            with col3:
                st.markdown('###')
                st.markdown('##')
                st.markdown("""
                <video controls width = 450 autoplay="true" muted="true" loop="true">
                <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/Thermal.mp4" type="video/mp4" />
                </video>
                """, unsafe_allow_html=True)
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
                st.markdown("""
                <video controls width = 450 autoplay="true" muted="true" loop="true">
                <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/paramedics.mp4" type="video/mp4" />
                </video>
                """, unsafe_allow_html=True)
                st.markdown("""
                <video controls width = 450 autoplay="true" muted="true" loop="true">
                <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/Namsan.mp4" type="video/mp4" />
                </video>
                """, unsafe_allow_html=True)
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
                st.markdown("""
                    <video controls width = 450 autoplay="true" muted="true" loop="true">
                    <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/Flood.mp4" type="video/mp4" />
                    </video>
                    """, unsafe_allow_html=True)
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
                    st.markdown("""
                    <video controls width = 450 autoplay="true" muted="true" loop="true">
                    <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/OpenCV%20People%20Counting%20Demo%20%232-3iiodzoG80A.mp4" type="video/mp4"/>
                    </video>
                    """, unsafe_allow_html=True)
                    st.markdown("""
                    <video controls width = 450 autoplay="true" muted="true" loop="true">
                    <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/candlelight vigil.mp4" type="video/mp4" />
                    </video>
                    """, unsafe_allow_html=True)
                    st.markdown("""
                    <video controls width = 450 autoplay="true" muted="true" loop="true">
                    <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/X-mas.mp4" type="video/mp4" />
                    </video>
                    """, unsafe_allow_html=True)
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
