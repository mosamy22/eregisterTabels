import cx_Oracle
import pandas as pd

con = cx_Oracle.connect("QABOOL_USER/QABOOL_USER@10.101.1.11:1521/ORCL", encoding="utf-8")

data1 = pd.read_sql('SELECT * FROM MCST.SIS_STUDENTS', con)
data2 = pd.read_sql('SELECT * FROM MCST.SIS_ADVISORY_LISTS', con)
con.close()

data1.head() # take a peek at data
data1.to_excel('students.xlsx')

data2.head()
data2.to_excel('advisory.xlsx')
