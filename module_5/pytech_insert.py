students = { "student_id": "1007",
  "first_name": "Joe",
  "last_name": "Black"
 }


student_id = students.insert_one(students).inserted_id
  
print(student_id)
  
