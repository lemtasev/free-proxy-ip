# -*- coding: utf-8 -*-

# from urllib import request, parse
# import ssl
#
# # url = r"http://ip.tool.chinaz.com/" # 检测ip网址
# # url = r"http://www.baidu.com/"
# url = r"https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list" # 开源代理ip查询接口
# headers = {
#     'User-Agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   r'Chrome/73.0.3683.86 Safari/537.36',
#     # 'Referer': r'',
#     'Connection': 'keep-alive'
# }
# postData = {
#     # 'name': 'abc'
# }
# postData = parse.urlencode(postData).encode('utf-8')
# ssl._create_default_https_context = ssl._create_unverified_context
#
# # 设置proxy
# proxy = request.ProxyHandler({'http': '104.154.40.136:8080'})
# opener = request.build_opener(proxy)
# request.install_opener(opener)
#
# req = request.Request(url, data=postData, headers=headers)
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))
