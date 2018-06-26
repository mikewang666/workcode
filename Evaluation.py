# -*- coding: utf8 -*-


import xlwt, xlrd

item_name = ['id', 'cmd', 'args', 'user', 'env', 'instances', 'cpus', 'mem',
                 'disk', 'gpus', 'executor', 'uris', 'fetch','storeUrls','backoffSeconds',
                 'backoffFactor', 'maxLaunchDelaySeconds', 'healthChecks', 'readinessChecks'
                 , 'dependencies', 'labels', 'ipAddress', 'version', 'residency', 'secrets',
                 'taskKillGracePeriodSeconds', 'requirePorts']
row_excel = 0

def clear_format(str1):
    str2 = str1.replace(',', '')
    str3 = str2.replace('"', '')
    return str3.strip()


def script_analyse(originFile, targetFile):

    fileOpen = open(originFile, 'r')
    filecontent= fileOpen.readlines()


    list_start = []
    list_block = []
    list_temp = []
    for count,line in enumerate(filecontent):
        line = line.strip()
        if line == '"apps": [':
            if len(list_temp) != 0:
                list_block.append(list_temp)
            list_start.append(count+1)
            list_temp = []
            list_temp.append(count+1)
        if line == '"versionInfo": {':
            list_temp.append(count+3)
    list_block.append(list_temp)
    print(len(list_block), list_block)
    row_num = 1

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    for number,item in enumerate(item_name):
        worksheet.write(0,number,item)
    for k in range(len(list_block)):
        result_temp = get_result(list_block[k], filecontent)
        write_excel(worksheet,result_temp)
        workbook.save(targetFile)


def get_result(num_block,filecontent):
    result = []
    dict1 = {}

    for i in range(len(num_block) - 1):
        print('正在第', num_block[i])
        for line_num in range(num_block[i], num_block[i + 1]):
            line_split = filecontent[line_num].strip().split(':')
            for key, content in enumerate(line_split):
                for item in item_name:
                    if clear_format(content) == item:
                        dict1.update({item: clear_format(line_split[key + 1])})

        result.append(dict1)
        dict1 = {}

    return result

def write_excel(worksheet,list_result):
    global row_excel
    for item_result in list_result:
        row_excel += 1
        print(row_excel)
        for number, item in enumerate(item_name):
            worksheet.write(row_excel, number, item_result[item])





# 写入excel
'''col_excel = 0
    for num in range(len(list_start)):
        line_num = list_start[num]
        print(num)
        while line_num <= list_end[num][-1]:
            col_excel += 1
            line_split = filecontent[line_num].split(':')
            row_excel = 0
            for i in range(len(line_split)):
                content = line_split[i]
                convert = content.replace(',', '')
                convert1 = convert.replace('"', '')
                worksheet.write(col_excel, row_excel, convert1)
                row_excel += 1
                workbook.save(targetFile)
            line_num += 1
'''





if __name__ == '__main__':
    sheetName = 'sheet1'
    originFile = r"uip.txt"
    targetFile = 'Task1.xls'
    script_analyse(originFile, targetFile)


