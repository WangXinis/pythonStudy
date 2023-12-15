import time
now=time.localtime(time.time())
print(time.asctime(now))
print(time.strftime("%y年%m月%d日 %H:%M",now))