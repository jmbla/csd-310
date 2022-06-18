from pymongo import MongoClient

url = 'mongodb://admin:admin@ac-um0ozvv-shard-00-00.dlvbmu8.mongodb.net:27017,ac-um0ozvv-shard-00-01.dlvbmu8.mongodb.net:27017,ac-um0ozvv-shard-00-02.dlvbmu8.mongodb.net:27017/?ssl=true&replicaSet=atlas-4dykia-shard-0&authSource=admin&retryWrites=true&w=majority';

client = MongoClient(url)

db = client.pytech

students = db['students']

max = {
  "student_id": "1007",
  "first_name": "Max",
  "last_name": "Levchin"
 }

michael = {
  "student_id": "1008",
  "first_name": "Michael",
  "last_name": "Widenius"
 }

pierre = {
  "student_id": "1009",
  "first_name": "Pierre",
  "last_name": "Omidyar"
 }


''' Adding values from above to MongoDB > pytech > students collection '''
max_student_id = students.insert_one(max).inserted_id
michael_student_id = students.insert_one(michael).inserted_id
pierre_student_id = students.insert_one(pierre).inserted_id


print("-- INSERT STATEMENTS --")
for docs in students.find():
  print("Inserted student record", docs["first_name"], docs["last_name"], "into the students collection with student_id", docs[ "student_id"])
