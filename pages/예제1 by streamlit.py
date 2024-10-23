import streamlit as st
import random

# 게임 시작할 때만 목표 숫자 생성
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0

st.title('숫자 맞추기 게임')
st.write('1부터 100 사이의 숫자를 맞춰보세요!')

# 사용자의 입력값
guess = st.number_input('숫자를 입력하세요', min_value=1, max_value=100, step=1)

# 버튼 클릭 시 입력값을 확인
if st.button('확인'):
    st.session_state.attempts += 1
    if guess < st.session_state.target:
        st.write(f"{guess}보다 큰 숫자입니다. 다시 시도해보세요!")
    elif guess > st.session_state.target:
        st.write(f"{guess}보다 작은 숫자입니다. 다시 시도해보세요!")
    else:
        st.write(f"축하합니다! {guess}가 정답입니다!")
        st.write(f"총 {st.session_state.attempts}번 시도하셨습니다.")
        # 게임 재시작 버튼
        if st.button('다시 시작하기'):
            st.session_state.target = random.randint(1, 100)
            st.session_state.attempts = 0
            st.experimental_rerun()

