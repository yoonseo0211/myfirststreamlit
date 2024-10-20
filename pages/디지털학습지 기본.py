import streamlit as st
import random

# 페이지 제목
st.title("디지털 학습지")

# 1. 캐릭터 맞추기 퀴즈# 세로로 레이아웃을 분할하기
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://media.tenor.com/CV9KmvIEY_gAAAAM/sad-crying.gif", caption="누구일까요?")
    answer1 = st.radio("첫 번째 캐릭터 이름을 선택하세요", ["Joy", "Sadness", "Anger"], key="answer1")
    if st.button("제출 1", key="btn1"):
        if answer1 == "Sadness":
            st.success("정답입니다! 슬픔이에요!(ㅠㅠ) 인사이드 아웃을 아주 잘 봤군요!")
        else:
            st.error("틀렸습니다. 다시 시도하세요.")

with col2:
    st.image("https://media.tenor.com/AFbAHAuv680AAAAM/bing-bong.gif", caption="누구일까요?")
    answer2 = st.radio("두 번째 캐릭터 이름을 선택하세요", ["Bing Bong", "Elephant", "Fear"], key="answer2")
    if st.button("제출 2", key="btn2"):
        if answer2.strip().lower() == "bing bong":
            st.success("정답입니다!")
        else:
            st.error("틀렸습니다. 다시 시도하세요.")

with col3:
    st.image("https://media0.giphy.com/media/Ta2eHM043vhVS/giphy.gif?cid=6c09b9527hc5vaugbt1zqey80qnqzc0pcohdytupicolempm&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g", caption="누구일까요?")
    answer3 = st.radio("세 번째 캐릭터 이름을 선택하세요", ["Joy", "Sadness", "Anger"], key="answer3")
    if st.button("제출 3", key="btn3"):
        if answer3.strip().lower() == "joy":
            st.success("정답입니다!")
        else:
            st.error("틀렸습니다. 다시 시도하세요.")

# 2. 탭 레이아웃 (수학 LaTeX, 유튜브, 데스모스 계산기)
st.subheader("흥미로운 콘텐츠 탭")

tab1, tab2 = st.tabs(["애니메이션으로 보는 수학", "애니메이션으로 보는 물리학"])


with tab1:
    st.write("애니메이션으로 보는 시리즈(By Alan Becker) : 수학 시리즈")
    st.video("https://www.youtube.com/watch?v=B1J6Ou4q8vE&list=PL7z8SQeih5Af9B2DshZul4KvTLI74NkUQ&index=1")
    st.text_input("영상을 본 후 소감을 간단히 작성해주세요.(수학)")
with tab2:
    st.write("애니메이션으로 보는 시리즈(By Alan Becker) : 물리학 시리즈")
    st.video("https://youtu.be/ErMSHiQRnc8?list=PL7z8SQeih5Af9B2DshZul4KvTLI74NkUQ")
    st.text_input("영상을 본 후 소감을 간단히 작성해주세요.(물리학)")

with st.expander("긴 글 숨기기"):
    st.write("""Streamlit과 파이썬은 데이터를 다루는 데 매우 유용한 도구입니다. 특히, Streamlit은 파이썬 기반의 웹 애플리케이션을 쉽게 개발할 수 있게 해주는 라이브러리로, 데이터 과학자나 분석가들이 복잡한 웹 개발 과정을 거치지 않고도 자신의 분석 결과를 공유하거나 시각화할 수 있게 해줍니다.

                파이썬은 이미 다양한 데이터 처리 라이브러리(예: pandas, NumPy, matplotlib, seaborn)를 통해 강력한 데이터 분석 도구로 자리 잡고 있습니다. 하지만, 분석 결과를 웹에서 공유하고 인터랙티브한 시각화를 제공하는 것은 또 다른 차원의 도전입니다. 많은 분석가들이 자신이 도출한 인사이트를 팀원이나 이해관계자들에게 쉽게 설명하고자 할 때, Streamlit이 그 해결책을 제시합니다.

                Streamlit의 장점 중 하나는 간결함입니다. 코드 몇 줄만으로도 복잡한 대시보드나 웹 애플리케이션을 만들 수 있습니다. 웹 개발에 대한 전문 지식이 없어도, 파이썬 스크립트에 Streamlit의 간단한 함수들을 추가하면 실행 가능한 웹 애플리케이션이 완성됩니다. 이를 통해 사용자는 데이터를 실시간으로 조작하고 다양한 시나리오를 테스트할 수 있습니다.

                예를 들어, pandas를 사용해 데이터를 처리한 후, Streamlit의 `st.write()` 함수로 데이터 프레임을 출력하거나, `st.line_chart()` 함수로 데이터의 트렌드를 손쉽게 시각화할 수 있습니다. 또한, Streamlit은 구글 시트와 같은 외부 데이터 소스와도 쉽게 연동할 수 있어, 실시간으로 데이터를 업데이트하고, 시각화 결과를 동적으로 변화시키는 것이 가능합니다.

                Streamlit은 기본적으로 서버에서 실행되며, 사용자는 웹 브라우저를 통해 접근할 수 있습니다. 이를 통해 팀원들과 분석 결과를 빠르게 공유하고, 더 나아가 인사이트를 바탕으로 협업할 수 있는 환경을 제공합니다. 예를 들어, 실시간 데이터 분석 웹앱을 만들어, 사용자로부터 입력을 받아 그에 따른 결과를 즉시 피드백하는 형태로 구현할 수 있습니다. 이는 기존에 수동으로 데이터를 확인하고 보고서를 작성하는 시간과 노력을 크게 절감시킵니다.

                또한, Streamlit은 매우 유연하여 사용자 맞춤형 인터페이스를 쉽게 제작할 수 있습니다. 슬라이더, 입력 박스, 버튼 등 다양한 위젯을 제공해 사용자가 직접 파라미터를 조정하면서 데이터를 실시간으로 분석할 수 있습니다. 이러한 기능들은 특히 교육 현장이나 연구에서 데이터 기반의 의사결정을 도울 때 매우 유용합니다.

                파이썬과 Streamlit을 결합하면 복잡한 데이터 분석 작업을 단순화하고, 그 결과를 인터랙티브하게 표현할 수 있는 강력한 도구가 됩니다. 이는 비즈니스 인사이트를 도출하는 데에도, 교육 및 연구 목적으로 데이터를 탐구하는 데에도 폭넓게 활용될 수 있습니다. 직관적이고 사용하기 쉬운 인터페이스 덕분에 프로그래밍 초보자들도 쉽게 접근할 수 있으며, 고급 사용자들에게는 커스터마이징할 수 있는 무한한 가능성을 제공합니다.

                결론적으로, 파이썬과 Streamlit의 조합은 데이터를 분석하고 시각화하는 강력한 도구로서, 데이터의 가치를 극대화하고, 그 결과를 명확하고 쉽게 공유할 수 있는 방법을 제공합니다.""")