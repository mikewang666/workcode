# -*- coding: utf8 -*-
import csv
import datetime


file1 = open('history_result.csv')
file2 = open('result.csv')
result_content_old = csv.reader(file1)
result_content_new = csv.reader(file2)
result_history = list(result_content_old)
result_new = list(result_content_new)
file1.close()
file2.close()


# 备份前一天的成绩
cur=datetime.datetime.now()
filename = str(cur.year)+'-'+str(cur.month)+'-'+str(cur.day)
with open(filename+"-bak.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(result_history)

# 提取有历史成绩的队伍名
team_id =[]
for team in result_history:
    team_id.append(team[0])


# 更新数据，如果没有该队伍，添加该队伍成绩
for team in result_new:
    if team[0] not in team_id:
        result_history.append(team+[team[2]]+[0])
        print('Name:', team[0], ' has been added.')
    else:
        num = team_id.index(team[0])
        if result_history[num][2] != team[2]:
            result_history[num][2] = team[2]
            print('Name:', team[0], '. Their today score has update')
        if result_history[num][3] < team[2]:
            result_history[num][3] = team[2]
            print('Name:', team[0], '. Their best score has update ')


result_history.sort(key=lambda x: x[3])
result_history.reverse()
result_sorted = []
for i in range(len(result_history)):
    result_history[i][4] = i+1

with open("history_result.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(result_history)