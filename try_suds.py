import suds
from suds.client import Client

# 注意，有些文档里接口可能没把?wsdl写进去，但是调用时是需要有这个参数的
url = "http://172.31.10.156:9528/hai/WebServiceEntry?wsdl"


Content = "<BSXml><MsgHeader><Sender>HIS</Sender></MsgHeader><MsgBody><Patient><SourcePatientId>1120575478</SourcePatientId><SourceVisitId>1120575478</SourceVisitId><ClinicId></ClinicId><HospizationId>1120575478</HospizationId><SourcePatientIdType>IV</SourcePatientIdType><AuthorOrganization >42501633100</AuthorOrganization><Name>沙信芳</Name></Patient><ClpInfo><BusinessID>1438731949</BusinessID><BusinessCircleID></BusinessCircleID><BusinessCompsiteID></BusinessCompsiteID><FlowCode>1104</FlowCode><FlowName>检验闭环(住院)</FlowName><OperateTypeCode>11040102</OperateTypeCode><OperateTypeName>护士复核</OperateTypeName><OperatorCode>0353</OperatorCode><OperatorName>徐苹</OperatorName><OperateDeptCode>347</OperateDeptCode><OperateDeptName>十二西</OperateDeptName><OperateDateTime>20230406T091802</OperateDateTime><GroupId></GroupId><GroupName></GroupName><OperateComments></OperateComments></ClpInfo></MsgBody></BSXml>"

client = Client(url)
print(client)


try:
    result = client.service.invoke(service="ClpSendMessageLog", urid="", pwd="", parameter=Content)
    print(result)
except Exception as e:
    print(e)