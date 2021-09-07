import os
import re
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import xlwt
import xlsxwriter

from matplotlib.font_manager import FontProperties


def generate_name(number, max_length_of_name):
  names = []
  ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for i in range(number):
    name = ''
    for j in range(max_length_of_name):
      name = name + random.choice(ascii_letters)
    names.append(name)
  return names


def generate_number(quantity, min_number, max_number):
  datas = []
  for i in range(quantity):
    datas.append(random.randint(min_number, max_number))
  return datas


def merge_data_by_map(data1, data2, head1, head2, data1_same_id, data2_same_id):
  datas = []
  dict_map = {}
  for i in range(len(data1)) :
    data = []
    for j in range(len(data1[i])):
      if j != data1_same_id :
        data.append(data1[i][j])
    dict_map[str(data1[i][data1_same_id])] = data

  for i in range(len(data2)):
    data = data2[i].copy()
    key = data[data2_same_id]
    if dict_map.get( key ) is not None:
      val = dict_map[key]
      for j in range(len(val)) :
        data.append(val[j])
      datas.append(data)
  return datas


def merge_data_by_pandas(data1, data2, head1, head2, data1_same_id, data2_same_id):
  df1 = pd.DataFrame(data1, columns=head1)
  df2 = pd.DataFrame(data2, columns=head2)
  #print(df1)
  #print(df2)
  key = head1[data1_same_id]
  df3 = pd.merge(df1, df2, how='inner', on=key)
  return df3


def write_excel(file_name, datas):
  workbook = xlsxwriter.Workbook(file_name)
  style = workbook.add_format({
      "fg_color": "yellow",  # background cloro
      "bold": 1,  
      "align": "center",  # 
      "valign": "vcenter",  # 
      "font_color": "red"  #
    })
  style_cen = workbook.add_format({
      "align": "center",  # 
      "valign": "vcenter",  # 
  })
  #style_pre = workbook.add_format({'num_format': '0.000%'})
  
  sheetname = "data"
  worksheet = workbook.add_worksheet(sheetname)  # 
  
  row, col = len(datas), datas.shape[1]
      
  head = [column for column in datas]
  worksheet.write_row('A1', head, style)
  worksheet.freeze_panes(1, 1)
  
  for i in range(row):
    for j in range(col):
      worksheet.write(i+1, j, datas.iloc[[i], [j]].values[0][0], style_cen)
    
  worksheet.set_column(0, col, 16)
  workbook.close()

def test_of_merge_data():
  Number = 1000
  names = generate_name(Number, 6)
  height = generate_number(Number, 150, 210)
  weight = generate_number(Number, 80, 250)

  Number_of_data1 = 100
  Number_of_data2 = 80
  data1 = []
  for i in range(Number_of_data1):
    id = random.randint(0, Number-1)
    data = [names[id], height[id]]
    data1.append(data)

  data2 = []
  for i in range(Number_of_data2):
    id = random.randint(0, Number-1)
    data = [names[id], weight[id]]
    data2.append(data)

  #print("data1")
  #print(data1)
  #print("data2")
  #print(data2)

  datas = merge_data_by_map(data1, data2, ["name", "height"], ["name", "weight"], 0, 0)
  print("\n")
  print("datas")
  print(datas)

  df = merge_data_by_pandas(data1, data2, ["name", "height"], ["name", "weight"], 0, 0)
  print("df")
  print(df)

  write_excel("data.xlsx", df)


if __name__ == "__main__":
  test_of_merge_data()
