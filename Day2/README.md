# Day 2

## Lab - Write a python program that reads a text file and print the occurence of each word in the file

Note
<pre>
- the word can be treated case insensitive
- i.e Apple, apple, APPLE, APple can be treated as same
</pre>

## Info - API Overview
<pre>
- API - Application Programming Interface
- let's two or more applications interact with each other via APIs
- allows applications to exchange data
- useful in authentWorking With Files

	Reading And Writing Files

	Parsing Different File Formats (CSV, JSON, YAML)icating applications
- helps in integrating 3rd party applications and their services
- examples
  - Google Map API
  - PayTM or GPay APIs
  - Gmail, Facebook Integration or Authentication
- REST API Methods
  - GET  - used while retrieving data ( retrieved already registered user details )
  - POST - used while creating new records ( registering new users )
  - PUT  - used while updating existing data
  - PATCH - used while updating partial update
  - DELETE - deleting a record
</pre>


## Lab - Running and testing the REST API
Open Terminal Tab 1, run the below command
```
cd ~/ansible-nov-2025
git pull
cd Day2/python/REST-API
uvicorn main:app --reload
```

Open Terminal Tab, run the below command
```
# To try retrieving existing records
curl -X GET http://localhost:8000/employees
curl -X GET http://localhost:8000/employees/1
curl -X GET http://localhost:8000/employees/2

# To add new record
curl -X POST http://localhost:8000/employees \
-H "Content-Type": "application/json" \
-d '{"id": 100, "name": "Siddharth", "dept": "IT"}'

# To try updating existing record
curl -X PUT http://localhost:8000/employees \
-H "Content-Type": "application/json" \
-d '{"id": 100, "name": "Shankar", "dept": "IT"}'

# To delete existing record
curl -X DELETE http://localhost:8000/employees/2 \
-H "Content-Type": "application/json"


```
