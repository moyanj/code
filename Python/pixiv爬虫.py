import requests as r
import json
import uuid
import time
import random
from requests.packages import urllib3
from threading import Thread

urllib3.disable_warnings()
save_path = "./pixiv/"
pre = "https://www.pixiv.net/ajax/"
FP = "lang=zh&version=8a10a9007b94f71b617fe580e88bd087c13a8994"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5859.0 Safari/537.36 Edge/117.0.1945.0",
    "Cookie": "",
}


def seacrh_url(word, page):
    tmp1 = pre + "search/artworks/" + word
    tmp2 = tmp1 + "?order=date_d&mode=all&p=" + str(page)
    tmp3 = tmp2 + "&s_mode=s_tag&type=all&" + FP
    print("本次搜索URL：" + tmp3)
    return tmp3


def imageList_url(id):
    path = pre + "illust/{}/pages".format(id)
    url = path + "?" + FP
    print("本次图片json的URL：" + url)
    return url


def getSeacrh_list(word, page):
    idList = []
    url = seacrh_url(word, page)
    resp = r.get(url, headers=header, verify=False)
    dictData = json.loads(resp.text)
    msgPack_data = dictData["body"]
    illustManga_data = msgPack_data["illustManga"]
    data = illustManga_data["data"]
    for i in data:
        id = i["id"]
        print("这次获取到的作品ID：" + id)
        idList.append(id)
    return idList


def getImage_list(ids):
    idImg_url = []
    for id in ids:
        imgUrl = []
        url = imageList_url(id)
        resp = r.get(url, headers=header, verify=False)
        dictData = json.loads(resp.text)
        msgPack_data = dictData["body"]
        for imageUrls in msgPack_data:
            urls = imageUrls["urls"]
            imageUrl = urls["original"]
            print("这次获取到的图片URL：" + imageUrl)
            imgUrl.append(imageUrl)
        idImg_url.append(imgUrl)
    return idImg_url


def download(url):
    print("本次文件下载URL:" + url)
    headers = header
    file_name = url.split("/")[11]
    id = file_name.split("_")[0]
    headers["Referer"] = "https://www.pixiv.net/artworks/{}".format(id)
    try:
        resp = r.get(url, headers=headers, verify=False)
        path = save_path + file_name
        f = open(path, "wb")
        f.write(resp.content)
    except Exception as e:
        print("文件下载失败")
    time.sleep(0.125)


def main(word, page):
    for i in range(1, page):
        id_list = getSeacrh_list(word, i)
        img_list = getImage_list(id_list)
        for imgUrls in img_list:
            for url in imgUrls:
                download(url)


main("原神", 100)
