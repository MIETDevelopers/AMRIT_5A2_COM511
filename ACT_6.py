'''Purpose:Write a program to create a list of student’s records and search a student record using a dictionary.
Author:AMRIT PAL SINGH
'''
print("-----Program for Student Information-----")
 
D = dict()
n = int(input('How many student record you want to store?? '))
 
for i in range(0,n):
    x, y = input("Enter the complete name (First and last name) of student: ").split()
    z = input("Enter contact number: ")
    m = input('Enter Marks: ')
    D[x, y] = (z, m)


def searchdetail(fname):
    ls = list()
     
    for sname,details in D.items():
        tup=(sname,details)
        ls.append(tup)

    for i in ls:
        count=0
        if i[0][0] == fname:
            print(i[1][0])
            count=count+1
    if count==0:
        print("Not found")

def option():
   
    print('1: Search contact number using first name')
    print('2: Exit')
    choice = int(input('Choose the operation:')) 

    if choice == 1:
        first = input('Enter first name of student: ')
        searchdetail(first)
        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y':
            option() 
    else:
        exit()

option()