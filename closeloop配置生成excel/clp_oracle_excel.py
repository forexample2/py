import cx_Oracle
from sqlalchemy import create_engine
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook

# 连接Oracle数据库
cx_Oracle.init_oracle_client(lib_dir="C:\oraclemini")
dsn = cx_Oracle.makedsn("172.31.10.164", "1521", service_name="hip32.shpdh.org")
conn = cx_Oracle.connect("BSHIP_CLP", "BSOFT", dsn=dsn)

# pd不能直接读oracle
engine = create_engine('oracle+cx_oracle://', creator=lambda: conn)

# 执行查询语句并将结果保存到pandas dataframe中
query = "select * from clp_view "
df = pd.read_sql(query, con=engine)
df = df.applymap(str)

engine.dispose()

# 创建Excel workbook和worksheet
wb = Workbook()
ws = wb.active

# 将pandas dataframe中的数据写入Excel worksheet
for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)


# 按照'闭环编码'字段进行分组
groups = df.groupby('闭环编码')

# 将每个分组写入一个新的sheet页
writer = pd.ExcelWriter('clp_group.xlsx', engine='xlsxwriter')
for name, group in groups:
    # 创建新的sheet页
    ws = writer.book.add_worksheet(str(name))
    # 将当前分组写入到新的sheet页中
    group.to_excel(writer, sheet_name=str(name), index=False, header=True)

writer.close()
