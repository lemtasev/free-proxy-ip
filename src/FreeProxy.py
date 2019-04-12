# -*- coding: utf-8 -*-

from urllib import request
import ssl

class FreeProxy:
    # url = r"https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"  # 开源代理ip查询接口
    def __init__(self, url = r"https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"):
        self.url = url

    def getAllProxyIp(self):
        print("get proxy ip from ",self.url,"...")
        print("this step may spend much time ...")
        headers = {
            'User-Agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                          r'Chrome/73.0.3683.86 Safari/537.36',
            'Connection': 'keep-alive'
        }
        ssl._create_default_https_context = ssl._create_unverified_context
        req = request.Request(self.url, headers=headers)

        # lines = res.splitlines()
        # for line in lines:
        #     print(line)

        try:
            response = request.urlopen(req)
            res = response.read().decode('utf-8')
            print("success!")
            with open('../data/all_ip.txt', 'w') as f:
                print("write result to data/all_ip.txt ...")
                f.write(res)
                print("write success!")
        except Exception as err:
            print("error: {0}".format(err))

        print("get ip json finish")

