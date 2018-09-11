import csv
import pandas as pd
count = 0
e_count = 0
f_count = 0
ef_count = 0
fa_count = 0
fc_count = 0
df = pd.DataFrame.from_csv("DATAset/la-county-restaurant-inspections.csv")
f =open("DATAset/la-county-restaurant-inspections.csv")
csv_reader = csv.reader(f)
for line in csv_reader:

    count+=1
    if line[2] == "17660 CHATSWORTH ST":
        fa_count+=1
    if line[3] == "LANCASTER":
        fc_count+=1
    if line[1] == "EE0000145":
        e_count+=1
    if line[4] == "FA0013858":
        f_count+=1
    if line[1] == "EE0000593" and line[3] == "GRANADA HILLS""":
        ef_count+=1

print("facility address 17660 CHATSWORTH ST is visited "+str(fa_count))
print("LANCASTER visited "+str(fc_count))


e_percentage = 0
f_percentage = 0
ef_percentage = 0

e_percentage = (e_count/count)*100
f_percentage = (f_count/count)*100
ef_percentage = (ef_count/count)*100
score_mean = df["score"].mean()

print("The average score of the LA County Resturant Inspections is: " +str(score_mean) )

print(" percentage of times that employee EE0000145 visit any facility is: "+str(e_percentage)+"%")
print(" percentage of times that facility FA0013858 is visited is: "+str(f_percentage)+"%")
print(" percentage of times that employee EE0000593 visit GRANADA HILLS is: "+str(ef_percentage)+"%")

