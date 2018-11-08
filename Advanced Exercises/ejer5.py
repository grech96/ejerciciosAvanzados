#Write a program extcount.py to count the number of files for each extension in the given directory. 
#The program should take a directory name as argument and print count and extension for each available file extension.

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
