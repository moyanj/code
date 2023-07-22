import requests
import time
from threading import Thread

global total


# 请求函数
def request_get(
    url, ret_type="text", timeout=5, encoding="utf-8", host="bbs-api.mihoyo.com"
):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Origin": "https://bbs.mihoyo.com",
        "Referer": "https://bbs.mihoyo.com/",
        "Host": host,
    }
    res = requests.get(url=url, headers=headers, timeout=timeout)
    res.encoding = encoding
    if ret_type == "text":
        return res.text

    elif ret_type == "image":
        return res.content

    elif ret_type == "json":
        return res.json()


# 保存图片
def save_image(image_src):
    try:
        content = request_get(image_src, "image", host="upload-bbs.mihoyo.com")
        with open(f"mys/{str(time.time())}.jpg", "wb") as f:
            f.write(content)
            global total
            total += 1
            print(f"保存第{total}张图片")
    except Exception as e:
        print("下载失败")


# 抓取内页数据
def detail(post_id):
    url = f"https://bbs-api.mihoyo.com/post/wapi/getPostFull?gids=5&post_id={post_id}&read=1"
    try:
        res_json = request_get(url, ret_type="json", timeout=5)
        if res_json["retcode"] == 0:
            image_list = res_json["data"]["post"]["image_list"]
            for img in image_list:
                img_url = img["url"]
                if (img_url.find("weigui")) < 0:
                    save_image(img_url)
    except Exception as e:
        print("内页数据抓取失败")


# 抓取函数
def main(last_id, forum_id):
    # 起始页面
    url = f"https://bbs-api.mihoyo.com/post/wapi/getForumPostList?forum_id={forum_id}&gids=2&is_good=false&last_id={last_id}&is_hot=false&page_size=20&sort_type=2"
    res_json = request_get(url, ret_type="json", timeout=5)
    if res_json["retcode"] == 0:
        for item in res_json["data"]["list"]:
            # 抓取内页数据
            detail(item["post"]["post_id"])

    if res_json["data"]["last_id"] != "":
        return main(res_json["data"]["last_id"], forum_id)


if __name__ == "__main__":
    global total
    total = 0
    thread_pool = []
    # 同人图

    tr1 = Thread(target=main, args=(40745785, 29))
    thread_pool.append(tr1)
    tr2 = Thread(target=main, args=(1687933524.358764, 29))
    thread_pool.append(tr2)
    tr3 = Thread(target=main, args=(1687933170.182543, 29))
    thread_pool.append(tr3)
    tr4 = Thread(target=main, args=(1687932828.457253, 29))
    thread_pool.append(tr4)
    # COS图

    cos1 = Thread(target=main, args=(1687933784.662275, 49))
    thread_pool.append(cos1)
    cos2 = Thread(target=main, args=(1687933138.048382, 49))
    thread_pool.append(cos2)
    cos3 = Thread(target=main, args=(1687934230.799456, 49))
    thread_pool.append(cos3)
    cos4 = Thread(target=main, args=(1687933632.420243, 49))
    thread_pool.append(cos4)
    for i in thread_pool:
        i.start()
