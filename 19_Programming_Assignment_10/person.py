# Paul Wade
# PA 10

# Class Definitions (Person, Student, Teacher)

class Person:
	def __init__(self, p_name, p_year_of_birth):
		self.name = p_name
		self.year_of_birth = p_year_of_birth

	def __str__(self):
		return f'\nName: {self.name}\nYear of birth: {self.year_of_birth}'


class Student(Person):
	def __init__(self, p_name, p_year_of_birth, p_major):
		super().__init__(p_name, p_year_of_birth)
		self.major = p_major

	def __str__(self):
		return super().__str__() + f'\nMajor: {self.major}'


class Teacher(Person):
	def __init__(self, p_name, p_year_of_birth, p_salary):
		super().__init__(p_name, p_year_of_birth)
		self.salary = p_salary

	def __str__(self):
		return super().__str__() + f'\nSalary: ${self.salary:,}'


# Start of Main Program

# instantiate a Person object using values input by user, then print out the object

print("Enter the person information:")
name = str(input("Enter the name: "))
year_of_birth = int(input("Enter the year of birth: "))

myPerson = Person(name, year_of_birth)
print("\nPerson information:" + str(myPerson))


# instantiate a Student object using values input by user, then print out the object

print("\nEnter the student information:")
name = str(input("Enter the name: "))
year_of_birth = int(input("Enter the year of birth: "))
major = str(input("Enter the major: "))

myStudent = Student(name, year_of_birth, major)
print("\nStudent information:" + str(myStudent))


# instantiate a Teacher object using values input by user, then print out the object

print("\nEnter the teacher information:")
name = str(input("Enter the name: "))
year_of_birth = int(input("Enter the year of birth: "))
salary = int(input("Enter the salary: "))

myTeacher = Teacher(name, year_of_birth, salary)
print("\nTeacher information:" + str(myTeacher))
