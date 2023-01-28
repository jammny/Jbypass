### Bypass测试  
在`encrypt.py`文件中，替换你的shellcode：

![img.png](img/img_3.png)  

执行：`python2 encrypt.py`  

![img_1.png](img/img_4.png)  

在`Jbypass.py`文件中，替换成你的服务器地址：

![img_2.png](img/img_5.png)  

python2打包exe：`pyinstaller.exe -F -w .\Jbypass.py`

火绒测试：

![img.png](img/img.png)  

360测试：    

 ![img_1.png](img/img_1.png)  

WD测试：  

![img_2.png](img/img_2.png)
