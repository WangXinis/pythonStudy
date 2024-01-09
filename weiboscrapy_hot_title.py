"""
爬取微博热搜标题，并且输出到屏幕
"""

import os
import re
import requests
from datetime import datetime


url = 'https://s.weibo.com/top/summary'
headers = {
    'Cookie': 'SUB=_2AkMSwJ8Bf8NxqwFRmfoRz2viZI53zgjEieKknG7aJRMxHRl-yT8XqlQAtRB6OUCx7s9IHZqRvhcy9DRESTe3DnGbJN3T; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5VFX_vgrfwKkGdyUArfb-n; _s_tentry=passport.weibo.com; Apache=4270087777277.7.1704726583169; SINAGLOBAL=4270087777277.7.1704726583169; ULV=1704726583178:1:1:1:4270087777277.7.1704726583169:',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
date = datetime.now().strftime("%Y-%m-%d")
response = requests.get(url, headers=headers, timeout=3).text
href = re.findall(r'<a href="(/weibo\?q=.*&Refer=top)" target="_blank">(.*?)</a>[\s]*<span> (.*?)</span>', response)
# print(href)
for item in href:
    baseurl, title, index = item
    print(title)