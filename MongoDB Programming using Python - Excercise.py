#Exercise
"""
Use the following database and collection in your local server.
"""
#Database: Demo

#Collection: Employee
 
'''
1. Write a Python program to insert the following data into the collection Employee.
'''
# importing class "MongoClinet" from the driver "pymongo"
from pymongo import MongoClient

# Connecting to the MongoDB database (or) Establishing MongoDB connection:
conn_obj = MongoClient('mongodb://localhost:27017/')
# conn_obj = MongoClient('localhost','27017')

print(type(conn_obj))

# Selecting a database
database_obj = conn_obj['Demo']
# database_obj = conn_obj.Demo

# Selecting a Collection
collection_obj = database_obj['Employee']
# collection_obj = database_obj.Employee

print(collection_obj)

document_list = [ {'EmpId':1,'Name':'Tim','Dept':'ETA','Salary':21990},
                  {'EmpId':2,'Name':'John','Dept':'ADM','Salary':22900},
                  {'EmpId':3,'Name':'James','Dept':'FIN','Salary':28100},
                  {'EmpId':4,'Name':'Robert','Dept':'ETA','Salary':100000} ]

returnval = collection_obj.insert_many(document_list)

print(returnval.inserted_ids)

'''
2. Write a Python program to display the details of employees earning more than 25000
'''
from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')    # (or) conn_obj = MongoClient('localhost','27017')
database_obj = conn_obj['Demo']                         # (or) database_obj = conn_obj.Demo
collection_obj = database_obj['Employee']               # (or) collection_obj = database_obj.Employee
print("Displaying the details of employees earning more than 25000:")
docs = collection_obj.find({'Salary':{'$gt':25000}})
for doc in docs:
    print(doc)
    
'''
3. Write a Python program to display the details of the employees whose names start with 'J' or whose dept has 'A'.
'''
from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')    
database_obj = conn_obj['Demo']                         
collection_obj = database_obj['Employee']               
print("Displaying the details of employees whose names start with 'J' or whose dept has 'A':")
doc1 = collection_obj.find({'Name':{'$regex': '^J'}})
doc2 = collection_obj.find({'Dept':{'$regex': '+A'}})
for doc in (doc1 or doc2):
    print(doc)
    
'''
4. Write a Python program to update the dept of John as "DNA".
'''
from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')    
database_obj = conn_obj['Demo']                         
collection_obj = database_obj['Employee']               
print("update the dept of John as 'DNA':")
collection_obj.update_one({'Name':'John'},{'$set':{'Dept':'DNA'}})
docs = collection_obj.find({'Name':'John'})
for doc in docs):
    print(doc)
    
'''
5. Write a Python program to delete the document ​​​​​​of Robert.
'''
from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')    
database_obj = conn_obj['Demo']                         
collection_obj = database_obj['Employee']               
print("update the dept of John as 'DNA':")
collection_obj.delete_one({'Name':'Robert'})
docs = collection_obj.find({})
for doc in docs:
    print(doc)
    
'''
6. Write a Python program which displays the following menu and seeks the user input up on its execution

Add a new employee

Update salary of an employee

Remove an employee 

Display an employee

Rules: 

If 1 is selected, take the employee details from the standard input, and insert a new document
If 2 is selected, input the employee id and the latest salary. Update the corresponding document
If 3 is selected, input the employee ID, and delete the corresponding document
If 4 is selected, input the employee ID, and display the corresponding document
For any other input, display all the employee documents
Note: Display respective error messages wherever needed.
'''
from pymongo import MongoClient
conn_obj = MongoClient('mongodb://localhost:27017/')    
database_obj = conn_obj['Demo']                         
collection_obj = database_obj['Employee']

print("Before Operation:")
docs = collection_obj.find()
for doc in docs:
    print(doc)
    
print("MENU:\n1.Add a new Employee\n2.Update salary of an Employee\n3.Remove an Employee\n4.Display an Employee")
inp = input("Please Enter the number to select an option:\n")
inp = int(inp)
if inp == 1:
    print("1.Adding a new Employee:")
    eid = input("Enter Employee ID: ")
    ename = input("Enter Employee Name: ")
    dept = input("Enter Employee Department Name: ")
    salary = input("Enter Employee Salary: ")
    last_row = collection_obj.find_one({}, { 'Name': 0 ,'Dept': 0 , 'Salary' : 0 }).sort( 'EmpId',-1 ).limit(1)
    last_eid = last_row['EmpId']
    document = { 'EmpId': int(last_eid)+1 , 'Name': ename ,'Dept': dept , 'Salary' : int(salary) }
    returnval = collection_obj.insert_one(document)
    print(returnval.inserted_id)
elif inp == 2:
    print("2.Updating salary of an Employee:")
    eid = input("Enter Employee ID: ")
    salary = input("Enter Employee Salary: ")
    returnval = collection_obj.update_one( {'EmpId': int(eid)},{ '$set' : { 'Salary' : int(salary) } } ) 
elif inp == 3:
    print("3.Deleting an Employee:")
    eid = input("Enter Employee ID: ")
    returnval = collection_obj.delete_one( {'EmpId': int(eid)} )
elif inp == 4:
    print("4.Displaying an Employee:")
    eid = input("Enter Employee ID: ")
    returnval = collection_obj.find_one( {'EmpId': int(eid)} )
    # returnval = collection_obj.find( {'EmpId': int(eid)} )
    print(returnval)
else:
    print("Others:")
    returnval = collection_obj.find()
    for val in returnval:
        print(val)
    
print("After Operation:")
docs = collection_obj.find()
for doc in docs:
    print(doc)
