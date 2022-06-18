from pymongo import MongoClient

url = 'mongodb://admin:admin@ac-um0ozvv-shard-00-00.dlvbmu8.mongodb.net:27017,ac-um0ozvv-shard-00-01.dlvbmu8.mongodb.net:27017,ac-um0ozvv-shard-00-02.dlvbmu8.mongodb.net:27017/?ssl=true&replicaSet=atlas-4dykia-shard-0&authSource=admin&retryWrites=true&w=majority';

client = MongoClient(url)

db = client.pytech

students = db['students']

max = { "_id": 1,
  "student_id": "1007",
  "first_name": "Max",
  "last_name": "Levchin"
 }

michael = { "_id": 2,
  "student_id": "1008",
  "first_name": "Michael",
  "last_name": "Widenius"
 }

pierre = { "_id": 3,
  "student_id": "1009",
  "first_name": "Pierre",
  "last_name": "Omidyar"
 }


''' Adding values from above to MongoDB > pytech > students collection
max_student_id = students.insert_one(max).inserted_id
michael_student_id = students.insert_one(michael).inserted_id
pierre_student_id = students.insert_one(pierre).inserted_id
'''

for docs in students.find():
  print(docs["student_id"])
