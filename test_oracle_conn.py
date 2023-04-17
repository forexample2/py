import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir="C:\oraclemini")

# dsn_tns = cx_Oracle.makedsn('hostname', 'port', service_name='service_name')
# conn = cx_Oracle.connect(user='username', password='password', dsn=dsn_tns)

conn = cx_Oracle.connect(user='BSHIP_LOG', password='BSOFT', dsn='172.31.10.164:1521/hip32.shpdh.org')

# 执行 SQL 查询
cursor = conn.cursor()
cursor.execute('SELECT * FROM dual')
result = cursor.fetchall()

# 打印结果
for row in result:
    print(row)

# 关闭连接
cursor.close()
conn.close()