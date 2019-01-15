import re
import  shelve

# \d 匹配数字  *是匹配一次或者多次
string="125789pythonad123"
pattern="\d*"
result=re.match(pattern,string)
print(result)
#.匹配除了换行符以外的任意字符
pattern2="py.*d"
result=re.match(pattern,string)
result2=re.search(pattern2,string)
print(result2)
#^匹配字符串开头位置 $匹配字符串结尾
string ="helloworld"
pattern="^hello"
result=re.search(pattern,string)
print(result)
#？匹配0次或者1次前面的原子
string ="wangsin"
pattern="wangs?"
result=re.search(pattern,string)
print(result)
# |模式选择符号，可以设置多个模式
pattern="python|java"
string ="I study java and python"
result=re.search(pattern,string)
print(result)
result=re.match(pattern,string,1)
print(result)
#()模式单元符
pattern="(cd){1,}"
string="testcdcdcdcdwang this is a test";
result=re.search(pattern,string)
print(result)
"""
    下面是模式修正
    I 匹配时忽略大小写
    M 多行匹配
    L 做本地化识别
    U 根据Unicode字符解析字符
    S 让.可以匹配换行符，就是用了这个之后.可以匹配任意字符了
"""
print("*"*50,"这里是模式修正的案例")
pattern1="python"
pattern2="python"
string="adfasdfsaPython_py"
result1=re.search(pattern1,string)
result2=re.search(pattern2,string,re.I)
print(result1)
print(result2)
pattern3=".*"
string="""
    www.baidu.com
    www.sina.com
"""
result3=re.search(pattern3,string,re.S)
result4=re.search(pattern3 ,string,re.UNICODE)
print(result3)
print(result4)
"""
    贪婪模式与懒惰模式
   贪婪模式：尽可能多的匹配；
   懒惰模式：尽可能少的匹配 
"""
print("*"*20,"贪婪模式与懒惰模式匹配例子","*"*20)
patter1="py.*y"#贪婪模式
pattern2="p.*?y"#懒惰模式
string="abcdpython_xyyy"
result1=re.search(pattern1,string)
result2=re.search(pattern2,string)
print(result1)
print(result2)