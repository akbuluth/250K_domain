import sys
import glob
import datetime
date = datetime.datetime.now()

directory = sys.argv[1]
all_files = glob.glob(directory+"/*.log")
result = {}

for each_file in all_files:
    file = open(each_file)
    all_lines = file.readlines()

    for each_line in all_lines:
        temp = each_line.split("|")
        if result.get(temp[0]):
            try:
                result[temp[0]] += int(temp[1])
            except:
                continue
        else:
            try:
                result[temp[0]] = int(temp[1])
            except:
                continue
    file.close()

sorted_result_list = sorted(result.items(), key=lambda x:x[1], reverse=True)
result = dict(sorted_result_list[:250000])


final = open("file_name"+date.strftime("%Y%m%d")+".txt", "w")

for i in result:
    final.write(i + "|" + str(result[i]) + "\n")

final.close()