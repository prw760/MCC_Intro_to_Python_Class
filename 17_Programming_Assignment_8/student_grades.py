# Paul Wade
# PA 8

# Populate dictionary with student names and grades

student_grades = {
	"Dylan Sprouse": "D",
	"Abigail Spencer": "C",
	"Daniel Kim": "B",
	"Lauren Tom": "A",
	"Michael DeLuise": "F",
	"Pedro Pascal": "B",
	"Paulina Garcia	": "A",
	"Paulina Gaitan": "C",
	"Gemma Chan": "C",
	"Carmen Soo": "B"
	}


# Main Program

while True:

	# Obtain Search Type (By Name or by Grade

	search_type = str(input("Would you like to search by name (N) or grade (G): "))

	if search_type == "N":

		# Search Dictionary for Grades by Student Name and Output Results`

		search_name = str(input("Enter the student's name to search for: "))

		search_grade = student_grades.get(search_name, "")

		if search_name in student_grades:

			# Grade found, so output results

			print(f"\n{search_name}'s grade is {student_grades[search_name]}")

			break    # Exit upon successful search

		else:

			print("The student name entered does not exist.")

	elif search_type == "G":

		# Search Dictionary for Names of Student's with a particular grade and output list (if any)

		search_grade = str(input("Enter a grade to search for (A,B,C,D,F): "))

		if search_grade in student_grades.values():

			# Students Found, so output results

			print("\nThe following students received a grade of " + search_grade + ":")

			for student, grade in student_grades.items():

				if grade == search_grade:
					print(student)

			break       # Exit upon successful search

		else:

			print("No students received the grade entered.")

	else:

		print("You must enter a N or G")
