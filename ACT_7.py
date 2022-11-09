'''Purpose:Create a database using lists and tuples
Author:AMRIT PAL SINGH
'''

#Student data in database created using list and tuples
database=[('Ravi Kumar', 1, 'ravi@gmail.com', 'male', '8/17/07', 'jammu', '5th', 'A2', 1234567890), ('Rakesh Dev', 2, 'rakesh@gmail.com', 'male', '8/24/07', 'jammu', '2nd', 'A1', 9732145321), ('Salman', 3, 'salman@gmail.com', 'male', '4/17/07', 'delhi', '3rd', 'A1', 9563456728), ('Ajay', 4, 'ajay@gmail.com', 'male', '4/5/07', 'delhi', '6th', 'A1', 9287654320)]

def querying():
    print("Getting available information of student in database:\n")
    for idx,element in enumerate(database):
        print(f"name:{database[idx][0]}")
        print(f"rollno:{database[idx][1]}")
        print(f"email:{database[idx][2]}")
        print(f"gender:{database[idx][3]}")
        print(f"d.o.b:{database[idx][4]}")
        print(f"address:{database[idx][5]}")
        print(f"semester:{database[idx][6]}")
        print(f"section:{database[idx][7]}")
        print(f"phono:{database[idx][8]}\n")

querying()