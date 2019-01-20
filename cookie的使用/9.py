"""死马当做活马"""
import requests 
# print(cookie)
"""
tgw_l7_route=1b9b7363f02f3a5519d03bdf813bc914; _zap=b6cb354a-5788-486d-b4ba-3c4a38707604; _xsrf=GdBbPvfgJvVNDULjL9y665wgmBp5y4Wd; d_c0="AODjQNvG2Q6PTo0HsK8FGwekG-vh0Us1688=|1547912921"; capsion_ticket="2|1:0|10:1547912929|14:capsion_ticket|44:Y2U3ZGI0Y2MwZmI3NGU3YWFiODkwM2YyOGM1M2ViYjI=|fcbbe5d7f4172560b1a296356e67c0348c300043a0b23a3e71fa8da2adccf4e9"

"""
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	'Cookie':'_zap=5b62d4cc-e687-45cd-ad70-e9de4faeb700;_xsrf=10513cbc-2a68-4e90-94dc-b3dd6ecc646d;d_c0=AEBpddnodQ6PToAmCszRXGQ-5n8T1vDhpRQ=|1541210945;l_n_c=1; n_c=1; tst=r;oauth_from=/settings/account; q_c1=1b9dc9b92e8848429a35d2a3bf6d7e5a|1547782229000|1541210947000;__utma=51854390.370178362.1547821188.1547821188.1547821188.1; __utmc=51854390; __utmz=51854390.1547821188.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20170612=1^3=entry_date=20170612=1; l_cap_id=MzI0ZDZhZGJkN2ZmNGE0MDlkYjUyZmE3YWI2OGRiZmI=|1547821684|ac372f4b27d1389076ecee53b9582350e571ad13;r_cap_id="YTk1ZWJiNTVhZTFiNDllNmFlNWZhZTJlMWIwOTM0NGQ=|1547821684|e84927aa321a5858847d4aab57078ff2de2fd3fd;cap_id=NDVjZTNmMzMzNTJhNDJjMzk4MmMxN2I5MjQ1ZjY2MjI=|1547821683|e3bc57c466cb42eca2927bed86b2a9dc99b779d5"; tgw_l7_route=66cb16bc7f45da64562a077714739c11; capsion_ticket="2|1:0|10:1547911712|14:capsion_ticket|44:ZDUyMDRhNzA4ZTZkNDgyMThmN2Y2NGUzNmMwZjcxMTc=|df134b2572c27923da2b99cab0614d6b3060b1ce02beb5f28db449dff9188aa7;z_c0=2|1:0|10:1547911721|4:z_c0|92:Mi4xd05NdkJRQUFBQUFBUUdsMTJlaDFEaVlBQUFCZ0FsVk5LWkF3WFFCWDNUMC1BUXBIbUVwdTZfYzE3N1NlT1g1V2lR|79adf8678ba5a79fbfd3d293439c5212675e31e899e37021466cef28a8eca466'
	 # 
	#  ',
}
url='http://www.zhihu.com'
print("我想要爬取的网页是:"+url)
r=requests.get(url,headers=headers)
data=r.text
fandle=open("./92.html","w",encoding="utf-8")
fandle.write(str(data))
fandle.close()
