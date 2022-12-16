import streamlit as st
import pandas as pd
import time
import numpy as np
import streamlit as st
import pydeck as pdk
from urllib.error import URLError
import base64
import altair as alt



add_selectbox = st.sidebar.selectbox('소방서를 선택하세요',
                                 ('마포소방서','관악소방서',
'동작소방서'
,'양천소방서'
,'강서소방서'
,'노원소방서'
,'강동소방서'
,'영등포소방서'
,'송파소방서'
,'성북소방서'
,'종로소방서'
,'서초소방서'
,'강남소방서'
,'중부소방서'
,'동대문소방서'
,'도봉소방서'
,'용산소방서'
,'광진소방서'
,'서대문소방서'
,'은평소방서'
,'중랑소방서'
,'강북소방서'
,'성북소방서'))
if add_selectbox == '마포소방서':
    
    col1,col2,col3=st.columns(3)
    with col1:
        np.random.seed(1)

        source = pd.DataFrame({
    'x': np.arange(100),
    'A': np.random.randn(100).cumsum(),
    'B': np.random.randn(100).cumsum(),
    'C': np.random.randn(100).cumsum(),
})

        base = alt.Chart(source).mark_circle(opacity=0.5).transform_fold(
    fold=['A', 'B', 'C'],
    as_=['category', 'y']
).encode(
    alt.X('x:Q'),
    alt.Y('y:Q'),
    alt.Color('category:N')
)

        base + base.transform_loess('x', 'y', groupby=['category']).mark_line(size=4)


        source = pd.DataFrame(
    {"category": ["a", "b", "c", "d", "e", "f"], "value": [4, 6, 10, 3, 7, 8]}
)

        base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
).properties(width='container')

        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")

        pie + text
    with col2:
        st.video('paramedics.mp4')
        st.video('candlelight vigil.mp4')
        
        
#     with col3:
        
    with col3:
        source = pd.DataFrame({'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]})
        bar = alt.Chart(source).mark_bar().encode(x='a',y='b').properties(width='container')
        source = pd.DataFrame({"category": ["a", "b", "c", "d", "e", "f"], "value": [4, 6, 10, 3, 7, 8]})
        base = alt.Chart(source).encode(theta=alt.Theta("value:Q", stack=True).properties(width='container'), color=alt.Color("category:N", legend=None))
        pie = base.mark_arc(outerRadius=120)
        text = base.mark_text(radius=140, size=20).encode(text="category:N")
        pie + text
        bar
        
        
#         source = pd.DataFrame(
#     [
#         {"team": "Germany", "matchday": 1, "point": 0, "diff": -1},
#         {"team": "Germany", "matchday": 2, "point": 3, "diff": 0},
#         {"team": "Germany", "matchday": 3, "point": 3, "diff": -2},
#         {"team": "Mexico", "matchday": 1, "point": 3, "diff": 1},
#         {"team": "Mexico", "matchday": 2, "point": 6, "diff": 2},
#         {"team": "Mexico", "matchday": 3, "point": 6, "diff": -1},
#         {"team": "South Korea", "matchday": 1, "point": 0, "diff": -1},
#         {"team": "South Korea", "matchday": 2, "point": 0, "diff": -2},
#         {"team": "South Korea", "matchday": 3, "point": 3, "diff": 0},
#         {"team": "Sweden", "matchday": 1, "point": 3, "diff": 1},
#         {"team": "Sweden", "matchday": 2, "point": 3, "diff": 0},
#         {"team": "Sweden", "matchday": 3, "point": 6, "diff": 3},
#     ]
# )

#         color_scale = alt.Scale(
#     domain=["Germany", "Mexico", "South Korea", "Sweden"],
#     range=["#000000", "#127153", "#C91A3C", "#0C71AB"],
# )

#         alt.Chart(source).mark_line().encode(
#     x="matchday:O", y="rank:O", color=alt.Color("team:N", scale=color_scale)
# ).transform_window(
#         rank="rank()",
#         sort=[
#         alt.SortField("point", order="descending"),
#         alt.SortField("diff", order="descending"),
#     ],
#         groupby=["matchday"],
# ).properties(title="World Cup 2018: Group F Rankings")
