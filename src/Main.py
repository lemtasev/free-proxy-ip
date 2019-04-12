# -*- coding: utf-8 -*-
from CheckIp import *
from FreeProxy import *
import sys

fp = FreeProxy()
cp = CheckIp()

while True:
    print("1.调用api获取proxy ip")
    print("2.检查proxy ip是否可用")
    print("0.退出")
    str = input("请输入：")
    if str == "0":
        print("Bye~")
        sys.exit()
    elif str == "1":
        fp.getAllProxyIp()
    elif str == "2":
        cp.start()
    else:
        print("输入错误！")
