
from pymongo import MongoClient

url = 'mongodb://admin:admin@ac-um0ozvv-shard-00-00.dlvbmu8.mongodb.net:27017,ac-um0ozvv-shard-00-01.dlvbmu8.mongodb.net:27017,ac-um0ozvv-shard-00-02.dlvbmu8.mongodb.net:27017/?ssl=true&replicaSet=atlas-4dykia-shard-0&authSource=admin&retryWrites=true&w=majority';

client = MongoClient(url)

db = client.pytech

students = db['students']

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for docs in students.find({}):
    print("Student ID: " + docs["student_id"] + "\nFirst Name: " + docs["first_name"] + "\nLast Name: " + docs["last_name"] + "\n")
    print()

result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

docs = students.find_one({"student_id": "1007"})
print("-- DISPLAYING UPDATED STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student ID: " + docs["student_id"] + "\nFirst Name: " + docs["first_name"] + "\nLast Name: " + docs["last_name"] + "\n")
