import streamlit as st
import pyodbc

# DB접속
# st.cache_resource를 사용하여 한 번만 실행합니다.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )
conn = init_connection()


# 쿼리 실행(1)
# 쿼리가 변경되거나 10분 후에만 다시 실행하기 위해 st.cache_data를 사용합니다.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
rows = run_query("SELECT TOP(10) ACCNBR,ACCDES  FROM ACCDEF a ;")

# 쿼리 값 출력(1)
for row in rows:
    st.write(f"{row[0]} {row[1]}")
