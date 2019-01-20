import urllib.request
from http import cookiejar
 
def save_cookie(url, cookie_filename):
    cookie = cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    resp = opener.open(url)
    cookieStr = ''
    for item in cookie:
        cookieStr = cookieStr + item.name + '=' + item.value + ';'
        print(cookieStr)
    # print(cookieStr)
    cookie.save()
 
 
if __name__ == '__main__':
    url = 'http://www.baidu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'
    }
    cookie_filename = 'cookie.txt'
    req = urllib.request.Request(url, headers=headers)
    save_cookie(req, cookie_filename)
