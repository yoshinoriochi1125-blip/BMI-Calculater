st.write("使い方：身長と体重を入れてボタンを押すだけでBMIがわかる")

import streamlit as st

st.set_page_config(page_title="BMI計算アプリ", page_icon="⚖️")
st.title("BMI計算アプリ")

st.write("身長(cm)と体重(kg)を入力して、BMIを計算します。")

col1, col2 = st.columns(2)
with col1:
    height = st.number_input("身長 (cm)", min_value=50.0, max_value=250.0, step=0.1)
with col2:
    weight = st.number_input("体重 (kg)", min_value=10.0, max_value=300.0, step=0.1)

if st.button("BMIを計算"):
    if height > 0:
        bmi = weight / ((height / 100) ** 2)

        if bmi < 18.5:
            st.warning(f"BMI: {bmi:.2f}（低体重）")
        elif bmi < 25:
            st.success(f"BMI: {bmi:.2f}（普通体重）")
        else:
            st.error(f"BMI: {bmi:.2f}（肥満）")
    else:
        st.error("身長を正しく入力してください。")

import pandas as pd

data = pd.DataFrame({"カテゴリ": ["低体重", "普通体重", "肥満"], "BMI範囲": [18.5, 25, 30]})
st.bar_chart(data.set_index("カテゴリ"))


