import json

from collections import OrderedDict


originFile = 'uip.txt'

fileOpen = open(originFile, 'r')
file_content = fileOpen.readlines()
dict_content = ''

for count, line in enumerate(file_content):
    if count == 79:
        line = line.replace(',','')
    if count >10 and count<80:
        dict_content = dict_content + line.strip()

json_content = json.loads(dict_content, object_pairs_hook=OrderedDict)
print(type(dict(json_content)))
for item in json_content:
    print(item)
print(list(json_content))
print(type(json.dumps(json_content)))
with open('result1.txt', 'w') as file1:
    file1.write(dict_content)
    file1.write('\n')
    file1.write('\n')
    file1.write(json.dumps(json_content))
file1.close()