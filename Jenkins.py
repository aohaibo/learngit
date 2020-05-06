 #-*- coding:gbk -*-
import jenkins
# -*- coding: utf-8
jenkins_server_url='http://172.28.2.7:8080'
user_id='20260289'
api_token='04c772598423993ae1232b21b70d305d'
server = jenkins.Jenkins(jenkins_server_url,username=user_id,password=api_token)
print(server)
name= 'wifi设置灰度环境'
print(server.get_job_info_regex(name, depth=0, folder_depth=0))
print(server.get_plugins())
print(server.get_all_jobs())
server.build_job(name)