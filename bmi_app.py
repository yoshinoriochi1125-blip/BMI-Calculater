# --- 必要なライブラリを読み込み ---
import streamlit as st
import pandas as pd

# --- ページ設定 ---
st.set_page_config(page_title="BMI計算アプリ", page_icon="⚖️", layout="centered")

# --- タイトルと説明 ---
st.title("BMI計算アプリ")
st.write("使い方：身長(cm)と体重(kg)を入力して「BMIを計算」を押してください。")

# --- 入力UI ---
col1, col2 = st.columns(2)
with col1:
    height = st.number_input("身長 (cm)", min_value=50.0, max_value=250.0, step=0.1, value=170.0)
with col2:
    weight = st.number_input("体重 (kg)", min_value=10.0, max_value=300.0, step=0.1, value=60.0)

# --- 計算ボタン ---
if st.button("BMIを計算"):
    if height > 0:
        bmi = weight / ((height / 100) ** 2)

        # 結果の色分け表示
        if bmi < 18.5:
            st.warning(f"BMI: {bmi:.2f}（低体重）")
        elif bmi < 25:
            st.success(f"BMI: {bmi:.2f}（普通体重）")
        else:
            st.error(f"BMI: {bmi:.2f}（肥満）")

        # 参考グラフ
        st.subheader("BMI分類の参考グラフ")
        data = pd.DataFrame({
            "カテゴリ": ["低体重", "普通体重", "肥満"],
            "BMI範囲": [18.5, 25, 30]
        })
        st.bar_chart(data.set_index("カテゴリ"))
    else:
        st.error("身長を正しく入力してください。")
