import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import openpyxl

# Streamlit 페이지 설정
st.set_page_config(page_title="파일 업로드 및 등급 계산", layout="wide")
st.title("파일 업로드 및 등급 계산")

# Seaborn 색상 팔레트 설정
sns.set_palette("flare")

# 파일 업로드 기능
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type="xlsx")

if uploaded_file is not None:
    # 1. 데이터 전처리
    def preprocess_data(df):
        df = df.iloc[7:37, [1, 2, 3, 4, 6, 7, 9, 10, 12, 15, 16]]
        df.columns = ['번호', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        df = df.apply(pd.to_numeric, errors='coerce')
        df = df.melt(id_vars='번호', value_name='점수', var_name='반')
        df = df.dropna()
        return df

    # 2. 등급 부여 함수
    def assign_grade(df_sorted, thresholds):
        total_students = len(df_sorted)
        df_sorted['누적 비율'] = (df_sorted.index + 1) / total_students
        def grade_threshold(row, thresholds):
            for i, threshold in enumerate(thresholds):
                if row['누적 비율'] <= threshold:
                    return i + 1
            return 9  # 9등급까지 부여
        df_sorted['등급'] = df_sorted.apply(grade_threshold, axis=1, thresholds=thresholds)
        df_sorted['등급'] = df_sorted['등급'].astype(str)
        return df_sorted

    # 3. 등급 컷 계산 함수
    def calculate_grade_cutoffs(df_sorted):
        grade_cutoffs = []
        previous_value = None
        for row in range(len(df_sorted)):
            current_value = df_sorted.iloc[row, 4]  # 등급
            if previous_value is not None and current_value != previous_value:
                grade_cutoffs.append({
                    '등급': f"{df_sorted.iloc[row-1, 4]}등급",
                    '컷 점수': df_sorted.iloc[row-1, 2]  # 점수
                })
            previous_value = current_value
        return pd.DataFrame(grade_cutoffs)

    # 데이터 불러오기 및 전처리
    df = pd.read_excel(uploaded_file)
    df = preprocess_data(df)

    # 총 학생 수 계산
    total_students = len(df)
    thresholds = [0.04, 0.11, 0.23, 0.40, 0.60, 0.77, 0.89, 0.96, 1.00]

    # 점수 순으로 정렬 및 등급 부여
    df_sorted = df.sort_values(by='점수', ascending=False).reset_index(drop=True)
    df_sorted = assign_grade(df_sorted, thresholds)
    df_sorted = df_sorted[['반', '번호', '점수', '누적 비율', '등급']]

    # 컬럼 나누기
    col1, col2 = st.columns(2)

    with col1:
        st.write("상위 20명 결과")
        st.write(df_sorted.head(20))

    with col2:
        # 등급 컷 계산 및 표시
        cutoffs_df = calculate_grade_cutoffs(df_sorted)
        if not cutoffs_df.empty:
            st.subheader("등급 컷 정보")
            st.dataframe(cutoffs_df)

        # 평균 점수 계산 및 출력
        mean_score = df_sorted['점수'].mean()
        st.write(f"전체 학생의 평균 점수: {mean_score:.2f}점")

    # 4. 시각화
    # 4.1 점수 분포 히스토그램
    st.subheader("점수 분포")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(x='점수', data=df_sorted, ax=ax, binwidth=10, binrange=[0, 100])
    ax.set_title('Distribution of Scores', fontsize=16)
    st.pyplot(fig)

    # 반별 점수 상자 그림 (Boxplot)
    st.subheader("반별 점수 분포 (상자 그림)")
    fig, ax = plt.subplots(figsize=(10, 6))

    # 반을 숫자로 변환 (1부터 10까지 순서대로 나오게끔)
    df_sorted['반'] = pd.Categorical(df_sorted['반'], categories=[str(i) for i in range(1, 11)], ordered=True)

    # 상자 그림 생성
    sns.boxplot(y='점수', x='반', data=df_sorted, ax=ax, dodge=True, width=0.7)

    # Y축에 1부터 10까지 설정
    ax.set_xticks(range(10))  # 0부터 9까지 인덱스로 설정
    ax.set_xticklabels([str(i) for i in range(1, 11)])  # 1부터 10까지 레이블로 표시

    # 제목 설정
    ax.set_title('Score distribution by class', fontsize=16)

    # Streamlit에 차트 표시
    st.pyplot(fig)