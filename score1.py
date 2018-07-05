from sklearn.metrics import f1_score
import os
import csv


def get_score(true_file, predict_file):
    true = []
    predict = []
    result_content = csv.reader(open(predict_file))
    for row in result_content:
        predict.append(int(row[1]))
    csv_reader = csv.reader(open(true_file))
    for row in csv_reader:
        true.append(int(row[1]))
    if len(set(true)) <= 2:
        return f1_score(true,predict,average='binary')
    else:
        return f1_score(true,predict,average='weighted')


def start_score(root_dir):
    team_list = os.listdir(root_dir+'/result')
    team_id = []
    team_type = []
    team_score = []
    for team in team_list:
        true_file = root_dir+'true/true'+team[0]+'.csv'
        team_id.append(os.path.splitext(team)[0][2:])
        team_type.append(team[0])
        team_score.append(get_score(true_file, root_dir+'result/'+team))

    result_dict = list(zip(team_id, team_type,team_score))
    result_dict.sort(key=lambda x: x[2])
    result_dict.reverse()
    return result_dict

if __name__=='__main__':
    root_dir = '/Users/tree/Desktop/bigdata/'
    final_result = start_score(root_dir)
    with open("result.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(final_result)

