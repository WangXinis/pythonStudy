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