# anti-censorship
anti censorship

需要导入的就是PIL

打包库在lib/interfere.py中，导入后可以直接使用

支持往打开的图片中加入人为的噪点，可以采用随机方式，也可以采用指定方式

从原始文件中读取图像，然后加噪音后可保存，可显示

例子：
sample.py

原始文件：image/s.jpeg
四个加噪文件：
s0.jpeg
s1.jpeg
s2.jpeg
s3.jpeg

可以选择噪音方式，主要包括划线和画点方式，直接选择覆盖密度，噪点（线）的颜色范围


运行环境：
ubuntu 1804 LTS, Python 3.6

开发环境：
PyCharm CE （PyCharm 社区版）

