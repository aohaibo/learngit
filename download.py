import requests
import json
import urllib
import socket

def pic_download(url, image_name):
    # 设置超时时间为30s
    socket.setdefaulttimeout(30)
    # 解决下载不完全问题且避免陷入死循环
    try:
        urllib.request.urlretrieve(url, image_name)
    except socket.timeout:
        count = 1
        while count <= 5:
            try:
                urllib.request.urlretrieve(url, image_name)
                break
            except socket.timeout:
                err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                print(err_info)
                count += 1
        if count > 5:
            print("downloading picture fialed!")
pic_download("http://tu.2015img.com/dateimg/190111/154G544J960211162.jpg", "test")
# getSogouImag('壁纸',2000,'d:/download/壁纸/')
# 植物 - %D6%B2%CE%EF
# 动物 - %B6%AF%CE%EF
# 网店商品摄影 - %CD%F8%B5%EA%C9%CC%C6%B7%C9%E3%D3%B0
# 名人头像 - %C3%FB%C8%CB%CD%B7%CF%F1
# 菜品 - %B2%CB%C6%B7
# 汽车标志
# 电影海报 %B5%E7%D3%B0%BA%A3%B1%A8
# 名牌标志 - %C3%FB%C5%C6%B1%EA%D6%BE
# 专辑封面 - %D7%A8%BC%AD%B7%E2%C3%E6
# 图书封面 - %CD%BC%CA%E9%B7%E2%C3%E6
# 红酒牌子 - %BA%EC%BE%C6%CA%B5%CE%EF
# 红酒品牌图标 - %BA%EC%BE%C6%C6%B7%C5%C6%CD%BC%B1%EA
# 世界名画欣赏100幅 - %CA%C0%BD%E7%C3%FB%BB%AD%D0%C0%C9%CD100%B7%F9
# %CA%C0%BD%E7%D6%F8%C3%FB%BE%B0%B5%E3
#getSogouImag_search('%CA%C0%BD%E7%D6%F8%C3%FB%BE%B0%B5%E3', 500, 'd:/download/景点/')