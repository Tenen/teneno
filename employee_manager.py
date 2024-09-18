import json
import os

# Define the path to the JSON file
EMPLOYEE_FILE_PATH = 'data/employees.json'


# Function to load employees from the JSON file
def load_employees():
    if os.path.exists(EMPLOYEE_FILE_PATH):
        with open(EMPLOYEE_FILE_PATH, 'r') as file:
            try:
                employees = json.load(file)
            except json.JSONDecodeError:
                employees = []
    else:
        employees = []
    return employees


# Function to save employees to the JSON file
def save_employees(employees):
    try:
        with open(EMPLOYEE_FILE_PATH, 'w') as file:
            json.dump(employees, file, indent=4)
    except IOError as e:
        print(f"Error saving employees: {e}")


# Function to add a new employee
def add_employee(name, age, emp_id, salary):
    employees = load_employees()

    # Check for duplicate ID
    for employee in employees:
        if employee["ID"] == emp_id:
            print(f"Error: An employee with ID {emp_id} already exists.")
            print(
                f"Existing Employee - Name: {employee['Name']}, Age: {employee['Age']}, ID: {employee['ID']}, Salary: {employee['Salary']}")
            print("Please try again with a different ID.")
            return  # Exit the function to prompt the user again in the main loop

    # Add new employee if ID is unique
    new_employee = {
        "Name": name,
        "Age": age,
        "ID": emp_id,
        "Salary": salary
    }
    employees.append(new_employee)
    save_employees(employees)
    print("Employee added successfully!")


# Function to edit an existing employee by ID or Name
def edit_employee(identifier, name=None, age=None, salary=None, emp_id=None):
    employees = load_employees()
    matched_employees = [e for e in employees if e["ID"] == identifier or e["Name"] == identifier]

    if not matched_employees:
        print(f"No employee found with ID or Name: {identifier}")
        return

    if len(matched_employees) > 1:
        print("\nMultiple employees found:")
        for idx, employee in enumerate(matched_employees, start=1):
            print(
                f"{idx}. Name: {employee['Name']}, Age: {employee['Age']}, ID: {employee['ID']}, Salary: {employee['Salary']}")
        choice = int(input("Select the employee number to edit: ")) - 1
        if 0 <= choice < len(matched_employees):
            employee = matched_employees[choice]
        else:
            print("Invalid selection.")
            return
    else:
        employee = matched_employees[0]

    if name:
        employee["Name"] = name
    if age:
        employee["Age"] = age
    if salary:
        employee["Salary"] = salary
    if emp_id:
        employee["ID"] = emp_id

    save_employees(employees)
    print("Employee edited successfully.")


# Function to delete an employee by ID or Name
def delete_employee(identifier):
    employees = load_employees()
    matched_employees = [e for e in employees if e["ID"] == identifier or e["Name"] == identifier]

    if not matched_employees:
        print(f"No employee found with ID or Name: {identifier}")
        return

    if len(matched_employees) > 1:
        print("\nMultiple employees found:")
        for idx, employee in enumerate(matched_employees, start=1):
            print(
                f"{idx}. Name: {employee['Name']}, Age: {employee['Age']}, ID: {employee['ID']}, Salary: {employee['Salary']}")
        choice = int(input("Select the employee number to delete: ")) - 1
        if 0 <= choice < len(matched_employees):
            employee = matched_employees[choice]
        else:
            print("Invalid selection.")
            return
    else:
        employee = matched_employees[0]

    confirm = input(
        f"Are you sure you want to delete the employee {employee['Name']} (ID: {employee['ID']})? (yes/no): ")
    if confirm.lower() == 'yes':
        employees = [e for e in employees if e["ID"] != employee["ID"]]
        save_employees(employees)
        print("Employee deleted successfully.")
    else:
        print("Deletion cancelled.")


# Function to list all employees
def list_employees():
    employees = load_employees()
    if employees:
        print("\nCurrent Employee List:")
        for idx, employee in enumerate(employees, start=1):
            print(
                f"{idx}. Name: {employee['Name']}, Age: {employee['Age']}, ID: {employee['ID']}, Salary: {employee['Salary']}")
    else:
        print("No employees found.")
