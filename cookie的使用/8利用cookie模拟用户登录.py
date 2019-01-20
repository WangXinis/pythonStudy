import urllib.request
from http import cookiejar
 
def load_cookie(url, cookie_filename):
    cookie = cookiejar.MozillaCookieJar()
    cookie.load(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    resp = opener.open(req)
    cookieStr = ''
    for item in cookie:
        cookieStr = cookieStr + item.name + '=' + item.value + ';'
    print(cookieStr)
 
 
if __name__ == '__main__':
    url = 'http://www.baidu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'
    }
    cookie_filename = 'cookie.txt'
    req = urllib.request.Request(url, headers=headers)
    load_cookie(req, cookie_filename)
    """突然想知道获取的内容是什么！！！"""
    response=urllib.request.urlopen(req)
    data=response.read()
    # print(type(data))
    # 'gbk' codec can't decode byte 错误解决方法:直接把上面代码read().decode('utf-8')取消了
    fandle=open("8.html","w")
    fandle.write(str(data))
    fandle.close()
