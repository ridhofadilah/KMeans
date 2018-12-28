
# coding: utf-8

# Sayid Muhamad Ridho Fadilah
# 1301154312
# IF3904

# In[99]:


#library yang diperlukan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import random


# In[100]:


#load data train
dataTrain = pd.read_csv('TrainsetTugas2.txt', delimiter = "\t")
print (dataTrain)


# In[101]:


#plot data train
plt.plot(dataTrain["x1"], dataTrain["x2"], "o")


# In[102]:


#inisialisasi nilai K (jumlah cluster) dan nilai centroid (x,y)
clusterSet = []
K = 7
for i in range (K):
    x1 = random.uniform(3,40) #dari data yang di plot, range nilai x dari 3 sampai 40
    x2 = random.uniform(1,30) #dari data yang di plot, range nilai y dari 1 sampai 30
    x = [x1,x2]
    clusterSet.append(x)
    
print (clusterSet)


# In[120]:


#fungsi bersihin data. ngehilangin nilai x1 dan x2 dan membuat tipenya menjadi float
def dataClean(data):
    hasilData=[]
    for i in range(data.shape[1]):
        a = i+1
        b = "x"+str(a) #menggabungkan nilai dengan nilai x
        hasilData.append(float(data[b])) #membuat menjadi float
    return hasilData


# In[104]:


#mencari jarak centroid dengan data
def euclideanDistance(data1, data2):
    hasil = 0
    for i in range(len(data1)):
        hasil += (data1[i]-data2[i])**2
    return hasil ** 0.5


# In[105]:


#cluster pertama kali
indexCluster = [[],[],[],[],[],[],[]] #menyimpan index data yang di cluster
nilaiCluster = [[],[],[],[],[],[],[]] #menyimpan nilai x1,x2 data yang di cluster
for i in range(dataTrain.shape[0]):
    data = dataClean(dataTrain[i:i+1])
    print ("data ke-",i)
    minimum = euclideanDistance(data,clusterSet[0]) #menginisialisasi nilai minimum
    clusterr = 0 #menginisialisasi index minimum berada pada cluster apa
    print ("cluster 0 : ",euclideanDistance(data,clusterSet[0]))
    for j in range(1,K):
        print ("cluster",j,": ",euclideanDistance(data,clusterSet[j]))
        if (euclideanDistance(data,clusterSet[j]) < minimum): #jika nilai baru yang dievaluasi lebih kecil maka
            minimum = euclideanDistance(data,clusterSet[j]) #nilai minimum akan di update
            clusterr = j #nilai cluster akan diupdate
    print ("minimum : ", minimum, " pada cluster ", clusterr, "\n")
    indexCluster[clusterr].append(i) #menyimpan index data yang jaraknya paling kecil ke cluster
    nilaiCluster[clusterr].append(data) #menyimpan nilai x1,x2 data yang jaraknya paling kecil ke cluster


# In[106]:


#evaluasi centroid
def ratarata(nilai):
    hasil = []
    for j in range(len(nilai[0])): #dari index 0 sampe panjangnya nilai
        total = 0
        for i in range(len(nilai)): #akan diulang dari index 1 data sampe data terakhir
            total += nilai[i][j] #jika j = 0 maka nilai x yang ditambah, jika j = 1 maka nilai y yang ditambah
        hasil.append(total/(len(nilai))) #rata rata hasilnya dan dimasukkan ke list baru
    return hasil #mengembalikan list tersebut/centroid yang telah terupdate


# In[107]:


#update centroid
for h in range (100): #update centroid akan diulang sebanyak 100 kali
    print (h)
    indexCluster = [[],[],[],[],[],[],[]] #menyimpan index data yang di cluster
    nilaiCluster = [[],[],[],[],[],[],[]] #menyimpan nilai x1,x2 data yang di cluster
    for i in range(dataTrain.shape[0]):
        data = dataClean(dataTrain[i:i+1])
        minimum = euclideanDistance(data,clusterSet[0]) #menginisialisasi nilai minimum
        clusterr = 0 #menginisialisasi index minimum berada pada cluster apa
        for j in range(1,K):
            if (euclideanDistance(data,clusterSet[j]) < minimum): #jika nilai baru yang dievaluasi lebih kecil maka
                minimum = euclideanDistance(data,clusterSet[j]) #nilai minimum akan di update
                clusterr = j #nilai cluster akan diupdate
        indexCluster[clusterr].append(i) #menyimpan index data yang jaraknya paling kecil ke cluster
        nilaiCluster[clusterr].append(data) #menyimpan nilai x1,x2 data yang jaraknya paling kecil ke cluster
    #update semua centroid
    for i in range(0,K):
        clusterSet[i] = ratarata(nilaiCluster[i])


# In[108]:


total = 0
for i in range (K):
    print ("isi index cluster",i)
    print (indexCluster[i])
    print ("jumlah: ",len(indexCluster[i]),"\n")
    total+= len(indexCluster[i])

print ("total data", total)


# In[109]:


#cluster 0 warna biru
#cluster 1 warna oren
#cluster 2 warna hijau
#cluster 3 warna merah
#cluster 4 warna ungu
#cluster 5 warna coklat
#cluster 6 warna pink
#centroid warna abuabu
#plot data train yang telah di clusterisasi
for i in range(K):
    print ("cluster",i)
    x1 = [nilaiCluster[i][j][0] for j in range(len(indexCluster[i]))] #mengambil nilai x1 pada setiap cluster
    x2 = [nilaiCluster[i][j][1] for j in range(len(indexCluster[i]))] #mengambil nilai x2 pada setiap cluster
    plt.plot(x1, x2, "o")
    plt.axis([0, 40, 0, 30]) #setting range nilai curva
    
x1 = [clusterSet[i][0] for i in range(K)] #ambil nilai x1 pada setiap centroid
x2 = [clusterSet[i][1] for i in range(K)] #ambil nilai x2 pada setiap centroid
plt.plot(x1, x2, "o")
plt.axis([0, 40, 0, 30]) #setting range nilai curva


# In[110]:


print (clusterSet)


# In[111]:


#load data test
dataTest = pd.read_csv('TestsetTugas2.txt', delimiter = "\t")
print (dataTest)


# In[115]:


#clusterisasi data test terhadap nilai centroid yang telah dievaluasi
indexCluster = [[],[],[],[],[],[],[]] #menyimpan index data yang di cluster
nilaiCluster = [[],[],[],[],[],[],[]] #menyimpan nilai x1,x2 data yang di cluster
hasil=[] #menyimpan hasil clusterisasi
for i in range(0,dataTest.shape[0]):
    data = dataClean(dataTest[i:i+1])
    print ("data ke-",i+1)
    minimum = euclideanDistance(data,clusterSet[0]) #menginisialisasi nilai minimum
    clusterr = 0 #menginisialisasi index minimum berada pada cluster apa
    print ("cluster 0 : ",euclideanDistance(data,clusterSet[0]))
    for j in range(1,K):
        print ("cluster",j,": ",euclideanDistance(data,clusterSet[j]))
        if (euclideanDistance(data,clusterSet[j]) < minimum): #jika nilai baru yang dievaluasi lebih kecil maka
            minimum = euclideanDistance(data,clusterSet[j]) #nilai minimum akan di update
            clusterr = j #nilai cluster akan diupdate
    print ("minimum : ", minimum, " pada cluster ", clusterr, "\n")
    indexCluster[clusterr].append(i) #menyimpan index data yang jaraknya paling kecil ke cluster
    nilaiCluster[clusterr].append(data) #menyimpan nilai x1,x2 data yang jaraknya paling kecil ke cluster
    hasil.append(clusterr) #mengisi data ke i masuk ke cluster mana


# In[116]:


for i in range (K):
    print ("cluster",i,"\n- index-nya :\n",indexCluster[i])
    print ("- nilai-nya :\n",nilaiCluster[i])
    print ("jumlah :", len(indexCluster[i]),"\n")


# In[117]:


#plot persebaran data train dan data test
plt.plot(dataTrain["x1"], dataTrain["x2"], "o") #warna biru
plt.plot(dataTest["x1"], dataTest["x2"], "o") #warna oren


# In[118]:


#cluster 0 warna biru
#cluster 1 warna oren
#cluster 2 warna hijau
#cluster 3 warna merah
#cluster 4 warna ungu
#cluster 5 warna coklat
#cluster 6 warna pink
#plot hasil data persebaran data test yang telah di clustering
for i in range(K):
    print ("cluster",i)
    x1 = [nilaiCluster[i][j][0] for j in range(len(indexCluster[i]))]#mengambil nilai x1 pada setiap cluster
    x2 = [nilaiCluster[i][j][1] for j in range(len(indexCluster[i]))] #mengambil nilai x2 pada setiap cluster
    plt.plot(x1, x2, "o")
    plt.axis([0, 40, 0, 30]) # set nilai range curva


# In[119]:


#membuat file txt
output = dataTest
output['label'] = hasil #output menambahkan kolom baru berupa label dimana isinya adalah hasil dari clustering
output.to_csv('prediksi.txt', header=True, index=False, sep='\t', mode='a') #membuat file baru yang bernama prediksi.txt

