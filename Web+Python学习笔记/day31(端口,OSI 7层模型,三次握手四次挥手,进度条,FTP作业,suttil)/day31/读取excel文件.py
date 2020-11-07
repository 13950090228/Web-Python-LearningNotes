## -*- coding: utf-8 -*-
#"""
#Created on Wed Nov 20 15:36:17 2019
#
#@author: 50671
#"""
#
#import os
##username='liuyongqi'
##file_name='2.txt'
##path=os.path.join('home',username,file_name)
##print(path)
##with open('a.txt',mode='w') as f:
##    f.write(file_name)
#exist = os.path.exists(r'C:\Users\50671\Desktop\11.jpg')   
#print(exist) 

import xlrd

#导入需要读取的第一个Excel表格的路径
data1 = xlrd.open_workbook(r'C:\Users\50671\Desktop\乱七八糟的文件\17电子信息工程（闽台合作）.xlsx')
table = data1.sheets()[0]
#创建一个空列表，存储Excel的数据
tables = []
#将excel表格内容导入到tables列表中
def import_excel(excel):
  for rown in range(excel.nrows):
   array = {'class':'','name':'','timeline':'','stage':''}
   array['class'] = table.cell_value(rown,0)
   array['name'] = table.cell_value(rown,1)
#   if table.cell(rown,2).ctype == 3:
#     date = xldate_as_tuple(table.cell(rown,2).value,0)
   array['timeline'] = table.cell_value(rown,2)
   array['stage'] = table.cell_value(rown,3)

   tables.append(array)
if __name__ == '__main__':
  #将excel表格的内容导入到列表中
  import_excel(table)
  for i in tables:
    print(i)
   
   
   