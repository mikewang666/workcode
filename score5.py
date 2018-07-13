from sklearn.metrics import f1_score
import os
import csv


def get_score1(question_type,true_file, predict_file):
    true = []
    predict = []
    result_content = csv.reader(open(predict_file))
    for row in result_content:
        predict.append(int(row[1]))
    csv_reader = csv.reader(open(true_file))
    for row in csv_reader:
        true.append(int(row[1]))
    if question_type <= 3:
        return f1_score(true,predict,average='binary')
    else:
        return f1_score(true,predict,average='weighted')


def get_score5(true_file1,true_file2,predict_file1,predict_file2):
    true1 = []
    predict1 = []
    csv_reader = csv.reader(open(true_file1))
    for row in csv_reader:
        true1.append(row[1])
    result_content = csv.reader(open(predict_file1))
    for row in result_content:
        predict1.append(row[1])
    count = 0
    for i in range(len(true1)):
        if true1[i] == predict1[i]:
            count = count + 1
    P = count / len(true1)

    true_gender =[]
    true_age = []
    gender = []
    age = []
    csv_reader = csv.reader(open(true_file2))
    for row in csv_reader:
        true_gender.append(int(row[1]))
        true_age.append(int(row[2]))

    result_content = csv.reader(open(predict_file2))
    for row in result_content:
        gender.append(int(row[1]))
        age.append(int(row[2]))

    count_gender = 0
    count_age = 0
    for i in range(len(true_age)):
        if true_gender[i]== gender[i]:
            count_gender += 1
        count_age = count_age + (25/(25+(true_age[i]-age[i])**2))

    Q1 = count_gender/len(true_gender)
    Q2 = count_age/len(true_age)
    Q = (Q1+Q2)*0.5

    final_score = (P+Q)*0.5
    return final_score


def start_score(root_dir):
    team_list = os.listdir(root_dir+'/result')
    team_id = []
    team_type = []
    team_score = []
    for team in team_list:
        question_type = int(team[0])


        if(question_type<5):
            team_type.append(question_type)
            true_file = root_dir + 'true/' + team[0] + '_true' + '.csv'
            predict_file = root_dir+'result/'+team
            team_id.append(os.path.splitext(team)[0][2:])
            team_score.append(get_score1(question_type,true_file, predict_file))

        if(question_type==5):
            if team[1] == '1':
                team_type.append(question_type)
                teamname = os.path.splitext(team)[0][3:]
                team_id.append(teamname)
                true_file1 = root_dir + 'true/51_true.csv'
                true_file2 = root_dir+'true/52_true.csv'
                predict_file1 = root_dir + 'result/51_' + teamname + '.csv'
                predict_file2 = root_dir + 'result/52_' + teamname + '.csv'
                team_score.append(get_score5(true_file1,true_file2,predict_file1,predict_file2))
            else:
                print(team,'is not team key')

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

