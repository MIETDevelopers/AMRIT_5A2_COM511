# count no.of alphabets in the given string
a="Welcome to python programming"
count=0
for i in a:
    if(i.isalpha()):
        count=count+1
print("number of alphabets: ",count)     

# check if the string is alphanumeric or not
s='HelloWorld2002'
print(s.isalnum())

# to extract characters in the given string
a="Welcome to python programming"
st=int(input("enter starting range: "))
en=int(input("enter ending range: "))
print(a[st:en])
