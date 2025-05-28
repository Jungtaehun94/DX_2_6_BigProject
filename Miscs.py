import numpy as np
import streamlit as st
# @st.experimental_singleton
def find_close_points(df_input, gu, n=3):
    df = df_input.copy()
    row = df.loc[df["출동소방서"] == gu].reset_index()
    df["distance"] = np.sqrt(
        (df["lng"] - row["lng"][0]) ** 2 + (df["lat"] - row["lat"][0]) ** 2
    )
    df["lng_dest"] = row["lng"][0]
    df["lat_dest"] = row["lat"][0]
    # Sort the rows by distance
    df.sort_values(by="distance", inplace=True, ignore_index=True)
    df["distance"] = df["distance"].astype(int)
    df[["r", "g", "b"]] = [192, 64, 64]
    df.loc[0, ["r", "g", "b"]] = [0, 16 * 8, 0]
    supp = df.loc[0, ["deficiency"]][0]
    supp = int(supp)
    from calculate_abc import calculate_abc
    est = int(df.loc[0, ["EstReq"]][0])
    df.loc[0, ["차출"]] = 0
    supp_list = list(calculate_abc(df.loc[1:3, ["dpt"]].reset_index(), supp))
    df.loc[1:3, ["차출"]] = supp_list
    df["소방공무원_22"] = df["소방공무원_22"].astype(str)
    df.loc[0:0, ["소방공무원_22"]] = f'Est: {est}\n' + df["소방공무원_22"] + f"({int(supp)})" 
    df["차출"] = df["차출"].apply(lambda x: str(int(x)) if np.isfinite(x) else "")
    df.loc[1:, ["소방공무원_22"]] = df["소방공무원_22"] + "(" + df["차출"] + ")"

    assign_icons(
        df,
        "https://img.icons8.com/plasticine/100/000000/marker.png",
    )
    df.loc[0, ["icon_data"]] = [
        URL_to_Icon_Data("https://github.com/Jungtaehun94/streramlit_temp_app/raw/main/100_green_marker.png")
    ]
    # Select the 3 closest points
    closest_points = df.head(n + 1).copy()
    return closest_points, supp_list

def URL_to_Icon_Data(image_url):
    import base64
    import requests

    response = requests.get(image_url)
    image_content = response.content
    encoded_image = base64.b64encode(image_content).decode("ascii")
    icon_data = {
        "url": r"data:image/png;base64," + str(encoded_image),
        "width": 128,
        "height": 128,
        "anchorY": 128,
    }
    return icon_data


def assign_icons(df, icon_url):
    import base64
    import requests

    image_url = icon_url
    response = requests.get(image_url)
    if response.status_code == 200:
        image_content = response.content
        encoded_image = base64.b64encode(image_content).decode("ascii")
    else:
        print("Failed to download image")
    icon_data = {
        "url": r"data:image/png;base64," + str(encoded_image),
        "width": 128,
        "height": 128,
        "anchorY": 128,
    }
    df["icon_data"] = None
    for i in df.index:
        df["icon_data"][i] = icon_data
    
