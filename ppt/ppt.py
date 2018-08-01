# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: ppt.py
@time: 2018/7/31 15:25
'''
import turtle
import time
#turtle.Screen()._root.attributes("-fullscreen", True)
import os


# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         print(root)  # 当前目录路径
#         print(dirs)  # 当前路径下所有子目录
#         print(files)  # 当前路径下所有非目录子文件

l = ['C:/Users/dlc/Desktop/LeetCode/ppt/1 (1).jpg', 'C:/Users/dlc/Desktop/LeetCode/ppt/1 (2).jpg']
turtle.speed(1)
turtle.ht()
for i in l:
    turtle.clear()
    turtle.Screen().bgpic(i)
    time.sleep(3)
turtle.done()