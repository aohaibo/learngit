#coding:utf-8
import requests
import json
import time
j=0
k=0
count=0
count2=0
for i in range(0,1):
    heads = open('e:/suki_header.txt').readlines()[i:i+1]
    datas = open('e:/suki_body.txt').readlines()[i:i+1]
    floor=open('e:suki_realfloor.txt').readlines()[i:i+1]
    heads = ''.join(heads).strip('\n')
    datas = ''.join(datas).strip('\n')
    print (datas)
    real_floor=''.join(floor).strip('\n')
    reactfloor=int(real_floor)+1000
    print (reactfloor)
    head1 = {"base-request-param":heads}
    datas1 = json.dumps(datas)
    r = requests.post("http://location.module.okii.com/steric/getFloors", data=datas, headers=head1)
    result = r.text
    print(result)
    a = json.loads(result)
    dataList = a.get('data')
    print(dataList['floorId'], dataList['buildingId'], dataList['reliability'])
    a=str(dataList['floorId'])
    print(a)
    b=dataList['buildingId']
    c=str(dataList['reliability'])
    print('------------------------------------'+'\n')
    '''筛选出置信度大于60和小于60的结果数量'''
    if int(c)<60 and int(a)==int(real_floor):
        m='true'
        j=j+1
        count=count+1
        print("count:"+count)
    else:
        m='flase'
        k=k+1
        if int(a)==int(real_floor):
            count2=count2+1
            print("count2:"+count2)
    with open ('e:/suki_results.txt','a+') as f:
        f.write("floorId:"+a+","+"buildingId:"+b+","+"reliability:"+c+',return_result:'+m+'\n')
        l=str(k)
        s=str(j)
    f.closed


with open ('f:/suki_results.txt','a+') as f:
    localtime = time.asctime(time.localtime(time.time()))
    f.write('\n'+'\n'+'\n')
    f.write(str(localtime)+'\n')

    f.write("reliability no more than 60:"+s+","+"reliability more than 60: "+l+'\n')
    f.write("------------------------sukisukisuki-----------------------"+'\n')

    f.write('\n' + '\n' + '\n')
f.closed