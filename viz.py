import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('시각화 예제')

option1 = None
option2 = None
# option이 with st.sidebar 구문 안에 들어가 있기 때문에
# 초기에 에러가 나올 수 있어서 초기값을 None으로 잡아주는 것

# sidebar을 추가하는 경우 아래와 같이 st.sidebar 조건 넣어줌
with st.sidebar:
    file = st.file_uploader('파일 업로드', type=['csv'])

    if file:
        df = pd.read_csv(file)
        st.dataframe(df)
        st.subheader('기준 선택')

        option1 = st.selectbox('x축', tuple(df.columns))
        option2 = st.selectbox('y축', tuple(df.columns))

if option1 and option2:
    fig, ax = plt.subplots(1, 1)
    # <예시> (2, 2)로 하면 총 4개까지 그래프 그릴 수 있음 
    fig.set_size_inches(10, 6)
    sns.barplot(x=option1, y=option2, data=df, ax=ax)
    st.pyplot(fig)