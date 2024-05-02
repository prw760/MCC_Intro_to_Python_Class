# Paul Wade
# PA 13

import sqlite3


# populate a list of student data . . .
student_data_list = [
    (1111, "Dave", "Grohl", "Music", 4.0),
    (2222, "Belinda", "Carlisle", "Accounting", 3.5),
    (3333, "Joe", "Eliott", "Computer Science", 2.8),
    (4444, "Angus", "Young", "Accounting", 2.1),
    (5555, "Susanna", "Hoffs", "Music", 3.1),
    (6666, "Debbie", "Harry", "Computer Science", 3.4),
    (7777, "Saul", "Hudson", "Music", 2.7),
    (8888, "Paul", "Hewson", "Computer Science", 1.8)
]


# assign path and filename "constants"
ASSIGNMENT_PATH = (
    '/users/paulwade/Documents/GitHub/educational/MCC_Intro_to_Python_Class/23_Programming_Assignment_13/ ')
DB_FILENAME = 'DSUcollege.db'


# function returns a database connection to a SQLite database
def create_connection():
    with sqlite3.connect(ASSIGNMENT_PATH + DB_FILENAME) as conn:
        return conn


# function to create/recreate the student table
def create_table(conn):
    curs = conn.cursor()
    curs.execute("DROP TABLE IF EXISTS students")
    create_sql = """CREATE TABLE students(
                            student_id INT,
                            first_name TEXT,
                            last_name TEXT,
                            major_name TEXT,
                            gpa REAL);"""
    cursor.execute(create_sql)

    print("The table was created successfully")


# function to populate the student table with data . . .
def populate_table(cursor_param, student_data_param):

    for this_student in student_data_param:

        student_id = str(this_student[0])
        first_name = str(this_student[1])
        last_name = str(this_student[2])
        major_name = str(this_student[3])
        gpa = "{:.1f}".format(float(this_student[4]))

        insert_sql = f'INSERT INTO students VALUES ({student_id}, "{first_name}", "{last_name}", "{major_name}", {gpa})'

        cursor_param.execute(insert_sql)

    print("The table was populated with the students successfully\n")


# function to update various records in the student database . . .
def update_table(cursor_param):

    delete_sql = "DELETE FROM STUDENTS WHERE student_id=1111"
    cursor_param.execute(delete_sql)
    print("The delete of Dave Grohl was successful")

    update_sql = "UPDATE STUDENTS SET major_name='Music' WHERE student_id=8888"
    cursor_param.execute(update_sql)
    print("The update of Paul Hewson was successful")

    update_sql = "UPDATE STUDENTS SET gpa =4.0 WHERE student_id=6666"
    cursor_param.execute(update_sql)
    print("The update of Debbie Harry was successful")


# function to query the student table and print various student lists . . .
def query_table(cursor_param):

    refresh_sql = "SELECT * FROM students"

    student_data = cursor_param.execute(refresh_sql)
    student_data_sorted = sorted(student_data, key=lambda x: x[2])

    print("\nAll students")
    for student in student_data_sorted:
        print(student)

    print("\nStudents majoring in Music")

    music_majors = [(student[1], student[2]) for student in student_data_sorted if student[3] == 'Music']

    for student in music_majors:
        print(student)

    print("\nStudents with a 3.0 or higher gpa")

    gpa_3_students = [(student[1], student[2], student[3], student[4]) for student in student_data_sorted if
                      student[4] >= 3.0]

    for student in gpa_3_students:
        print(student)


# Main program starts here . . .
with create_connection() as connection:
    cursor = connection.cursor()

    create_table(connection)

    populate_table(cursor, student_data_list)

    update_table(cursor)

# have to reopen database connection to refresh data . . .
with create_connection() as connection:
    cursor = connection.cursor()

    query_table(cursor)

# JEFFREY, PLEASE NOTE: My "Students Majoring in Music" list is printed sorted by last_name field.
# I hope that is okay even though it doesn't exactly match the assignment output screenshot

# ALSO: I don't understand why my python3 installation only allows me to import "sqlite3" and not "sqlite."
# I hope this doesn't make any difference for the purposes of this assignment.
