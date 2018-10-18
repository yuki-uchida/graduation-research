import pandas as pd
import re
import numpy as np
df = pd.read_csv('comment.csv',encoding='cp932')
comment_list = []
columns = []
column_num = 1
for review in df["0"]:
  context = review.replace('\n','')
  context = context.replace('\r','')
  context = [i for i in re.split('。',context) if i != '']
  for comment in context:
    if (len(list(comment)) >= 20) and (len(list(comment)) <= 70):
      comment_list.append(comment)
      if column_num <= 50:
        columns.append("##{}##".format(column_num))
        column_num = column_num + 1
new_list = []
new_list.append(columns)
while len(comment_list) >= 1:
  new_list.append(comment_list[0:50])
  del(comment_list[0:50])

new_list = np.array(new_list).reshape((1,7))

for row in new_list[0]:
  try:
    df2 = df2.append(pd.DataFrame(row).T)
  except NameError:
    df2 = pd.DataFrame(row).T

# print(df2)
df2.to_csv('comment_cw.csv',header=False,index=True,encoding='cp932')




import csv
csv_file = open("comment_cw.csv", "r", encoding="cp932", errors="", newline="" )
csv_reader = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
output_csv = open('some.csv', 'w', encoding="cp932")
writer = csv.writer(output_csv, lineterminator='\n')

first_line = True
for line in csv_reader:
  line.insert(1,"80")
  writer.writerow(line)

# writer.writerow(list)
# writer.writerows(array2d)

# f.close()

















