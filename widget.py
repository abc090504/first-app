import streamlit as st
import pandas as pd
import random
import datetime
df = pd.read_csv("movies.csv")

st.divider()
st.title('버튼예제')
st.divider()
#1. 데이터 조회
if st.button("데이터 조회"):
    st.dataframe(df)

#2. 랜덤 영화 추천
if st.button("랜덤 추천"):
    st.write(df.sample(1))

if st.button("최저 평점 영화"):
    st.write(df.loc[df['rating'].idxmin()])