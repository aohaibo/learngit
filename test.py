import os
import hashlib
import urllib
fp=open("D:/url.txt", "r");
mn=open("D:/sign.txt", "a+");

for eachline in fp:
    #mn.writelines(eachline)
    eachline=str(eachline.strip('\n'))
    PrivateKey='103b3f626336a803f85a6e8ab1cffa21312af43a'
    ss='PublicKeyGbKtZsxxc3k8C5nbW0YJoa+4S/4a6JzMnzp6h50NuwHe3n206T/UEA==ResourceIduaicensor-emgglselTimestamp1558317762241Url%s%s'%(eachline,PrivateKey)
    print(ss)
    sign = hashlib.sha1()
    sign.update(ss.encode("utf8"))
    signature = sign.hexdigest()
    print (eachline+","+signature);
    mn.writelines(eachline+","+signature);