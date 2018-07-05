from sklearn.metrics import f1_score
import os
import operator
import csv
root_dir = '/Users/tree/Desktop/bigdata'

userid = []
true = []
csv_reader = csv.reader(open('/Users/tree/Desktop/bigdata/true.csv'))
for row in csv_reader:
    userid.append(row[0])
    true.append(int(row[1]))


team_list = os.listdir(root_dir)
teamid = []
teamscore = []

for team in team_list:
    predict = []
    if team != 'true.csv':
        teamid.append(os.path.splitext(team)[0])
        file_path = os.path.join(root_dir, team)
        result_content = csv.reader(open(file_path))
        for row in result_content:
            predict.append(int(row[1]))
        if len(set(predict) <= 2):
            teamscore.append(f1_score(true, predict, average='binary'))
        else:
            teamscore.append(f1_score(true, predict, average='weight'))
for i in range(len(teamid)):
    print('id =', teamid[i], '| f1score =', teamscore[i])

result_dict = dict(zip(teamid, teamscore))
print(result_dict)
result_sort = sorted(result_dict.items(), key=operator.itemgetter(1))
with open("result.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(result_sort)


#

# for result in result_sort:
#     print(type(result),result)
# # print(type(result_dict))
# # print(result_dict)