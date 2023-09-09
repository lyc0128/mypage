import streamlit as st
from PIL import Image

st.set_page_config(
    page_title = '예찬')
menu = st.selectbox('MENU',['자기소개','학교소개','동아리소개','관심분야'])

if menu == '자기소개':
    st.subheader('자기소개:')
    st.subheader('이름: 이예찬')
    st.subheader('특징: 호기심이 많다.')
    st.subheader('MBTI: INTJ')
elif menu == '학교소개':
    st.subheader('학교소개:')
    image = Image.open('다운로드2.jfif')
    st.image(image, width=1000)
    st.subheader('1.운동장이 크다.')
    st.subheader('2.시설이 좋다.')
    st.subheader('3.(우리)집이랑 가깝다.')
elif menu == '동아리소개':
    st.subheader('동아리소개:')
    st.subheader('1.이름: 소프트웨어 메이킹')
    st.subheader('2. 선생님이 마호돌쌤이다. 그래서 편하다.')
else:
    st.subheader('관심분야')
    st.subheader('1. 축구보기')
    image = Image.open('cr.jpg')
    st.image(image, width=1000)
    st.subheader('2. 만화(웹툰)')
    image = Image.open('B.jpg')
    st.image(image, width=1000)
   





