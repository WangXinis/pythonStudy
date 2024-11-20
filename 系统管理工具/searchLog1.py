#grep -oP '^(\w{3} \d{2} \d{2}:\d{2}:\d{2})(.+)((?:\d{1,3}.){3}\d{1,3})$' /root/myiplogin.log
#通过命令，将日志中含有日期和ip的文件输出到 myiplogin.log
#找出文件中的ip
#处理日志文件中的ip
import re

# 正则表达式模式
#pattern = r'(\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b \d{1,2} \d{2}:\d{2}:\d{2})\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
#pattern = r'(\(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b \d{1,2} \d{2}:\d{2}:\d{2})\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
pattern = r'(\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b \d{1,2} \d{2}:\d{2}:\d{2})\s+(.*\.\d{1,3}\.\d{1,3}\.\d{1,3})'
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
#pattern = r'^(\d{4}-\d{2}-\d{2})(.+)((?:\d{1,3}.){3}\d{1,3})$'
# 读取文件内容
# todo 
# 根据登录日志，查找多次尝试登录失败的用户，添加进防火墙
with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
        # 查找所有匹配的日期和IP地址
        matches = re.findall(pattern, content)
        #ip_matches=re.findall(ip_pattern,content)
        
        #print("matches:",matches)
        # 打印所有找到的日期和IP地址
        """
        ip_match = re.search(ip_pattern, text)
        ip = ip_match.group()
        """
        for match in matches:
                #匹配日期
                #print(f"Date: {match[0]}, IP: {match[1]}",end=",")
                print(f"Date: {match[0]}",end=",")
                #匹配ip地址
                ip_match=re.search(ip_pattern, str(match[1]))
                IP=ip_match.group()
                print(f"IP:{IP}")
