#Write a program to count the frequency of characters in a given file. 
#Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?



texto = open('ejer1.txt')


for c in texto:
    print(len(c))




