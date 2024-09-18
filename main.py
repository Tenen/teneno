from employee_manager import add_employee, edit_employee, delete_employee, list_employees, load_employees

def main_menu():
    print("\nWhat is the purpose of your visit?")
    print("1. Add Employee")
    print("2. Edit Employee")
    print("3. Delete Employee")
    print("4. List Employees")
    print("5. Exit")

def main():
    # Display the welcome message once at the start
    print("\nWelcome User to {Employee Management System} or {EMS} for short.")

    while True:
        # Display the main menu options
        main_menu()

        choice = input("Please enter the desired number: ")

        if choice == '1':
            while True:
                print("\nTo return to the main menu at any time, press 0.")
                name = input("Enter Name: ")
                if name == '0':
                    break
                age = input("Enter Age: ")
                if age == '0':
                    break
                emp_id = input("Enter ID: ")
                if emp_id == '0':
                    break
                salary = input("Enter Salary: ")
                if salary == '0':
                    break

                # Try to add employee, if duplicate ID, retry the loop
                add_employee(name, age, emp_id, salary)

                # Check if employee was added successfully
                if any(emp["ID"] == emp_id for emp in load_employees()):
                    print("Employee added successfully! Returning to main menu.")
                    break  # Exit the loop after successful addition

        elif choice == '2':
            while True:
                print("\nTo return to the main menu at any time, press 0.")
                identifier = input("Enter Employee ID or Name to edit: ")
                if identifier == '0':
                    break
                name = input("Enter new Name (leave blank to keep current): ")
                if name == '0':
                    break
                age = input("Enter new Age (leave blank to keep current): ")
                if age == '0':
                    break
                salary = input("Enter new Salary (leave blank to keep current): ")
                if salary == '0':
                    break
                emp_id = input("Enter Employee ID (leave blank to keep current): ")
                if emp_id == '0':
                    break
                edit_employee(identifier, name or None, age or None, salary or None, emp_id or None)
                print("Employee edited successfully! Returning to main menu.")
                break

        elif choice == '3':
            while True:
                print("\nTo return to the main menu at any time, press 0.")
                identifier = input("Enter Employee ID or Name to delete: ")
                if identifier == '0':
                    break
                delete_employee(identifier)
                print("Employee deleted successfully! Returning to main menu.")
                break

        elif choice == '4':
            list_employees()

        elif choice == '5':
            print("Exiting program...")
            break

        elif choice == '0':
            print("Returning to main menu...")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
