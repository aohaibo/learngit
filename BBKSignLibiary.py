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
        return
m=str("https://" + "account.alpha.okii.com" + "/app/login##" + "password=" + "y123465" + "##" + "userName=" + "17688939941")

getLoginmd5(str(m))