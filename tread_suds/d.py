import cx_Oracle
from suds.client import Client

# 连接Oracle数据库
cx_Oracle.init_oracle_client(lib_dir="C:\oraclemini")
connection = cx_Oracle.connect('BSHIP_LOG/BSOFT@172.31.10.164:1521/hip32.shpdh.org')

# 注意，有些文档里接口可能没把?wsdl写进去，但是调用时是需要有这个参数的
url = "http://172.31.10.156:9528/hai/WebServiceEntry?wsdl"

client = Client(url)

cur = connection.cursor()
cur.execute("SELECT ARGS as parameter FROM BSHIP_LOG.LOG_ES where substr(procedeureid,1,1) = 'd'  ")

parameter_value = ''
for row in cur:
    clob_data = row[0].read()
    try:
        result = client.service.invoke(service="ClpSendMessageLog", urid="", pwd="", parameter=clob_data)
        print(result)
    except Exception as e:
        print(e)

cur.close()
connection.close()