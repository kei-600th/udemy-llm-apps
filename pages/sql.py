import streamlit as st

st.title("Text-to-SQL")

question = st.text_input(label="質問")

if question:
    answer = "商品データは100件です。"
    sql = "select count(*) from product"
    st.info(sql)
    st.success(answer)
