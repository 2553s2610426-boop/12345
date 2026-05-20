# app.py

import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# 제목
st.title("🚀 나의 첫 Streamlit 웹앱")

st.write("스트림릿으로 만든 간단한 웹앱 예제입니다.")

# 사이드바
st.sidebar.header("설정")

name = st.sidebar.text_input("이름 입력", "Guest")

number = st.sidebar.slider(
    "데이터 개수 선택",
    min_value=10,
    max_value=100,
    value=30
)

# 메인 화면
st.subheader(f"안녕하세요, {name}님 👋")

# 랜덤 데이터 생성
data = pd.DataFrame({
    "x": np.arange(number),
    "y": np.random.randn(number).cumsum()
})

# 데이터 표시
st.write("### 생성된 데이터")
st.dataframe(data)

# 차트 표시
st.write("### 차트")
st.line_chart(data.set_index("x"))

# 버튼
if st.button("메시지 출력"):
    st.success("버튼이 클릭되었습니다!")

# 컬럼 레이아웃
col1, col2 = st.columns(2)

with col1:
    st.metric("오늘 방문자", "1,024", "+12%")

with col2:
    st.metric("매출", "$8,530", "+5.4%")

# 파일 업로드
uploaded_file = st.file_uploader(
    "CSV 파일 업로드",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### 업로드한 데이터")
    st.dataframe(df)

    st.write("### 데이터 통계")
    st.write(df.describe())

# 푸터
st.markdown("---")
st.caption("Made with Streamlit ❤️")
