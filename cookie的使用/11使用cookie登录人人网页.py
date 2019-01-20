from urllib import request,parse
from http import cookiejar
 
# 创建cookiejar实例对象
cookie = cookiejar.CookieJar()
 
# 根据创建的cookie生成cookie的管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
 
# 创建http请求管理器
http_handle = request.HTTPHandler()
 
# 创建https管理器
https_handle = request.HTTPSHandler()
 
# 创建求求管理器，将上面3个管理器作为参数属性
# 有了opener，就可以替代urlopen来获取请求了
opener =  request.build_opener(cookie_handle,http_handle,https_handle)
 
def login():
    '''
    负责初次登录
    需要传递用户名和密码，来获取登录的cookie凭证
    '''
    # 登录url，需要从登录form的action属性中获取
    url = 'http://www.renren.com/PLogin.do'
 
    # 登录所需要的数据，数据为字典形式，
    # 此键值需要从form扁担中对应的input的name属性中获取
    username=input('请输入你的账户(手机、邮箱):')
    password=input('请输入你的密码:')
    data = {
        'email':username,
        'password':password
    }

 
    # 将数据解析成urlencode格式
    data = parse.urlencode(data)
    print(data,"的数据类型是:",type(data))
    data=bytes(data,'utf-8')
    print(type(data))
    req = request.Request(url,data=data)
 
    # 正常是用request.urlopen(),这里用opener.open()发起请求
    response = opener.open(req)
 
 
def getHomePage():
    '''
    获取登录后的页面
    '''
 
    # 此url是登录后的链接地址
    url = 'http://www.renren.com/969499568/profile'
 
    # 如果已经执行了上面的login函数，
    # 那么此时的opener已经是包含了cookie信息的一个opener对象
    res = opener.open(url)
 
    html = res.read().decode()
    htm=str(html)
    with open('renren.html','w',encoding='utf-8') as f:
        f.write(html)
 
def getOtherPage(url=None):
    if url is not None:
        res=opener.open(url)
        html = res.read().decode()
        htm=str(html)
        with open('YouWangted.html','w',encoding='utf-8') as file:
            file.write(html)
    else:
        print("爬取的网址是空的,请输入正确的url")

if __name__ == '__main__':
    '''
    依次执行上面两个函数
    '''
    login()
    getHomePage()
    url="http://friend.renren.com/managefriends"
    getOtherPage(url)