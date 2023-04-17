# py 
 
### 1. es获取服务入参再上传 
#### 场景：闭环表空间满了之后，闭环服务瘫了几天，但还是有入参存在es中。重传这些数据就需要从es中获取到入参再上传。

##### 获取es中服务失败的webservice入参，然后存储到oracle数仓，再从字段中获取遍历再提交

   - es存到oracle的脚本`es_to_oracle.py`
   - oracle读取到重新上传用到`suds_oracle.py`
   - `tread_suds`文件夹是`suds_oracle.py`的多个拆分，根据16进制id号拆分成16个段，同时批量跑
   
   - 用来练习的脚本 `test_es_conn.py` 、`test_oracle_conn.py`、 `try_suds.py`来测试接口

### 2. 实时获取闭环节点配置，自动生成excel分组
   
