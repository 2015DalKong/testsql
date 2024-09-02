"""
Connects to a SQL database using pymssql
"""

import streamlit as st
import pyodbc


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

cursor = conn.cursor()

# SQL 쿼리 실행
cursor.execute("SELECT TOP 10 (ACCNBR) FROM ACCDEF;")
result = cursor.fetchall()

# 결과 표시
st.write(result)

conn.close()
