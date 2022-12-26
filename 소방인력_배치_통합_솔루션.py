# from vega_datasets import data
import inspect
import textwrap
from urllib.error import URLError
import pandas as pd
import pydeck as pdk
from pydeck.types import String
import numpy as np
import altair as alt
import streamlit as st
from streamlit.hello.utils import show_code
from io import BytesIO
from urllib import request
from PIL import Image
from add_logo import add_logo
from up_down import up, down
from video import autoplay_muted_video
from PIL import Image
from Miscs import find_close_points, URL_to_Icon_Data, assign_icons

url = "https://nfds.go.kr/images/common/logo_emb.png"
res = request.urlopen(url).read()
logo_im = Image.open(BytesIO(res))

st.set_page_config(layout="wide", page_title="2반6조빅프로젝트 ", page_icon="🚒")

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

df = pd.read_csv(r"./data.csv", encoding="cp949")
df_text = df.copy()
df_text["증원"] = df_text["증원"].where(df_text["증원"] > 0, "")
df_text["감원"] = df_text["감원"].where(df_text["감원"] < 0, "")

df_text["현원"] = df_text["현원"].astype(str)

df_text["오차"] = df_text["오차"].astype(str)

df_text["증원"] = df_text["증원"].astype(str)
df_text["감원"] = df_text["감원"].astype(str)
df_text["감원"] = df_text["감원"].str[1:]
df_text["증원"] = ("(" + df_text["증원"] + ")").where(df_text["증원"] != "", "")
df_text["감원"] = ("(" + df_text["감원"] + ")").where(df_text["감원"] != "", "")
df_inc = df_text.copy()
df_inc["현원"] = df_inc["현원"].where(df_text["증원"] != "", "")
df_dec = df_text.copy()
df_dec["현원"] = df_dec["현원"].where(df_text["감원"] != "", "")
df_zero = df_text.copy()
df_zero["현원"] = df_zero["현원"].where(df_zero["오차"] == "0", "")
df_dpt = pd.read_csv(r"./data2.csv", encoding="cp949")

# import pandas as pd

# # Create a list of longitude values from 37 to 38 in steps of 0.01
# lng_values = list(range(370, 375))
# lng_values = [x / 10 for x in lng_values]

# # Create a list of latitude values from 126 to 128 in steps of 0.01
# lat_values = list(range(1270, 1275))
# lat_values = [x / 10 for x in lat_values]

# # Create an empty list to store the rows of the dataframe
# rows = []

# # Iterate over the longitude values
# for lng in lng_values:
#   # For each longitude value, add a row for each latitude value
#   for lat in lat_values:
#     rows.append({'lng': lng, 'lat': lat, 'val': 10})


# # Create a dataframe from the rows
# df_grid = pd.DataFrame(rows)
# df_grid


df_dpt, supp_list = find_close_points(df_dpt, df_dpt.sample(1).reset_index()["출동소방서"][0], 3)
gu_loc = df_dpt.columns.get_loc('출동소방서')

with st.sidebar:
    to_show = st.radio("유형별", ("평시", "재난 발생시"))
# find_close_points(df_dpt,df_dpt.sample(1).reset_index()['출동소방서'][0],3)


def mapping_demo():
    try:
        df_dec_icons = df_dec.loc[df_dec["감원"] != "", :].copy()
        assign_icons(
            df_dec_icons, "https://img.icons8.com/plasticine/100/000000/marker.png"
        )
        df_inc_icons = df_inc.loc[df_dec["증원"] != "", :].copy()
        assign_icons(
            df_inc_icons,
            "https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/100_green_marker.png",
        )
        ALL_LAYERS = {
            "평시": pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position=["lng", "lat"],
                # radius 0 줘서 숨겨놨음
                get_radius="0",
                get_elevation=10,
                stroked=True,
                get_line_color=[255, 0, 0],
                line_width_min_pixels=1,
                radius_scale=6,
                pickable=True,
                elevation_range=[0, 400],
                get_fill_color=["255", "128", 0, "192"],
                extruded=True,
            ),
            "재난 발생시": pdk.Layer(
                "ColumnLayer",
                data=df_dpt,
                get_position=["lng", "lat"],
                get_elevation="deficiency*0",
                radius=150 * 0,
                elevation_scale=1,
                pickable=True,
                elevation_range=[0, 400],
                #                 get_fill_color=["deficiency*0.07", 1,"deficiency*7", 128],
                #                 get_fill_color=["deficiency*10", "0","0", "128"],
                get_fill_color=["r", "g", "b"],
                extruded=True,
            ),
        }
        aaa = pdk.Layer(
            "ColumnLayer",
            data=df_text,
            get_position=["lng", "lat"],
            get_elevation="-오차*100",
            radius=300,
            elevation_scale=1,
            pickable=True,
            elevation_range=[0, 400],
            #                 get_fill_color=["deficiency*0.07", 1,"deficiency*7", 128],
            get_fill_color=["255", "32", "0", "128"],
            extruded=True,
        )
        bbb = pdk.Layer(
            "ColumnLayer",
            data=df,
            get_position=["lng", "lat"],
            get_elevation="오차*100",
            radius=300,
            elevation_scale=1,
            pickable=True,
            elevation_range=[0, 400],
            #                 get_fill_color=["deficiency*0.07", 1,"deficiency*7", 128],
            get_fill_color=["0", "192", "128", "128"],
            extruded=True,
        )
        ccc = pdk.Layer(
            "TextLayer",
            data=df_inc,
            get_position=["lng", "lat-0.01"],
            get_text="현원 + 증원",
            get_size=30,
            get_color=[64, 192, 64],
            get_angle=0,
            # Note that string constants in pydeck are explicitly passed as strings
            # This distinguishes them from columns in a data set
            get_text_anchor=String("middle"),
            get_alignment_baseline=String("center"),
        )
        ddd = pdk.Layer(
            "TextLayer",
            data=df_dec,
            get_position=["lng+0.017", "lat-0.005"],
            get_text="현원 + 감원",
            get_size=30,
            get_color=[192, 64, 64],
            get_angle=0,
            # Note that string constants in pydeck are explicitly passed as strings
            # This distinguishes them from columns in a data set
            get_text_anchor=String("middle"),
            get_alignment_baseline=String("center"),
        )
        eee = pdk.Layer(
            "TextLayer",
            data=df_zero,
            get_position=["lng", "lat-0.01"],
            get_text="현원",
            get_size=30,
            get_color=[64, 64, 64],
            get_angle=0,
            # Note that string constants in pydeck are explicitly passed as strings
            # This distinguishes them from columns in a data set
            get_text_anchor=String("middle"),
            get_alignment_baseline=String("center"),
        )
        fff = pdk.Layer(
            type="IconLayer",
            data=df_dec_icons,
            get_icon="icon_data",
            get_size=4,
            size_scale=15,
            get_position=["lng", "lat"],
            pickable=True,
            extruded=False,
        )
        ggg = pdk.Layer(
            type="IconLayer",
            data=df_inc_icons,
            get_icon="icon_data",
            get_size=4,
            size_scale=15,
            get_position=["lng", "lat"],
            pickable=True,
            extruded=False,
        )
        hhh = (
            pdk.Layer(
                "TextLayer",
                data=df_dpt,
                get_position=["lng", "lat-0.005"],
                get_text="소방공무원_22",
                get_size=30,
                get_color=["r", "g", "b"],
                get_angle=0,
                # Note that string constants in pydeck are explicitly passed as strings
                # This distinguishes them from columns in a data set
                get_text_anchor=String("middle"),
                get_alignment_baseline=String("center"),
            ),
        )
        iii = (
            pdk.Layer(
                "ArcLayer",
                data=df_dpt,
                get_width="20",
                get_source_position=["lng", "lat"],
                get_target_position=["lng_dest", "lat_dest"],
                #                         get_tilt=30,
                pickable=True,
                #                 get_fill_color=["deficiency*0.07", 1,"deficiency*7", 128],
                #                 get_fill_color=["deficiency*10", "0","0", "128"],
                get_source_color=["255", "127", "0", "32"],
                get_target_color=["255", "127", "0", "192"],
                extruded=True,
                auto_highlight=True,
            ),
        )
        jjj = pdk.Layer(
            "ScatterplotLayer",
            data=df_dpt.loc[0:0,],
            get_position=["lng", "lat"],
            # radius 0 줘서 숨겨놨음
            get_radius="100",
            #                         stroked=True,
            #                         get_line_color=[128, 128, 0],
            line_width_min_pixels=1,
            radius_scale=6,
            pickable=True,
            elevation_range=[0, 400],
            get_fill_color=["192", "192", 0, "64"],
            extruded=True,
        )
        kkk = pdk.Layer(
            type="IconLayer",
            data=df_dpt,
            get_icon="icon_data",
            get_size=4,
            size_scale=15,
            get_position=["lng", "lat-0.003"],
            pickable=True,
            extruded=False,
        )
        lll = pdk.Layer(
            type="IconLayer",
            data=df_inc_icons,
            get_icon="icon_data",
            get_size=4,
            size_scale=15,
            get_position=["lng", "lat-0.002"],
            pickable=True,
            extruded=False,
        )

        #         with st.sidebar:
        #             to_show = st.radio("유형별",('평시', '재난 발생시'))
        selected_layers = [
            layer for layer_name, layer in ALL_LAYERS.items() if to_show == layer_name
        ]
        selected_layer_name = [
            layer_name
            for layer_name, layer in ALL_LAYERS.items()
            if to_show == layer_name
        ]
        if selected_layer_name[0] == "평시":
            selected_layers += [ccc, ddd, eee, fff, ggg]
            #             selected_layers = [ccc]
            st.pydeck_chart(
                pdk.Deck(
                    map_style=None,
                    initial_view_state={
                        "latitude": 37.55,
                        "longitude": 126.99,
                        "zoom": 10.5,
                        "pitch": 40,
                        "width": "100%",
                        "height": 650,
                    },
                    tooltip={
                        "html": "<b>{출동소방서}</b><br>현원: {현원}<br>예측 적정인력: {현원} + {오차}<br>전체출동건수: {전체출동건수}<br>1인출동건수: {1인출동건수}<br>구급이송인원: {구급이송인원}<br>생존구조인원: {생존구조인원}<br>재산피해경감율: {재산피해경감율}",
                        "style": {"color": "white"},
                    },
                    layers=selected_layers,
                )
            )
        elif selected_layer_name[0] == "재난 발생시":
            selected_layers += [hhh, iii, jjj, kkk]
            st.pydeck_chart(
                pdk.Deck(
                    map_style=None,
                    initial_view_state={
                        "latitude": df_dpt["lat"].mean(),
                        "longitude": df_dpt["lng"].mean(),
                        "zoom": 11,
                        "pitch": 40,
                        "width": '100%',
                        "height": 430,
                    },
                    tooltip={
                        "html": "<b>{출동소방서}</b><br>가용인원: {dpt}<br>차출: {차출}",
                        "style": {"color": "white"},
                    },
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


if to_show == "재난 발생시":
    cols_head = st.columns((2.5, 3.8, 2))
    #     with cols_head[0]:

    #         imagee = Image.open('캡쳐5.png')

    #         st.image(imagee,width=250)
    with cols_head[0]:
        st.markdown("<div><h2 id='-' style='letter-spacing: 6px;'align='left';>현장CCTV</h1></div>", unsafe_allow_html=True)
    with cols_head[1]:
        st.markdown("<div><h2 id='-' style='letter-spacing: 2px;'align='left';>재난 발생시 소방서별 필요인력</h1></div>", unsafe_allow_html=True)
    with cols_head[2]:
        st.markdown("<div><h2 id='-' style='letter-spacing: 6px;'align='left';>인력 현황</h1></div>", unsafe_allow_html=True)
    #         st.markdown("# 적정 인력 : 0 3 0 0 명　　 출동 인력 : 0 2 5 5 명")
#     with cols_head[2]:
#         #         st.markdown("#             ")
#         st.markdown("<div style='background-color: aqua;'><h1 id='-'>2　단계　 🚨　  </h1></div>", unsafe_allow_html=True)
#         st.markdown("# 필요 인력　　 + 0 0 4 5 명")
#     with cols_head[3]:
#         image = Image.open('캡처.PNG')

#         st.image(image)
#         st.markdown('##### 　실시간 출동인력 ')


#         chart_data = pd.DataFrame(
#         np.random.randn(13, 3),
#         columns=["a", "b", "c"])

#         st.bar_chart(chart_data)

#     with cols_head[3]:

#         source = pd.DataFrame({"values": [12, 23, 47, 6, 52, 19]})

#         base = alt.Chart(source).encode(
#         theta=alt.Theta("values:Q", stack=True),
#         radius=alt.Radius("values", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
#         color="values:N",
# )

#         c1 = base.mark_arc(innerRadius=20, stroke="#fff")

#         c2 = base.mark_text(radiusOffset=10).encode(text="values:Q")

#         c1 + c2

if to_show == "평시":
    cols_title = st.columns((12, 2, 1))
    i = 0
    with cols_title[0]:
        st.markdown("##  평시 소방서별 필요인력")
    with cols_title[1]:
        st.markdown("## 인력현황")
    with cols_title[2]:
        st.markdown("""<p style="font-size:10%;"/>""", unsafe_allow_html=True)
        st.markdown(up(), unsafe_allow_html=True)
        st.markdown(down(), unsafe_allow_html=True)
    cols = st.columns((12, 1, 1, 1))
else:
#     cols_title = st.columns((0.9, 1.5, 1.5, 0.9))
#     i = 1
    #     with cols_title[0]:
    #         st.markdown("## 화재 발생지역")
    #     with cols_title[3]:
    #         st.markdown("""<p style="font-size:10%;"/>""", unsafe_allow_html=True)
    #         st.markdown(up(), unsafe_allow_html=True)
    #         st.markdown(down(), unsafe_allow_html=True)
    cols = st.columns((2, 6, 2))
import altair as alt

df = pd.read_csv(r"./data.csv", encoding="cp949")
df["현원"] = df["현원"] + df["감원"]
df["감원"] = df["감원"].abs()
order = "{'현원':0, '증원': 1, '감원': 2}"
column = "['#0000FF', '#00FF00', '#FF0000]"
bar_chart = (
    alt.Chart(df, height=500)
    .transform_fold(["현원", "증원", "감원"], as_=["column", "value"])
    .mark_bar(size=13)
    .encode(
        y=alt.Y("gu:N",title='자치구'),
        x=alt.X("value:Q",title='소방인력'),
        color=alt.Color("column:N",
                        title='범례',
                        scale=alt.Scale(domain=["현원", "증원", "감원"],
                                        range=["#264b96", "green", "red"]),
                       ),
        #     color=alt.Color('column:N',scale=alt.Scale(domain=['현원', '증원', '감원'],range=['#264b96', '#006f3c', '#bf212f'])),
        order="order:O",
    )
).configure_legend(titleFontSize=20, labelFontSize=16)
df3 = pd.read_csv(
    "LOCAL_PEOPLE_20221211.csv", encoding="cp949", low_memory=False, index_col=False
)

#     df3['TOT_LVPOP_CO'].astype(float)
df3 = df3.groupby(by=["행정동코드", "기준일ID", "시간대구분"], as_index=False).sum()
df3 = df3.loc[df3["기준일ID"] == df3["기준일ID"].unique().tolist()[-1], :]

# 실시간 데이터가 없으므로 일단 현재시각 덮어씌우기
import datetime
import pytz

kst = pytz.timezone("Asia/Seoul")
current_time = datetime.datetime.now(kst)
# # 현재 시각
# latest_time_hr = latest_time_ = current_time.hour
# # 마지막 데이터 시각
# latest_time_hr = df3.loc[df3["유동인구"] != 0, :]["시간대구분"].unique().tolist()[-1]

# cols[1].metric('','현재','증원')
# cols[2].metric('','인력','-감소')
# cols[3].metric('','현황',' ')
# cols[3].markdown('###')
if to_show == "재난 발생시":
    st.empty()
#     metric_counter = 0
#     for dpt in df_dpt['출동소방서'].unique().tolist():
#         temp_df = df_dpt.loc[df_dpt['출동소방서'] == dpt,:].reset_index()
#         with cols[metric_counter%3+i+1]:
#             st.metric(dpt, temp_df['dpt'][0], temp_df['deficiency'][0].astype(str))
#         metric_counter +=1
#         if metric_counter > 17:
#             break;
else:
    metric_counter = 0
    for dpt in df["출동소방서"].unique().tolist():
        temp_df = df.loc[df["출동소방서"] == dpt, :].reset_index()
        with cols[metric_counter % 3 + i + 1]:
            st.metric(dpt, temp_df["현원"][0], temp_df["오차"][0].astype(str))
        metric_counter += 1
        if metric_counter > 17:
            break
    with cols[0]:
        mapping_demo()
        st.markdown(
            """<style> @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@800&family=Noto+Sans+KR:wght@500&display=swap'); </style><div style="margin-left: 28px;margin-top: -650px;z-index: 999;position: relative;width: 276px;height: 50px;background-color: rgba(0, 0, 0, 0.5);">
  <ul style="display: flex; flex-direction: row; width: 280px; align-items: center; padding-left: 0px; padding-top: 7px; padding-bottom: 7px;">
    <li style="align-items: center; cursor: pointer; display: flex; flex-direction: row; margin-left: 10px; margin-top: auto; align-content: center;"><span style="background: rgba(192, 64, 64, 0.8); border-color: rgb(255, 99, 132); border-width: 3px; display: inline-block; height: 20px; margin-right: 10px; width: 20px;"></span>
      <p style="color: rgb(218, 218, 218); margin: 0px; padding: 0px; font-family: &quot;Noto Sans KR&quot;, sans-serif; font-size: 18px;">감원 필요</p>
    </li>
    <li style="align-items: center; cursor: pointer; display: flex; flex-direction: row; margin-left: 20px;"><span style="background: rgba(64, 192, 64, 0.8); border-color: rgb(54, 162, 235); border-width: 3px; display: inline-block; height: 20px; margin-right: 10px; width: 20px;"></span>
      <p style="color: rgb(218, 218, 218); margin: 0px; padding: 0px; font-family: &quot;Noto Sans KR&quot;, sans-serif; font-size: 18px;">증원 필요</p>
    </li>
  </ul>
</div>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            """ <style>[id="deckgl-wrapper"] {margin-top: 0px;}</style> """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """ <style>[class~="css-1sdqqxz e1tzin5v2"] {font-family: &quot;Noto Sans KR&quot;}</style> """,
            unsafe_allow_html=True,
        )
if to_show == "재난 발생시":
    ne_cols = st.columns((2.5, 3.8, 1, 1))
    n_cols = st.columns((9))
    with ne_cols[1]:
        mapping_demo()
        st.markdown(
            """<div style="margin-left: 12px;margin-top: -435px;z-index: 999;position: relative;width: 315px;height: 50px;background-color: rgba(0, 0, 0, 0.5);">
            <ul style="display: flex; flex-direction: row; width: 342px; align-items: center; padding-left: 0px; padding-top: 7px; padding-bottom: 7px;">
            <li style="align-items: center; cursor: pointer; display: flex; flex-direction: row; margin-left: 10px; margin-top: auto; align-content: center;"><span style="background: rgba(192, 64, 64, 0.8); border-color: rgb(255, 99, 132); border-width: 3px; display: inline-block; height: 20px; margin-right: 10px; width: 20px;"></span>
            <p style="color: rgb(218, 218, 218); margin: 0px; padding: 0px; font-family: &quot;Noto Sans KR&quot;, sans-serif; font-size: 18px;">지원 소방서</p>
            </li>
            <li style="align-items: center; cursor: pointer; display: flex; flex-direction: row; margin-left: 20px;"><span style="background: rgba(64, 192, 64, 0.8); border-color: rgb(54, 162, 235); border-width: 3px; display: inline-block; height: 20px; margin-right: 10px; width: 20px;"></span>
            <p style="color: rgb(218, 218, 218); margin: 0px; padding: 0px; font-family: &quot;Noto Sans KR&quot;, sans-serif; font-size: 18px;">관할 소방서</p>
            </li>
            </ul>
            </div>""",
            unsafe_allow_html=True,
        )
#         st.markdown("#　")
#         st.markdown("#　")
#         st.markdown("#　")
#         st.markdown("#　")

    with ne_cols[0]:
        st.markdown("""<p style="font-size:10%;"/>""", unsafe_allow_html=True)
        autoplay_muted_video("인구카운팅.mp4", width=400)
        autoplay_muted_video("화재2.mp4", width=400)
    #         st.bar_chart(chart_data, x="행정동코드", y="유동인구")

    #         autoplay_muted_video('바디캠3.mp4', width=260)
    with ne_cols[2]:
        st.metric("충원 필요 소방서", df_dpt.iloc[0, gu_loc].replace('소방서', ''), sum(supp_list))
        st.metric("차출 대상 소방서", df_dpt.iloc[1, gu_loc].replace('소방서', ''), -supp_list[0])
        
#         st.metric("충원 필요 소방서", "서초", "15명 ")
#         st.metric("충원 필요 소방서", "강남", "20명 ")
#         st.markdown(" 출동 대응 1단계<br>필요 인력",unsafe_allow_html=True)
#         st.markdown(" 출동 대응 2단계<br>필요 인력",unsafe_allow_html=True)
#         st.markdown(" 출동 대응 3단계<br>필요 인력",unsafe_allow_html=True)
    #         st.markdown("""<style>[data-testid="stVerticalBlock"] {font-family: &quot;Noto Sans KR&quot;}</style>""",unsafe_allow_html=True)
    #         autoplay_muted_video('화재1.mp4', width=260)
    #         autoplay_muted_video('화재2.mp4', width=260)

    #         imagee = Image.open('캡처3.PNG')

    #         st.image(imagee,width=260)
    with ne_cols[3]:
        metrics = []
        for i in range(1,len(supp_list)):
            st.metric("차출 대상 소방서", df_dpt.iloc[i+1, gu_loc].replace('소방서', ''), -supp_list[i])
#             st.metric("충원 필요 소방서", df_dpt.iloc[i, gu_loc], supp_list[i])
#         st.metric("충원 필요 소방서", "동작", "17명")
#         st.metric("충원 필요 소방서", "송파", "8명")
#         st.markdown("1 개 소방서　　　출동　<br>&nbsp;",unsafe_allow_html=True)
#         st.markdown("2~5 개 소방서　　출동　<br>&nbsp;",unsafe_allow_html=True)
#         st.markdown("6 개 이상 소방서　 출동　<br>&nbsp;",unsafe_allow_html=True)
        st.markdown("""<p style="font-size:10%;"/>""", unsafe_allow_html=True)
    st.markdown('### 자치구별 유동 인구')
    new_ne_cols = st.columns((7.5, 2))
    df_4_chart3 = df3.copy()
    df_4_chart3["유동인구"].replace({0: np.NaN}, inplace=True)
    def update_chart_data(latest_time_hr):
            return df_4_chart3[df_4_chart3["시간대구분"] == latest_time_hr]
#     ampm = "오후" if latest_time_hr > 12 else "오전"
#     latest_time_hr = (latest_time_hr - 12) if latest_time_hr > 12 else latest_time_hr
    with new_ne_cols[1]:
            latest_time_hr = st.slider("조회할 시간대 선택:", 0, 24, step=1)
    with new_ne_cols[0]:
        st.bar_chart(update_chart_data(latest_time_hr), x="행정동코드", y="유동인구")
#     df_4_chart3 = df_4_chart3[["행정동코드", "유동인구"]]
    
    chart_data2 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
#         line_chart(chart_data2, width=4, use_container_width=True)
    
else:
    new_cols = st.columns((12, 1, 1, 1))
    new_cols[0].altair_chart(bar_chart, use_container_width=True)
# if to_show == '재난 발생시':
# #     st.empty()
#     chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     nee_columns=['a', 'b', 'c'])

#     st.line_chart(chart_data)
#     nee_cols = st.nee_columns((1,4,6,8))
#     nee_cols = st.nee_columns((12,1,1,1))
#     nee_cols[0].markdown(f'### 자치구별 유동 인구 현황 ({ampm} {latest_time_hr}시 기준)')
#     nee_cols[0].bar_chart(chart_data, x="행정동코드", y="유동인구")

#     metric_counter = 0
#     for dpt in df['출동소방서'].unique().tolist()[17:]:
#         temp_df = df_dpt.loc[df_dpt['출동소방서'] == dpt,:].reset_index()
#         with new_cols[metric_counter%3+1]:
#             st.metric(dpt, temp_df['dpt'][0], temp_df['deficiency'][0].astype(str))
#         metric_counter +=1
#         if metric_counter > 17:
#             break;
# else:
#     metric_counter = 0
#     for dpt in df['출동소방서'].unique().tolist()[17:]:
#         temp_df = df.loc[df['출동소방서'] == dpt,:].reset_index()
#         with nee_cols[metric_counter%3+1]:
#             st.metric(dpt, temp_df['22년 실제 소방공무원'][0], temp_df['오차'][0].astype(str))
#         metric_counter +=1
#         if metric_counter > 17:
#             break;


# if to_show == "재난 발생시":
#     with st.sidebar:
#         st.title("119 종합 상황 센터")
#     add_selectbox = st.sidebar.selectbox("신고 유형을 선택하세요", ("재난", "범죄", "민원/상담"))
#     if add_selectbox == "재난":

#         def 사고유형을선택해주세요():
#             st.empty()

#         def 화재():
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.subheader("화재 상황 발생 지역")
#                 df = pd.DataFrame(
#                     np.random.randn(1, 2) / [40, 50] + [37.5642, 127.0016],
#                     columns=["lat", "lon"],
#                 )

#                 st.map(df)
#             #             st.pydeck_chart(pdk.Deck(
#             #           map_style=None,
#             #            initial_view_state=pdk.ViewState(
#             #         latitude=37.5642,
#             #         longitude=127.0016,
#             #         zoom=10,
#             #         pitch=50,)))
#             #             chart_data = pd.DataFrame(
#             #    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#             #    columns=['lat', 'lon'])
#             with col2:
#                 st.subheader("실시간 현장CCTV")
#                 st.markdown(
#                     """
#                 <video controls width = 450 autoplay="true" muted="true" loop="true">
#                 <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/Campsite%20Fire.mp4" type="video/mp4" />
#                 </video>
#                 """,
#                     unsafe_allow_html=True,
#                 )
#                 st.markdown(
#                     """
#                 <video controls width = 450 autoplay="true" muted="true" loop="true">
#                 <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/Seoul_Night_View.mp4" type="video/mp4" />
#                 </video>
#                 """,
#                     unsafe_allow_html=True,
#                 )
#             with col3:
#                 st.markdown("###")
#                 st.markdown("##")
#                 st.markdown(
#                     """
#                 <video controls width = 450 autoplay="true" muted="true" loop="true">
#                 <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/Thermal.mp4" type="video/mp4" />
#                 </video>
#                 """,
#                     unsafe_allow_html=True,
#                 )

#         #         with col3:
#         #             st.subheader("서울시 내 소방서 표시")
#         # #             st.pydeck_chart(pdk.Deck(
#         # #           map_style=None,
#         # #            initial_view_state=pdk.ViewState(
#         # #         latitude=37.5642,
#         # #         longitude=127.0016,
#         # #         zoom=10,
#         # #         pitch=50,)))

#         #             df = pd.DataFrame(
#         #     np.random.randn(25, 2) / [40, 50] + [37.56, 127.00],
#         #     columns=['lat', 'lon'])

#         #             st.map(df)

#         def 구급():
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.subheader("구급 상황 발생 지역")
#                 df = pd.DataFrame(
#                     np.random.randn(1, 2) / [40, 50] + [37.5642, 127.0016],
#                     columns=["lat", "lon"],
#                 )

#                 st.map(df)
#             with col2:
#                 st.subheader("실시간 현장 CCTV")
#                 #             st.image('https://cdn.kado.net/news/photo/202205/1126349_551566_0650.jpg')
#                 st.markdown(
#                     """
#                 <video controls width = 450 autoplay="true" muted="true" loop="true">
#                 <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/paramedics.mp4" type="video/mp4" />
#                 </video>
#                 """,
#                     unsafe_allow_html=True,
#                 )
#                 st.markdown(
#                     """
#                 <video controls width = 450 autoplay="true" muted="true" loop="true">
#                 <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/Namsan.mp4" type="video/mp4" />
#                 </video>
#                 """,
#                     unsafe_allow_html=True,
#                 )

#         #         with col3:
#         #             st.subheader("서울시 내 소방서 표시")
#         #             df = pd.DataFrame(
#         #     np.random.randn(25, 2) / [40, 50] + [37.56, 127.00],
#         #     columns=['lat', 'lon'])

#         #             st.map(df)
#         def 구조():
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.subheader("구조 상황 발생 지역")
#                 df = pd.DataFrame(
#                     np.random.randn(1, 2) / [40, 50] + [37.5642, 127.0016],
#                     columns=["lat", "lon"],
#                 )

#                 st.map(df)
#             with col2:
#                 st.subheader("실시간 현장 CCTV")
#                 #             st.image('https://pip-thumb.zumst.com/api/v1/swyze_VC002_77445815_content.jpeg?w=880&h=495')
#                 st.markdown(
#                     """
#                     <video controls width = 450 autoplay="true" muted="true" loop="true">
#                     <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/Flood.mp4" type="video/mp4" />
#                     </video>
#                     """,
#                     unsafe_allow_html=True,
#                 )

#         #         with col3:
#         #             st.subheader("서울시 내 소방서 표시")
#         #             df = pd.DataFrame(
#         #     np.random.randn(25, 2) / [40, 50] + [37.56, 127.00],
#         #     columns=['lat', 'lon'])

#         #             st.map(df)
#         def 시위():
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.subheader("시위 상황 발생 지역")
#                 df = pd.DataFrame(
#                     np.random.randn(1, 2) / [40, 50] + [37.5642, 127.0016],
#                     columns=["lat", "lon"],
#                 )

#                 st.map(df)
#                 with col2:
#                     st.subheader("🚨🚨실시간 현장 CCTV🚨🚨")
#                     st.markdown(
#                         """
#                     <video controls width = 450 autoplay="true" muted="true" loop="true">
#                     <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/OpenCV%20People%20Counting%20Demo%20%232-3iiodzoG80A.mp4" type="video/mp4"/>
#                     </video>
#                     """,
#                         unsafe_allow_html=True,
#                     )
#                     st.markdown(
#                         """
#                     <video controls width = 450 autoplay="true" muted="true" loop="true">
#                     <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/candlelight vigil.mp4" type="video/mp4" />
#                     </video>
#                     """,
#                         unsafe_allow_html=True,
#                     )
#                     st.markdown(
#                         """
#                     <video controls width = 450 autoplay="true" muted="true" loop="true">
#                     <source src="https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/X-mas.mp4" type="video/mp4" />
#                     </video>
#                     """,
#                         unsafe_allow_html=True,
#                     )

#         #         with col3:
#         #             st.subheader("서울시 내 소방서 표시")
#         #             df = pd.DataFrame(
#         #     np.random.randn(25, 2) / [40, 50] + [37.56, 127.00],
#         #     columns=['lat', 'lon'])

#         #             st.map(df)
#         page_names_to_funcs = {
#             "사고유형을선택해주세요": 사고유형을선택해주세요,
#             "화재": 화재,
#             "구급": 구급,
#             "구조": 구조,
#             "시위": 시위,
#         }
#         selected_page = st.sidebar.selectbox(
#             "아래 재난 유형을 선택하세요", page_names_to_funcs.keys()
#         )
#         page_names_to_funcs[selected_page]()
#     elif add_selectbox == "범죄":
#         st.sidebar.title("-----112로 이관하겠습니다-----서울 경찰청 종합상황실 : 02-6150-1155")
#         st.title("112 종합상황실")
#         st.image(
#             "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F277323345630656E1A"
#         )
#     else:
#         st.title("정부 민원 안내 콜센터")
#         st.image("http://www.outsourcing.co.kr/news/photo/202211/95401_34878_5915.jpg")
#         st.sidebar.title("----100으로 이관하겠습니다----정부합동민원센터 : 110")
#     with st.sidebar:
#         st.markdown(
#             """<style>@import url(https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@800&family=Noto+Sans+KR:wght@500&display=swap);@font-face{font-family:&quot}[class*=css],body{font-family:'Noto Sans KR'}</style>""",
#             unsafe_allow_html=True,
#         )
