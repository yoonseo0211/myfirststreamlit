import streamlit as st

st.title("👋🏻 윤서의 페이지입니다")
st.subheader("윤서를 소개합니다.")
st.write("아래 버튼을 눌러보아요.")

st.link_button("소개 바로가기!", "https://www.naver.com/")

# st.success("초록색 창")
# st.error("빨간색 창")
st.info("파란색 창")
# st.warning("노란색 창") # ctrl+/ : 주석처리

st.image("https://media.giphy.com/media/iCh8iLOteYr0Q/giphy.gif?cid=ecf05e47ea6yhl7rvq347icv5e2rs6svqnq52llas0n84aix&ep=v1_gifs_related&rid=giphy.gif&ct=g", caption="윤서")