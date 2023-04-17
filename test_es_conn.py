# -*- coding=utf-8'*-
# pip install elasticsearch==5.4.0，老版本需要装这个
from elasticsearch import Elasticsearch

# es = Elasticsearch(["http://192.168.103.44:9200"], http_auth=('elastic','bsoft01'))
es = Elasticsearch(
    ['192.168.103.44'],
    http_auth=('elastic', 'bsoft01')
)
# 查看连接是否成功
print(es.info())