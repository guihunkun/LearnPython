import os
import numpy as np
import pandas as pd
import xlrd
import xlwt
import xlsxwriter
import matplotlib.pyplot as plt


def read_data(file):
    with open(file, "r") as f:
        id, subject_1, subject_2, subject_3 =[], [], [], []
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            line = line.split(' ')
            id.append((line[0]))
            subject_1.append(float(line[1]))
            subject_2.append(float(line[2]))
            subject_3.append(float(line[3]))
        row, col = len(subject_1), 3
        table = np.zeros((row, col))
        table[:, 0], table[:, 1], table[:, 2] = subject_1, subject_2, subject_3
        # head = ['subject_1', 'subject_2', 'subject_3']
        # data = pd.DataFrame(table)
        # data.columns = head
        return table


def write_excel_demo(file_name):
    workbook = xlsxwriter.Workbook(file_name)
    # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1
    worksheet = workbook.add_worksheet(u'Test')
    worksheet.write(0, 0, '数学')
    workbook.close()

def write_excel(file_name, data):
    workbook = xlsxwriter.Workbook(file_name)
    # 1）设置单元格格式
    style = workbook.add_format({
        "align": "center",    # 对齐方式
        "valign": "vcenter",  # 字体对齐方式
    })
    style_more = workbook.add_format({
        "fg_color": "yellow",  # 单元格的背景颜色
        "bold": 1,             # 字体加粗
        "align": "center",     # 对齐方式
        "valign": "vcenter",   # 字体对齐方式
        "font_color": "red"    # 字体颜色
    })

    # 2）设置数据格式为百分比
    style_pre = workbook.add_format({'num_format': '0.000%'})

    worksheet = workbook.add_worksheet(u'Score')  # 在文件中创建一个名为Score的sheet,不加名字默认为sheet1
    row, col = len(data), len(data[0, :])
    width = 20
    # 3) 设置单元格宽度
    worksheet.set_column(0, col, width)
    head = ['subject_1', 'subject_2', 'subject_3']
    '''
    for i in range(len(head)):
        worksheet.write(0, i+1, head[i], style_more) 
    '''
    worksheet.write_row('B1', head, style_more)  # 写入表头
    
    # 冻结第一行和第一列
    worksheet.freeze_panes(1, 1)
    
    for i in range(row):
        for j in range(col):
            worksheet.write(i+1, j+1, data[i][j], style)
    # 4) 调用Excel自身的公式
    worksheet.write(row, col+1, '=SUM(B6:D6)')

    # 5) 插入Excel图表
    chart = workbook.add_chart({"type": "column"})
    # column 柱状图
    # area面积图
    # bar 条形图
    # line折现图
    # radar雷达图
    # 5为图表添加数据
    chart.add_series(
        {"name": "成绩",  # 标题
         "categories": "=Score!$b$1:$d$1",  # 统计项名称 工作簿名称+数据
         "values": "=Score!$b$2:$d$2",  # 统计值 工作簿名称+数据
         "line": {"color": "black", "bold": True}  # 柱子边颜色
         }
    )
    worksheet.insert_chart("A11", chart)
    
    # 6) 插入本地图片(例如用matplotlib画的图)
    x = np.linspace(0, np.pi)
    y = np.sin(x)
    plt.plot(x, y, color='red', marker='+')
    plt.savefig('sin.png')  # 保存图片
    plt.show()
    worksheet.insert_image('D18', 'sin.png')
    workbook.close()


if __name__ == '__main__':
    file_name = "test.xlsx"
    write_excel_demo(file_name)
    data = read_data("data/score.txt")
    file_name = 'result.xlsx'
    write_excel(file_name, data)
