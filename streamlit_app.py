# Streamlitライブラリをインポート
import streamlit as st
import random

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('おみくじアプリ')

omikuji=["大吉","中吉","小吉","吉","凶","大凶","末吉"]

if st.button("おみくじをひく"):
    a=random.choice(omikuji)
    print(a)
