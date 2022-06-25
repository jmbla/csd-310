from pymongo import MongoClient

url = 'mongodb://admin:admin@ac-um0ozvv-shard-00-00.dlvbmu8.mongodb.net:27017,ac-um0ozvv-shard-00-01.dlvbmu8.mongodb.net:27017,ac-um0ozvv-shard-00-02.dlvbmu8.mongodb.net:27017/?ssl=true&replicaSet=atlas-4dykia-shard-0&authSource=admin&retryWrites=true&w=majority';

client = MongoClient(url)

db = client.pytech

students = db['students']


print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for docs in students.find({}):
    print("Student ID: ", docs["student_id"])
    print("First Name:", docs["first_name"])
    print("Last Name:", docs["last_name"])
    print()

docs = students.find_one({"student_id": "1008"})
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student ID: ", docs["student_id"])
print("First Name:", docs["first_name"])
print("Last Name:", docs["last_name"])

docs = db.students.find({"student_id": "1008"})
print(docs)

print(students.find_one({"student_id": "1008"}))
