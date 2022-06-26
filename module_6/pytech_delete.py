from pymongo import MongoClient

url = 'mongodb://admin:admin@ac-um0ozvv-shard-00-00.dlvbmu8.mongodb.net:27017,ac-um0ozvv-shard-00-01.dlvbmu8.mongodb.net:27017,ac-um0ozvv-shard-00-02.dlvbmu8.mongodb.net:27017/?ssl=true&replicaSet=atlas-4dykia-shard-0&authSource=admin&retryWrites=true&w=majority';

client = MongoClient(url)

db = client.pytech

students = db['students']

docs = students.find({})

print('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')

for doc in docs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")
    print()

students.delete_one({"student_id": "1010"})

students.insert_one({"student_id": "1010", "first_name": "Peter", "last_name": "Parker"}).inserted_id

insertedDoc = students.find_one({"student_id": "1010"})

print('-- INSERT STATEMENTS --')
print('Inserted student record 1010 into the students collection with document_id', insertedDoc["_id"])
print()


docs = students.find({})

print('-- DISPLAYING NEW STUDENT LIST DOC --')

for doc in docs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")


students.delete_one({"student_id": "1010"})

docs = students.find({})

print('-- DELETED STUDENT ID: 1010 --')

for doc in docs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")