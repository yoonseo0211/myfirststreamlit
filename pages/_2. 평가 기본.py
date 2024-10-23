import streamlit as st

# 페이지 제목 설정
st.title("형성평가 퀴즈")
st.subheader("아래 질문에 답해주세요!")

# 정답 확인 함수
def check_answers(answers):
    feedback = []
    correct_answers = ["파이썬", "리눅스", "머신러닝"]
    
    for i, answer in enumerate(answers):
        if answer == correct_answers[i]:
            feedback.append(f"문제 {i+1}: 정답입니다! 잘 하셨어요 🎉")
        else:
            feedback.append(f"문제 {i+1}: 오답입니다. 다시 시도해보세요 😅")
    
    return feedback

# 문제와 선택지 설정
questions = [
    {"question": "1. 파이썬의 대표적인 사용 분야는?", 
     "options": ["프론트엔드 개발", "백엔드 개발", "파이썬"]},
    {"question": "2. 오픈 소스 운영 체제는?", 
     "options": ["윈도우", "리눅스", "맥OS"]},
    {"question": "3. AI에서 데이터를 학습시키는 기법은?", 
     "options": ["머신러닝", "클라우드 컴퓨팅", "데이터베이스"]},
]

# 사용자 답변을 저장할 리스트
user_answers = []

# 퀴즈 질문 생성
for i, q in enumerate(questions):
    st.write(q["question"])
    answer = st.radio(f"문제 {i+1}", q["options"], key=f"q{i+1}")
    user_answers.append(answer)

# "제출" 버튼
if st.button("제출하기"):
    feedback = check_answers(user_answers)
    for msg in feedback:
        st.write(msg)
    
    # 정답 개수 표시
    correct_count = sum([1 for i, answer in enumerate(user_answers) if answer == ["파이썬", "리눅스", "머신러닝"][i]])
    st.write(f"총 {correct_count}개의 문제를 맞추셨습니다.")

# 간단한 스타일링 (배경색, 텍스트 색상 등)
st.markdown("""
    <style>
    body {
        background-color: #f0f0f0;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
    }
    .stRadio > label {
        font-size: 18px;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)
