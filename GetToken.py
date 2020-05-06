import base64
import json
import requests
import hashlib

import hashlib
import time

loginKey = "bSxP2jCuAbWkwIkY";
phoneKey = "qcV6MVsPx8ts0sTY";
padKey = "rCxcMTYgVxeGJD3HCWE6p2vUSAfsKeUk";
childrenGuardKey = "DyXEW2SGf6d8OHms";
watchKey = "LKyF8jThHbZfUeTP";
serverKey = "EszvQIizkX7vgRp7";
wifiReader_IOSKey = "mXhRItnwWSO12KO9";
wifiReader_AndroidKey = "kJDy0uRlxfiJNY7X";

ISOTIMEFORMAT = "%Y-%m-%d %H:%M:%S"

nowtime = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))


def getLoginmd5(initStr):
    import hashlib
    import types
    forceStr = str(initStr)
    count = 0
    encryptCount = 0
    loginParaLIst = ["days=-2", "deviceId=a0:93:47:5e:d1:16", "mac=a0:93:47:5e:d1:16", "appId=11"]
    encryptStr = ""
    if type(forceStr) is types.StringType:
        if "##" in forceStr:
            forceStr.split('##')
            #  print forceStr.count("##")
            while count < forceStr.count("##"):
                loginParaLIst.append(forceStr.split('##')[count + 1])
                count = count + 1
            # loginParaLIst.append(forceStr.split('##')[count])
            loginParaLIst.append("timestamp=" + nowtime)
            loginParaLIst = sorted(loginParaLIst)
            #          print sorted(loginParaLIst)
            while encryptCount < len(loginParaLIst):
                if encryptCount != len(loginParaLIst) - 1:
                    encryptStr = encryptStr + loginParaLIst[encryptCount] + "##"
                else:
                    encryptStr = encryptStr + loginParaLIst[encryptCount]
                encryptCount = encryptCount + 1
                #      print encryptStr
            m = hashlib.md5()
            #   print forceStr.split('##')[0] + encryptStr
            m.update(forceStr.split('##')[0] + encryptStr + watchKey)
            #  print(m.hexdigest())
            return m.hexdigest()

    else:
        #return error
        print("error")


def getLoginStr(initStr):
    import types
    forceStr = str(initStr)
    count = 0
    encryptCount = 0
    loginParaLIst = ["days=-2", "deviceId=a0:93:47:5e:d1:16", "mac=a0:93:47:5e:d1:16", "appId=11"]
    encryptStr = ""
    if type(forceStr) is types.StringType:
        if "##" in forceStr:
            forceStr.split('##')
            while count < forceStr.count("##"):
                loginParaLIst.append(forceStr.split('##')[count + 1])
                count = count + 1
            # loginParaLIst.append(forceStr.split('##')[count])
            loginParaLIst.append("timestamp=" + nowtime)
            #            loginParaLIst = sorted(loginParaLIst)
            while encryptCount < len(loginParaLIst):
                if encryptCount != len(loginParaLIst) - 1:
                    encryptStr = encryptStr + loginParaLIst[encryptCount] + "&"
                else:
                    encryptStr = encryptStr + loginParaLIst[encryptCount]
                encryptCount = encryptCount + 1
        return encryptStr
    else:
        # return error
        print("error")


def getLoginmd5_server(initStr):
    import hashlib
    import types
    forceStr = str(initStr)
    count = 0
    encryptCount = 0
    loginParaLIst = ["areaCode=86", "deviceId=a0:93:47:5e:d1:16", "mac=a0:93:47:5e:d1:16", "appId=9"]
    encryptStr = ""
    if type(forceStr) is types.StringType:
        if "##" in forceStr:
            forceStr.split('##')
            print
            forceStr.count("##")
            while count < forceStr.count("##"):
                loginParaLIst.append(forceStr.split('##')[count + 1])
                count = count + 1
            # loginParaLIst.append(forceStr.split('##')[count])
            loginParaLIst.append("timestamp=" + nowtime)
            loginParaLIst = sorted(loginParaLIst)
            print
            sorted(loginParaLIst)
            while encryptCount < len(loginParaLIst):
                if encryptCount != len(loginParaLIst) - 1:
                    encryptStr = encryptStr + loginParaLIst[encryptCount] + "##"
                else:
                    encryptStr = encryptStr + loginParaLIst[encryptCount]
                encryptCount = encryptCount + 1
            print
            encryptStr
            m = hashlib.md5()
            print
            forceStr.split('##')[0] + encryptStr
            m.update(forceStr.split('##')[0] + encryptStr + serverKey)
            print(m.hexdigest())
            return m.hexdigest()

    else:
        # return error
        print("error")


def getLoginStr_server(initStr):
    import types
    forceStr = str(initStr)
    count = 0
    encryptCount = 0
    loginParaLIst = ["areaCode=86", "deviceId=a0:93:47:5e:d1:16", "mac=a0:93:47:5e:d1:16", "appId=9"]
    encryptStr = ""
    if type(forceStr) is types.StringType:
        if "##" in forceStr:
            forceStr.split('##')
            while count < forceStr.count("##"):
                loginParaLIst.append(forceStr.split('##')[count + 1])
                count = count + 1
            # loginParaLIst.append(forceStr.split('##')[count])
            loginParaLIst.append("timestamp=" + nowtime)
            #            loginParaLIst = sorted(loginParaLIst)
            while encryptCount < len(loginParaLIst):
                if encryptCount != len(loginParaLIst) - 1:
                    encryptStr = encryptStr + loginParaLIst[encryptCount] + "&"
                else:
                    encryptStr = encryptStr + loginParaLIst[encryptCount]
                encryptCount = encryptCount + 1
        return encryptStr
    else:
        # return error
        print("error")

# print getLoginmd5("abcd##abc##abcde")
# print getLoginStr("abcd##abc##abcde")


headers = {'Content-Type': 'application/json'}


def login(number, password, url):
    signStr = "https://" + url + "/app/login##" + "password=" + password + "##" + "userName=" + number
    sign1 = getLoginmd5(signStr)
    logStr = getLoginStr(url + "##password=" + password + "##userName=" + number)
    getUrl = "https://" + url + "/app/login?" + logStr + "&sign=" + sign1
    response = requests.post(getUrl)

    token = response.json()["data"]
    return json.dumps(token)

def login_test(number, password, url):
    signStr = "http://" + url + "/app/login##" + "password=" + password + "##" + "userName=" + number
    sign1 = getLoginmd5(signStr)
    logStr = getLoginStr(url + "##password=" + password + "##userName=" + number)
    getUrl = "http://" + url + "/app/login?" + logStr + "&sign=" + sign1
    response = requests.post(getUrl)

    token = response.json()["data"]

    return json.dumps(token)
# login("13717414578","zyl123456","account.okii.com")

signKey = "82c81ef2f73b44af"
def getSign(url,baseStr,body):
    md5Str = url+baseStr+body+signKey
    print (md5Str)
    m = hashlib.md5()
    m.update(md5Str)
    print(m.hexdigest())
    return m.hexdigest()


#getSign("/smartwatch/holidayguard","123","123")


def getAccountId(number, url):
    getUrl = "http://" + url + "/mobileaccount/getMobileIdByNumber/" + number
    response = requests.get(getUrl, headers=headers)
    print (response.json()["data"]["id"])
    return response.json()["data"]["id"]

getAccountId("13717414578","watch.module.okii.com")

    #return json.dumps(token)
def getPhoneByToken(mac, appId, url,timestamp,number, password):
    signStr = "http://" + url + "/server/getPhoneByToken##" + "appId=" + appId + "##" + "mac=" + mac + "timestamp=" + timestamp
    print(signStr)
    sign = getLoginmd5(signStr)
    #logStr = getLoginStr(url + "appId=" + appId + "##" + "mac=" + mac + "timestamp=" + timestamp)
    token = login(number, password, url)
    getUrl = "http://" + url + "/server/getPhoneByToken/" + "appId=" + appId + "##" + "mac=" + mac+ "timestamp=" + timestamp + "&sign=" + sign+ "&token=" + token
    response = requests.get(getUrl, headers=headers)
    print (response.json()["data"]["id"])
    return response.json()["data"]["id"]

#getPhoneByToken("a0:93:47:5e:d1:16","1","account.alpha.okii.com","2017-08-02 09:37","18566174962","y123456")
sign = getLoginmd5("http://account.alpha.okii.com/server/getPhoneByToken##appId=1##mac=a0:93:47:5e:d1:16##timestamp=2017-08-02 09:37")