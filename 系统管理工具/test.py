import re

# 给定文本
text = "Nov 13 12:25:05 hecs-395634 sshd[488276]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=37.44.238.68"

# 正则表达式模式
pattern = r'(\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b \d{1,2} \d{2}:\d{2}:\d{2})\s+(.*\.\d{1,3}\.\d{1,3}\.\d{1,3})'
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
# 查找匹配的日期和IP地址
match = re.search(pattern, text)
ip_match = re.search(ip_pattern, text)
if match:
    date = match.group(1)
    ip = ip_match.group()
    print(f"Date: {date}, IP: {ip}")