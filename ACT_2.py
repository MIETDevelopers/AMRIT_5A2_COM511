# using for loop
list=[1,3,5,7,9]
for i in list:
    print(i)

#using loop and range()
    list = [1, 3, 5, 7, 9]
# getting length of list
length = len(list)
# Iterating the index
for i in range(length):
     print(list[i])

# using while loop
list = [1, 3, 5, 7, 9]
# Getting length of list
length = len(list)
i = 0
# Iterating using while loop
while i<length:
  print(list[i])
  i+=1

# Using list comprehension (Possibly the most concrete way)
list = [1, 3, 5, 7, 9]
# Using list comprehension
[print(i) for i in list]


 #  Dictionary
# 1: Access key using the build .keys()
# Python code to iterate through all values in a dictionary
statesAndCapitals ={
'Gujarat':'Gandhinagar',
'Maharashtra': 'Mumbai',
'Rajasthan':'Jaipur',
'Bihar': 'Patna'
}
keys = statesAndCapitals.keys()
print(keys)


# 2: Access key without using a key()
# Python code to iterate through all keys in a dictionary
statesAndCapitals ={
'Gujarat':'Gandhinagar',
'Maharashtra': 'Mumbai',
'Rajasthan':'Jaipur',
'Bihar': 'Patna'
}
print('List Of given states:\n')

# Iterating over keys
for state in statesAndCapitals:
   print(state)

#    3: Iterate through all values using .values()
# Python code to iterate through all values in a dictionary
statesAndCapitals ={
'Gujarat':'Gandhinagar',
'Maharashtra': 'Mumbai',
'Rajasthan':'Jaipur',
'Bihar': 'Patna'
}
print('List Of given capitals:\n')
# Iterating over values
for capital in statesAndCapitals.values():
        print(capital)


# 4: Iterate through all key, and value pairs using items()
# Python code to iterate through all key, value pairs in a dictionary
statesAndCapitals ={
'Gujarat':'Gandhinagar',
'Maharashtra': 'Mumbai',
'Rajasthan':'Jaipur',
'Bihar': 'Patna'
}
print('List Of given states and their capitals:\n')
# Iterating over values
for state, capital in statesAndCapitals.items():
  print(state,":",capital)


#   5: Access both key and value without using items()
# Python code to iterate through all values in a dictionary
statesAndCapitals ={
'Gujarat':'Gandhinagar',
'Maharashtra': 'Mumbai',
'Rajasthan':'Jaipur',
'Bihar': 'Patna'
}
for i in statesAndCapitals:
    print(i,'->', statesAndCapitals[i])

# 6: Print items in Key-Value in pair
# Python code to iterate through all values in a dictionary
statesAndCapitals ={
'Gujarat':'Gandhinagar',
'Maharashtra': 'Mumbai',
'Rajasthan':'Jaipur',
'Bihar': 'Patna'
}
keys = statesAndCapitals.items()
print(keys)
