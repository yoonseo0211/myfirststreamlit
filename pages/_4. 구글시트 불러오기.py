import streamlit as st
from streamlit_gsheets import GSheetsConnection
import numpy as np

st.title("구글시트와 연결하는 앱 만들기")
url = "https://docs.google.com/spreadsheets/d/1MDhQpSf110rcR3bSjZ8yEBoMByLZ6Yxs-hQRsC6to1g/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url, usecols=[0, 1, 2])


# 맞은 문제 개수를 저장할 변수
correct_count = 0

# st.dataframe(data)
if st.button("데이터 새로고침하기"):
    st.cache_data.clear()
for index, row in data.iterrows():
    st.markdown("### ✏️문제 "+str(index+1)+". "+str(row["문제"]))
    user_answer = st.text_input("정답을 입력하세요.",key=index)
    if user_answer == "":
        continue
    elif user_answer == row["정답"]:
        st.success("맞았습니다!")
        correct_count += 1  # 맞은 문제 수 증가

    else:
        st.warning("다시 풀어보세요.")



# 최종적으로 맞은 문제 개수 출력
if st.button("결과 보기"):
    st.error(f"# 점수: {np.round(100*correct_count/len(data),1)}점")
    st.write(f"### 전체 {len(data)}개의 문제 중에서 {correct_count}개의 문제를 맞췄습니다!")