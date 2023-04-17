# pip install elasticsearch==5.4.0，老版本需要装这个
from elasticsearch import Elasticsearch
import cx_Oracle

# 自己本地oracle目录指向
cx_Oracle.init_oracle_client(lib_dir="C:\oraclemini")

# 连接到 Elasticsearch
es = Elasticsearch(
    ['192.168.103.44'],
    http_auth=('elastic', 'bsoft01')
)

# 定义 Elasticsearch 查询语句
query = {
    "query": {
    "bool": {
    "must": [
    {
    "query_string": {
    "default_field": "bsoft.PartTime",
    "query": "0329"
    }
    }
    ,
    {
    "query_string": {
    "default_field": "bsoft.Return.Return_ik",
    "query": "tablespace"
    }
    }
    ,
    {
    "query_string": {
    "default_field": "bsoft.InputName",
    "query": "ClpSendMessageLog"
    }
    }
    ],
    "must_not": [ ],
    "should": [ ]
    }
    },
    "_source": ["bsoft.Args", "bsoft.DateTime","bsoft.ProcedeureID","bsoft.ErrId"],
    "from": 0,
    "size": 5,
    "sort": [ ],
    "aggs": { }
}

# 执行查询，使用 scroll API 获取所有数据
scroll = es.search(
    index="procedure",
    body=query,
    scroll="2m"
)

# 连接到 Oracle 数据库
connection = cx_Oracle.connect(
    user='BSHIP_LOG',
    password='BSOFT',
    dsn='172.31.10.164:1521/hip32.shpdh.org'
)
cursor = connection.cursor()

# 遍历所有结果并将其插入到 Oracle 表中
while True:
    # 获取当前滚动 ID
    scroll_id = scroll['_scroll_id']

    # 提取当前批次的结果
    results = scroll['hits']['hits']

    # 如果没有结果则退出循环
    if not results:
        break

    # 处理当前批次的结果
    for result in results:
        # 提取需要导出的字段
        field1 = result['_source']['bsoft.ProcedeureID']
        field2 = result['_source']['bsoft.DateTime']
        field3 = result['_source']['bsoft.ErrId']
        field4 = result['_source']['bsoft.Args']
        # ...

        # 将结果插入到 Oracle 表中
        insert_query = "INSERT INTO LOG_ES (PROCEDEUREID, DateTime, ErrId, Args) VALUES (:1, :2, :3, :4)"
        cursor.execute(insert_query, (field1, field2, field3, field4))

    # 获取下一批结果
    scroll = es.scroll(scroll_id=scroll_id, scroll='2m')

# 提交事务并关闭连接
connection.commit()
cursor.close()
connection.close()
