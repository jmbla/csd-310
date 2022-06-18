MongoDB: insert_one() Example
  fred = {"first_name": "Fred"}
  
  fred_employee_id = employees.insert_one(fred).inserted_id
  
  print(fred_employee_id)
  
  MongoDB: find() Example
    docs = db.collection_name.find()
    
    for doc in docs:
      print(doc)
      MongoDB: find_one() Exmaple
        doc = db.collection_name.find_one({"employee_id": "1007"})
        
        print(doc["employee_id"])
        
  
