import os

import pandas as pd
import subprocess

test_unit = 'testunit2.exe'
cmd = subprocess.Popen(['C:\\Users\\13994\\PycharmProjects\\OptDataHook\\testunit2.exe'], shell=True,
                       stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
cmd.stdin.write('100\n'.encode('gbk'))
cmd.stdin.write('299\n'.encode('gbk'))
# 实时输出
# for lineItem in iter(cmd.stdout.readline,'b'):
#     encode_type = chatdet.detect(item)

# 非实时
info,err = cmd.communicate()
if err.decode('gbk') == '':
    # info.decode('gbk')
    list1=info.decode('gbk').split('\r\n')
    print(int(list1[1]))

