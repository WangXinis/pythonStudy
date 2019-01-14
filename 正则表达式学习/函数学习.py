import re
"""
    re.match()函数
    从源字符串的起始位置匹配一个模式
"""
string="apythonhellomypythonhistorypython"
pattern=".python."
result=re.match(pattern,string)
print(result)
print(result.span())
# 查看返回的类型
print(type(result.span()))
"""
    re.search()
    使用该函数会从整个字符串匹配
"""
string="hellomypythonhispythonourpyhonedn"
pattern=".python."
result=re.match(pattern,string)
result2=re.search(pattern,string)
print(result)
print(result2)
print("*"*20,"全局匹配模式","全局匹配模式")
"""
    全局匹配模式，上面的那种方法只能有一个输出结果，下面学习一下
    多个输出结果
   1、 使用re.compile()对正则表达式进行预编译
   2、 编译后使用findall()函数从字符串中找出所有结果
"""
string="hellomypythonhispythonourpythonend"
pattern=".python."
re_pattern=re.compile(pattern)
result=re_pattern.findall(string)
print(result)

