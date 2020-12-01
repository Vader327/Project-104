from collections import Counter
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
n = len(data)
total = 0
new_data=[]

for i in data:
        total += float(i[2])
        new_data.append(float(i[2]))
new_data.sort()

mean = total / n
print("Mean: " + str(mean))

if n % 2 == 0:
        median = (float(new_data[n//2]) + float(new_data[n//2 - 1])) / 2
else:
        median = float([n/2])
print("Median: " + str(median))

dictn = {}
for i in new_data:
        dictn[i] = 0

data1 = Counter(new_data)
for i, occ in data1.items():
        dictn[i] += occ

temp_arr = []
temp_occ = 0
for i, occ in dictn.items():
        if occ > temp_occ:
                temp_occ = occ
                temp_arr.append(i)
                
print("Mode: " + str(temp_arr[-1]))
