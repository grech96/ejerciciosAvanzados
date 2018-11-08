import os

f=os.listdir()
lista=[]
dic={}

for i in f:
    x=i.find('.')
    lista.append(i[x+1:])
    #print(i)

for j in lista:
    dic[j]=dic.get(j,0)+1
    #print(j)

for key,value in dic.items():
    print(value,'archivos','con extencion .',key)


    
