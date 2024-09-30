import streamlit as st
import random

# 세션 상태 초기화 (문제와 정답)
if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(1, 100)
if 'num2' not in st.session_state:
    st.session_state.num2 = random.randint(1, 100)
if 'answer' not in st.session_state:
    st.session_state.answer = st.session_state.num1 + st.session_state.num2
if 'new_num1' not in st.session_state:
    st.session_state.new_num1 = None
if 'new_num2' not in st.session_state:
    st.session_state.new_answer = None

# 페이지 제목
st.title('수학 문제 풀이')

# 간단한 설명
st.write('주어진 수학 문제를 풀고, 답을 입력하세요. 제출하면 정답 여부와 피드백을 제공합니다.')

# 기존 문제 출력
st.write(f"문제: {st.session_state.num1} + {st.session_state.num2} = ?")

# 학생의 답 입력
student_answer = st.number_input('답을 입력하세요:', min_value=0, max_value=200, step=1, key='student_answer')

# 기존 문제 답 제출 버튼
if st.button('제출'):
    if student_answer == st.session_state.answer:
        st.success(f"정답입니다! 답: {st.session_state.answer}")
        st.balloons()
    else:
        st.errsor(f"틀렸습니다. 다시 시도해보세요. 정답은 {st.session_state.answer}입니다.")

# 새로운 문제 생성 버튼
if st.button('새로운 문제'):
    # 새로운 문제와 정답 생성
    st.sesssion_state.new_num1 = random.randint(1, 100)

# 새로운 문제가 있을 때만 출력
if st.session_state.new_num1 is not None and st.session_state.new_num2 is not None:
    st.write(f"새로운 문제: {st.session_state.new_num1} + {st.session_state.new_num2} = ?")

    # 새로운 문제에 대한 답 입력
    new_studdent_answer = st.number_input('새 문제의 답을 입력하세요:', min_value=0, max_value=200, step=1, key='new_student_answer')

    # 새로운 문제 답 제출 버튼
    if st.button('새 문제 제출'):
        if new_student_answer == st.session_state.new_answer:
            st.success(f"정답입니다! 답: {st.session_state.new_answer}")
            st.balloons()
        else:
            st.error(f"틀렸습니다. 다시 시도해보세요. 정답은 {st.session_state.new_answer}입니다.")
