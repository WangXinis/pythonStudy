#grep -oP '^(\w{3} \d{2} \d{2}:\d{2}:\d{2})(.+)((?:\d{1,3}.){3}\d{1,3})$' /root/myiplogin.log
#通过命令，将日志中含有日期和ip的文件输出到 myiplogin.log
#找出文件中的ip
#处理日志文件中的ip
import re

# 正则表达式模式
#pattern = r'(\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b \d{1,2} \d{2}:\d{2}:\d{2})\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
pattern = r'(\(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b \d{1,2} \d{2}:\d{2}:\d{2})\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
#pattern = r'^(\d{4}-\d{2}-\d{2})(.+)((?:\d{1,3}.){3}\d{1,3})$'
# 读取文件内容
with open('example.txt', 'r') as file:
        content = file.readline()
        print(content)

        # 查找所有匹配的日期和IP地址
        matches = re.findall(pattern, content)
        print("matches:",matches)
        # 打印所有找到的日期和IP地址
        for match in matches:
                print(f"Date: {match[0]}, IP: {match[1]}")
