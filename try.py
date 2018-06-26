import json
import xlwt
from collections import OrderedDict

def script_analyse(originFile, targetFile):
    fileopen = open(originFile, 'r')
    file_content = fileopen.readlines()
    list_block = []
    list_temp = []
    for count, line in enumerate(file_content):
        line = line.strip()
        if line == '"apps": [':
            if len(list_temp) != 0:
                list_block.append(list_temp)
            list_temp = []
            list_temp.append(count+1)
        if line == '"versionInfo": {':
            list_temp.append(count + 4)
    list_block.append(list_temp)
    print('apps 个数：',len(list_block))
    final_result = []
    for item in list_block:
        for num in range(len(item)-1):
            final_result.append(get_json(item[num], item[num+1], file_content))
            item[num+1] = item[num+1] + 1
    print('共有记录个数', len(final_result))
    write_excel(final_result, targetFile)


# 将数据转换成json字典格式，返回值是转换后的字典


def get_json(start_num, end_num, file_content):
    dict_content = ''
    for count, line in enumerate(file_content):
        if count == end_num:
            line = line.replace(',', '')
        if count >= start_num and count <= end_num:
            dict_content = dict_content + line.strip()
    # json_content = json.loads(dict_content,object_pairs_hook=OrderedDict)
    json_content = json.loads(dict_content)
    return json_content


# 写入excel文件


def write_excel(final_result, targetFile):

    title = list(final_result[0])
    title.sort()

    book = xlwt.Workbook()  # 创建一个excel对象
    sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)  # 添加一个sheet页
    for i in range(len(title)):  # 循环列
        sheet.write(0, i, title[i])  # 将title数组中的字段写入到0行i列中
    for row_excel, item in enumerate(final_result):  # 循环列表，取出每一个记录的参数
        for col_excel, title_name in enumerate(title):  # 循环列表
            sheet.write(row_excel+2, col_excel, str(item[title_name]))  # 将信息写入
    book.save(targetFile)  # 保存excel


if __name__ == '__main__':
    originFile = 'uip.txt'
    targetFile = 'task1.xls'
    script_analyse(originFile, targetFile)
