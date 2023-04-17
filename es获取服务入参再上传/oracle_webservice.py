import cx_Oracle
import requests
from zeep import Client
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin
from requests import Session
cx_Oracle.init_oracle_client(lib_dir="C:\oraclemini")
# 连接Oracle数据库
connection = cx_Oracle.connect('BSHIP_LOG/BSOFT@172.31.10.164:1521/hip32.shpdh.org')

# 创建Zeep客户端
''' 
wsdl = 'http://172.31.10.156:9528/hai/WebServiceEntry?wsdl'
session = Session()
history = HistoryPlugin()
transport = Transport(session=session, plugins=[history])
client = Client(wsdl=wsdl, transport=transport)
response = requests.post(url, json=data)
'''

# 获取数据
cursor = connection.cursor()
cursor.execute('SELECT ARGS FROM BSHIP_LOG.LOG_ES ')
rows = cursor.fetchall()
data = [row[0] for row in rows]

url = "http://172.31.10.156:9526/hai/HttpEntry"
data = {"service": "ClpSendMessageLog", "urid": "", "pwd": "", "parameter": data }
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    # 对结果进行处理
else:
    print(f"Error: {response.status_code} {response.reason}")

cursor.close()
connection.close()
'''
# 调用Web服务
result = client.service.web_method(data)
'''

# 输出结果
print(result)
