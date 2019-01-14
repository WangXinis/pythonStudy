import re
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