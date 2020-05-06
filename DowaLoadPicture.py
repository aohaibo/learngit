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


def getSogouImage(category, length, path):
    n = length
    cate = category
    # 植物'https://pic.sogou.com/pics?query=%D6%B2%CE%EF&w=05009900&p=&_asf=pic.sogou.com&_ast=1551841075&sut=2435&sst0=1551841074994'
    # 壁纸'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n)
    imgs = requests.get('https://pic.sogou.com/pics?query=%D6%B2%CE%EF')
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        imgs_url.append(j['bthumbUrl'])
    m = 0
    for img_url in imgs_url:
        print('***** ' + str(m) + '.jpg *****' + '   Downloading...')
        urllib.request.urlretrieve(img_url, path + str(m) + '.jpg')
        m = m + 1
    print('Download complete!')


def getSogouImag_search(query, length, path):
    # 搜索类型的 - 搜狐每次加载48张
    n = (int)(length / 48)

    for i in range(n):
        start = (i + 6) * 48
        start = 284
        url = 'https://pic.sogou.com/pics?query=' + query + '&mode=1&start=' + str(
            start) + '&reqType=ajax&reqFrom=result&tn=0'
        print(url)
        imgs = requests.get(url)

        jd = json.loads(imgs.text)
        jd = jd['items']
        imgs_url = []
        for j in jd:
            imgs_url.append(j['pic_url'])
        m = 0
        for img_url in imgs_url:
            print('***** ' + str(m) + '.jpg *****' + '   Downloading...')
            try:
                pic_download(img_url, path + str(start) + str(m) + '.jpg')
            except:
                print('error!')
            m = m + 1

    print('Download complete!')


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
getSogouImag_search('%CA%C0%BD%E7%D6%F8%C3%FB%BE%B0%B5%E3', 500, 'd:/download/景点/')