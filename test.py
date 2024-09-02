"""
Connects to a SQL database using pymssql
"""
import pymssql
import pandas as pd
import streamlit as st

## MSSQL 접속
conn = pymssql.connect(
    server='172.16.0.230',
    port='49936',
    user='sa_imn',
    password='Wdk@0424!@#$',
    database='IEDATA_IMN',
    as_dict=True
)
cursor = conn.cursor()

## SQL문 실행
SQL_QUERY = """
SELECT TOP 10 (ACCNBR) FROM ACCDEF a ;
"""
cursor.execute(SQL_QUERY)

# records = cursor.fetchall()
# for r in records:
#     print(f"{r['ACCNBR']}")

row = cursor.fetchall()
# while row:
#     # print(row)
#     row=cursor.fetchone()
#     break

conn.close()

# print(row)
df = pd.DataFrame(row)
print(df)

st.dataframe(df)
