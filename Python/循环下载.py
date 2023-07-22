import wget
def dom(domurl, s):
    for i in range(s):
        test = "第"+str(i + 1)+"张"
        print("正在下载{}".format(test))
        lj = data + "\{}.png".format(test)
        print(domurl)
        wget.download(domurl, lj)
        print("\n{}下载完毕".format(test))
        t.sleep(1)