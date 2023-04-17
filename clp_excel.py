import openpyxl

wb = openpyxl.load_workbook('clp_group.xlsx')

sheet_names = wb.sheetnames

print(sheet_names)
http://172.31.10.156:8090/platform/oauth/authorize?oauth_token=f6d2834e9d79d5e3ea9abc158b3604af&oauth_callback=http%3A%2F%2F192.168.103.46%3A8080%2Fhip-dms%2Foauth%2Fcallback%3Fconsumer%3Dsample%26returnTo%3D%252Fhip-dms%252F#/evidenceClause



# ctrl + q 快速文档
# ctrl + j 建议列表
# ctrl + b 申明
# ctrl + / 注释
# ctrl + shift + / 块注释
# ctrl + e 最近文件
# ctrl +p 查看形参
# ctrl + shift + j  两行并一行
