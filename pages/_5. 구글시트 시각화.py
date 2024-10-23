import streamlit as st
from streamlit_gsheets import GSheetsConnection
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import koreanize_matplotlib

st.title("구글시트와 연결하는 앱 만들기")

# st.dataframe(data)
if st.button("데이터 새로고침하기"):
    st.cache_data.clear()

url = "https://docs.google.com/spreadsheets/d/1MDhQpSf110rcR3bSjZ8yEBoMByLZ6Yxs-hQRsC6to1g/edit?gid=1498412415#gid=1498412415"

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url, usecols=[0, 1, 2])

# 데이터 시각화
st.subheader("흥미도와 이해도 차트")

st.write(df.head())

# Seaborn 바 차트
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df, x = 'class', hue = 'interest', ax=ax)
# Streamlit에 차트 표시
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df, x = 'class', hue = 'understand', ax=ax)
# Streamlit에 차트 표시
st.pyplot(fig)