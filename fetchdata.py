import xlsxwriter
from xlsxwriter import Workbook
import cx_Oracle



conn = cx_Oracle.connect("QABOOL_USER/QABOOL_USER@10.101.1.11:1521/ORCL", encoding="utf-8")

workbook = xlsxwriter.Workbook('students.xlsx')
sheet = workbook.add_worksheet()

cur = conn.cursor()
cur.execute("select * from MCST.SIS_STUDENTS")

for r, row in enumerate(cur.fetchall()):
         for c, col in enumerate(row):
                sheet.write(r, c, col)

workbook.close()
cur.close()


