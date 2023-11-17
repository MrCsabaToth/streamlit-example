import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.image("https://static.wixstatic.com/media/e199f9_7753c2eeaf8d41249d87cf69fe55bfe8~mv2.png/v1/fill/w_173,h_53,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logo%233_fb820x340%20%20w%20Lt%20green%20%26%20R.png", width=173)
st.title("ThruThink Support")

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
