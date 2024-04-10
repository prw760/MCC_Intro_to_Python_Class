# Paul Wade
# PA_9

class Employee:
	def __init__(self, empID, name, department, yearly_salary):
		self.employee_number = empID
		self.name = name
		self.department = department
		self.yearly_salary = yearly_salary

	def __str__(self):
		return (f"\nEmployee Information: \
				\nEmployee Number: {self.employee_number} \
				\nName: {self.name} \
				\nDepartment: {self.department} \
				\nYearly Salary: ${self.yearly_salary:,}")

	def update_department(self, department):
		self.department = department

	def update_salary(self, yearly_salary):
		self.yearly_salary = yearly_salary


print("Enter the employee information:")
employee_number = int(input("Enter employee number: "))
employee_name = str(input("Enter employee name: "))
employee_department = str(input("Enter employee department: "))
employee_salary = int(input("Enter employee salary: "))

myEmployee = Employee(employee_number, employee_name, employee_department, employee_salary)

print(myEmployee)

myEmployee.update_department("Finance")
myEmployee.update_salary(75000)

print(myEmployee)
