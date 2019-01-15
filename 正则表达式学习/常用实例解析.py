import re
"""
    解析网址
"""
pattern="[a-zA-Z]+://[^\s]*[.com|.cn]"
string="""
<a href="http://www.sina.com">百度首页</a>
"""
result=re.search(pattern,string)
print(result)
"""
    解析电话号码
"""
pattern="\d{4}-\d{7}|\d{3}-\d{8}|\d{11}"
string="13176221906"
result=re.search(pattern,string)
print(result)



