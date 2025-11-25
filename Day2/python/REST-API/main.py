from fastapi import FastAPI, HTTPException

app = FastAPI()

employees = [ 
        { "id": 1, "name": "Sharma", "dept": "IT" },
        { "id": 2, "name": "Martin", "dept": "IT" }
]

# Add an employee
#To test this, we need to use curl utility in the command-line with below command
#curl -X POST http://localhost:8000/employees \
#-H "Content-Type": "application/json" \
#-d '{"id": 100, "name": "Siddharth", "dept": "IT"}'
@app.post("/employees")
def addEmployee( employee: dict ):
    employees.append( employee)
    return {"Message": "Employee details added", "data": employee}

#To test this, in your web browse http://localhost:8000/employees
@app.get("/employees")
def getEmployees():
    return employees

#To test this, in your web browse http://localhost:8000/employees/1
#To test this, in your web browse http://localhost:8000/employees/2
#To test this, in your web browse http://localhost:8000/employees/3
@app.get("/employees/{employeeID}")
def getEmployeeById( employeeID: int ):
    for employee in employees:
        if employee["id"] == employeeID:
           return employee
    raise HttpException(404,detail="Employee details not found")

#To test this

#curl -X PUT http://localhost:8000/employees \
#-H "Content-Type": "application/json" \
#-d '{"id": 100, "name": "Shankar", "dept": "IT"}'
@app.put("/employees/{employeeID}")
def updateEmployee( employeeID: int, data: dict ):
    for employee in employees:
        if employee["id"] == employeeID:
           employee.update( data )
           return {"message": "Updated", "data": employee}
    raise HttpException(404,detail="Employee details not found")

#To delete a record given a ID
#curl -x DELETE https://localhost:8000/employee/100
@app.delete("/employees/{employeeID}")
def deleteEmployee(employeeID: int):
    for employee in employees:
        if employee["id"] ==  employeeID:
            employees.remove(employee)
            return {"message": "Deleted successfully"}
    raise HttpException(404,detail="Employee details not found")
