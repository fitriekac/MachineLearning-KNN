
# coding: utf-8

# In[ ]:


import csv
import math
import collections

def ambilDataTest():
    with open('DataTest_Tugas3_AI.csv') as file:
        reader = csv.reader(file, delimiter=',')
        data = []
        next(reader)
        for row in reader:
            data.append([float(row[1]), float(row[2]),float(row[3]), float(row[4]), float(row[5])])
        return data


def ambilDataTrain():
    with open('DataTrain_Tugas3_AI.csv') as file:
        reader = csv.reader(file, delimiter=',')
        data = []
        next(reader)
        for row in reader:
            data.append([float(row[1]), float(row[2]),float(row[3]), float(row[4]), float(row[5]), float(row[6])])
        return data
    
def simpan(hasil):
    with open('TebakanTugas3.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for h in hasil:
            writer.writerow([h])

def hitungjarak(pos1, pos2):
    a = (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2 + (pos1[2] - pos2[2])**2 + (pos1[3] - pos2[3])**2 + (pos1[4] - pos2[4])**2
    return math.sqrt(a)


def bubbleSort(arr, kelas):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                kelas[j], kelas[j + 1] = kelas[j + 1], kelas[j]
    return kelas

data_train = ambilDataTrain()
data_test = ambilDataTest()
K = 7
prediksi = []
for d_test in data_test:
    dist = []
    kelas = []
    for d_train in data_train:
        dist.append(hitungjarak(d_test, d_train))
        kelas.append(int(d_train[5]))
    kelas = bubbleSort(dist, kelas)
    kelas = kelas[:K]
    counter = collections.Counter(kelas)
    hasil = counter.most_common(1)[0][0]
    print(hasil)
    prediksi.append(hasil)
simpan(prediksi)


# In[ ]:





# In[ ]:




