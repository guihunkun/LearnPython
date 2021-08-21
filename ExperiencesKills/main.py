import os
import re
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import xlwt
import xlsxwriter


def command_line_parameters():
    print("命令行参数个数: ", len(sys.argv))
    print("命令行参数列表: ", sys.argv)
    for i in range(len(sys.argv)):
        print("第 ", i, " 个参数是 : ", sys.argv[i])


def path():
    # 1) 改变当前工作目录到指定的路径
    # os.chdir() # 方法用于改变当前工作目录到指定的路径
    # os.chdir("E:/computer/Pycharm/ExperiencesKills")
    # os.chdir("../")  # 到当前目录的上一级目录

    # 2) 获取当前文件的绝对路径
    abspath = os.path.abspath(__file__)  # 获取当前文件的绝对路径
    print(abspath)

    # 3) 获取指定的文件夹包含的文件或文件夹的名字的列表
    # os.listdir()  # 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    listdirs = os.listdir()
    print(listdirs)

    # 4) 获取当前文件夹的上一层目录
    # os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 表示获取当前文件夹上一层目录
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # 5) 创建文件夹
    fold = "guihun"
    folder = os.path.exists(fold)  # 判断是否存在文件夹如果不存在则创建为文件夹
    if not folder:
        os.makedirs("fold")

    # 6) 判断路径 path 是否存在
    # os.path.exists(path)  # 如果路径 path 存在，返回 True; 如果路径 path 不存在，返回 False
    path = listdirs[1]
    if os.path.exists(path):
        print(path, "文件存在")
    else:
        print(path, "文件不存在")

    # 7) 创建名字为 fileName 的txt文件
    file_name = "memo"
    file = open(file_name + '.txt', 'w')
    file.close()


def read_allFiles(path):
    # 获取指定文件夹 path 下的所有文件
    path_files = []
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    for file in files:
        if not os.path.isdir(file):
            file_name = os.path.join(path, file)
            path_files.append(file_name)
    return path_files


def read_all_specified_type_files(path, type):
    # 获取指定文件夹 path 下的所有 type 类型文件
    specified_files = []
    path_files = read_allFiles(path)
    for file in path_files:
        file_name = os.path.basename(file)  # 获取文件名
        if file_name.find(type) != -1:
            specified_files.append(file)  # 将文本文件提取出来
    return specified_files


def test_of_read_allFiles():
    route = "data"
    folder = os.path.exists(route)  # 判断是否存在文件夹如果不存在则创建为文件夹
    if not folder:
        os.makedirs(route)
    all_files = read_allFiles(route)
    print(all_files)

    txt_files = read_all_specified_type_files(route, ".txt")
    if txt_files:
        f = open(txt_files[0], 'r')  # 打开文本文件
        print(f.read())  # 读取文本文件内容
        f.close()


if __name__ == '__main__':
    # command_line_parameters()
    # path()
    test_of_read_allFiles()