import streamlit as st

tab1, tab2 = st.tabs(["과학용 계산기", "수학 그래프 계산기"])


with tab1:
    st.components.v1.iframe("https://www.desmos.com/scientific", height=500)
with tab2:
    st.subheader("다음 함수식을 그래핑 계산기에 나타내보세요.")
    st.info("❓x의 제곱은 x^2 로 입력할 수 있어요.")
    st.latex("y=2x-1")
    st.latex("y=x^2+1")
    st.text_input("두 그래프의 모양은 어떻게 다른가요?")
    st.components.v1.iframe("https://www.desmos.com/calculator", height=500)

