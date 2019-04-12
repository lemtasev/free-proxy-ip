# -*- coding: utf-8 -*-

from urllib import request
import ssl
import json

"""
读取data/目录下的ip，测试代理连接是否可用
"""
class CheckIp:

    def __init__(self, url = r"http://www.baidu.com"):
        self.url = url

    def checkHttpConnect(self, proxyIp, proxyPort):
        headers = {
            'User-Agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                          r'Chrome/73.0.3683.86 Safari/537.36',
            # 'Referer': r'',
            'Connection': 'keep-alive'
        }
        ssl._create_default_https_context = ssl._create_unverified_context
        # 设置proxy
        proxy = request.ProxyHandler({'http': proxyIp + ":" + proxyPort})
        opener = request.build_opener(proxy)
        request.install_opener(opener)

        req = request.Request(self.url, headers=headers)
        try:
            print("connecting:" + self.url, "proxy:" + proxyIp + ":" + proxyPort)
            response = request.urlopen(req, timeout=10)
            code = response.getcode()
        except Exception as err:
            print("error: {0}".format(err))
            code = -1
        if code == 200:
            # 访问成功
            return True
        else:
            # 失败
            return False

    def start(self):
        with open(r'../data/all_ip.txt', 'r') as f:
            allIpList = f.readlines()
        print("there are ",allIpList.__len__()," ip")
        successIpList = []
        failIpList = []
        i = 0
        for ipStr in allIpList:
            i = i + 1
            if i > 10:
                break
            d = json.loads(ipStr)
            if self.checkHttpConnect(str(d['host']), str(d['port'])):
                # 加入可用ip列表
                successIpList.append(ipStr)
            else:
                # 加入不可用列表
                failIpList.append(ipStr)

        print("available ip:",successIpList.__len__())
        print("unavailable ip:",failIpList.__len__())
        with open(r'../data/suc_ip.txt', 'w') as f:
            f.write(''.join(successIpList))

        with open(r'../data/fai_ip.txt', 'w') as f:
            f.write(''.join(failIpList))
