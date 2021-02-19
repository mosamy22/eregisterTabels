import cx_Oracle
import pandas as pd

con = cx_Oracle.connect("QABOOL_USER/QABOOL_USER@10.101.1.11:1521/ORCL", encoding="utf-8")

data = pd.read_sql('SELECT * FROM MCST.SIS_STUDENTS', con)
con.close()

data.head() # take a peek at data
data.to_excel('students2.xlsx')
