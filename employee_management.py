import json
import os
from datetime import datetime

class Employee:
    """Represents an employee with basic attributes."""
    def __init__(self, emp_id, name, department, salary, position):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.position = position

    def to_dict(self):
        """Convert Employee object to dictionary for JSON serialization."""
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary,
            "position": self.position
        }

    @staticmethod
    def from_dict(data):
        """Create an Employee object from a dictionary."""
        return Employee(
            data["emp_id"],
            data["name"],
            data["department"],
            data["salary"],
            data["position"]
        )

    def __str__(self):
        return f"ID: {self.emp_id} | Name: {self.name} | Dept: {self.department} | Salary: ${self.salary:,.2f} | Position: {self.position}"


class EmployeeManager:
    """Manages a collection of employees with file persistence."""
    def __init__(self, filename="employees.json"):
        self.filename = filename
        self.employees = {}  # emp_id -> Employee object
        self.load_from_file()

    def load_from_file(self):
        """Load employee data from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    for emp_data in data:
                        emp = Employee.from_dict(emp_data)
                        self.employees[emp.emp_id] = emp
                print(f"Loaded {len(self.employees)} employees from {self.filename}")
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading file: {e}. Starting with empty database.")
        else:
            print(f"No existing data file found. Starting fresh.")

    def save_to_file(self):
        """Save all employees to JSON file."""
        data = [emp.to_dict() for emp in self.employees.values()]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Saved {len(self.employees)} employees to {self.filename}")

    def add_employee(self, emp_id, name, department, salary, position):
        """Add a new employee. Returns True if successful, False if ID already exists."""
        if emp_id in self.employees:
            print(f"Employee with ID {emp_id} already exists.")
            return False
        self.employees[emp_id] = Employee(emp_id, name, department, salary, position)
        self.save_to_file()  # auto-save after each change
        print(f"Employee {name} added successfully.")
        return True

    def view_all(self):
        """Display all employees."""
        if not self.employees:
            print("No employees found.")
            return
        print("\n--- All Employees ---")
        for emp in self.employees.values():
            print(emp)
        print(f"Total: {len(self.employees)} employees\n")

    def search_by_id(self, emp_id):
        """Return employee if found, else None."""
        return self.employees.get(emp_id)

    def search_by_name(self, name):
        """Return list of employees matching the name (case‑insensitive partial match)."""
        name_lower = name.lower()
        result = [emp for emp in self.employees.values() if name_lower in emp.name.lower()]
        return result

    def update_employee(self, emp_id, name=None, department=None, salary=None, position=None):
        """Update employee details. Only provided fields are updated."""
        emp = self.employees.get(emp_id)
        if not emp:
            print(f"Employee with ID {emp_id} not found.")
            return False
        if name:
            emp.name = name
        if department:
            emp.department = department
        if salary is not None:
            emp.salary = salary
        if position:
            emp.position = position
        self.save_to_file()
        print(f"Employee {emp_id} updated successfully.")
        return True

    def delete_employee(self, emp_id):
        """Delete an employee by ID."""
        if emp_id in self.employees:
            del self.employees[emp_id]
            self.save_to_file()
            print(f"Employee {emp_id} deleted successfully.")
            return True
        else:
            print(f"Employee with ID {emp_id} not found.")
            return False


def main():
    """Main menu loop."""
    manager = EmployeeManager()

    while True:
        print("\n" + "="*40)
        print("     EMPLOYEE MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        print("="*40)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\n--- Add New Employee ---")
            try:
                emp_id = input("Enter Employee ID: ").strip()
                name = input("Enter Name: ").strip()
                department = input("Enter Department: ").strip()
                salary = float(input("Enter Salary: "))
                position = input("Enter Position: ").strip()
                manager.add_employee(emp_id, name, department, salary, position)
            except ValueError:
                print("Invalid input. Salary must be a number.")

        elif choice == "2":
            manager.view_all()

        elif choice == "3":
            print("\n--- Search Employee ---")
            print("Search by: (1) ID  (2) Name")
            sub = input("Your choice: ").strip()
            if sub == "1":
                emp_id = input("Enter Employee ID: ").strip()
                emp = manager.search_by_id(emp_id)
                if emp:
                    print(emp)
                else:
                    print("Employee not found.")
            elif sub == "2":
                name = input("Enter name (or part): ").strip()
                results = manager.search_by_name(name)
                if results:
                    print(f"Found {len(results)} employee(s):")
                    for emp in results:
                        print(emp)
                else:
                    print("No matching employees.")
            else:
                print("Invalid search option.")

        elif choice == "4":
            print("\n--- Update Employee ---")
            emp_id = input("Enter Employee ID to update: ").strip()
            emp = manager.search_by_id(emp_id)
            if not emp:
                print("Employee not found.")
                continue
            print("Leave field blank to keep current value.")
            name = input(f"New Name (current: {emp.name}): ").strip()
            department = input(f"New Department (current: {emp.department}): ").strip()
            salary_input = input(f"New Salary (current: {emp.salary}): ").strip()
            position = input(f"New Position (current: {emp.position}): ").strip()

            # Convert salary if provided
            salary = None
            if salary_input:
                try:
                    salary = float(salary_input)
                except ValueError:
                    print("Invalid salary. Keeping current value.")
            # Only pass non-empty values (salary can be 0, so check None)
            manager.update_employee(
                emp_id,
                name=name if name else None,
                department=department if department else None,
                salary=salary if salary_input else None,
                position=position if position else None
            )

        elif choice == "5":
            print("\n--- Delete Employee ---")
            emp_id = input("Enter Employee ID to delete: ").strip()
            manager.delete_employee(emp_id)

        elif choice == "6":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()