import streamlit as st
import pandas as pd

st.set_page_config(page_title="답정너AI 로그 대시보드", layout="wide")
st.title("📊 답정너AI 로그 대시보드")

file_path = "chat_log.csv"

try:
    df = pd.read_csv(file_path)
    st.dataframe(df)

    st.download_button(
        label="CSV 다운로드",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="chat_log.csv",
        mime="text/csv"
    )
except FileNotFoundError:
    st.warning("아직 chat_log.csv 파일이 생성되지 않았습니다.")
