"""
Data structure:

courses: list = [
    course: dict = {
        id: string,
        name: string
    }
]

students: list = [
    student: dict = {
        id: string,
        name: string,
        dob: string,
        marks : dict = {
            course_id (string) : mark (float)
        }
    }
]
"""
pre_entered_students = [
    {"id": "S001", "name": "An", "dob": "12/01/2000", "marks": {"C001": 15.0, "C002": 19.0}},
    {"id": "S002", "name": "Binh", "dob": "30/12/2005", "marks": {"C001": 18.0}},
    {"id": "S003", "name": "Cuong", "dob": "03/03/2004", "marks": {"C002": 20.0}}
]

pre_entered_courses = [
    {"id": "C001", "name": "Python"},
    {"id": "C002", "name": "OOP"}
]

def input_student() -> list:
    n = int(input("Enter the number of students: "))
    students = []
    for _ in range(n):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student birthday: ")
        student = {"id": student_id, "name": name, "dob": dob, "marks": {}}

        students.append(student)
    return students

def input_courses() -> list:
    n = int(input("Enter the number of courses: "))
    courses = []
    for _ in range(n):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = {"id": course_id, "name": name}

        courses.append(course)
    return courses

def select_course_and_input_marks(students, courses):
    course_id = input("Enter the course ID to input marks: ")
    course = None

    #search
    for c in courses:
        if c["id"] == course_id:
            course = c
            break
    
    if course is None:
        print("Course not found!")
        return
    print(f"Entering marks for course: {course['name']}")
    for student in students:
        mark = float(input(f"Enter marks for student {student['name']} (ID: {student['id']}): "))
        student["marks"][course_id] = mark

# listing functions
def list_courses(courses):
    if (not courses):
        print("No courses entered yet")

    print("======================")
    print("Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

    print("======================")


def list_students(students):
    if (not students):
        print("No student entered yet")
        return
    
    print("======================")
    print("Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

    print("======================")


def show_student_marks(students, courses):
    print("======================")
    course_id = input("Enter the course ID to view marks: ")
    
    #search for the correseponding id
    course = None
    for c in courses:
        if c["id"] == course_id:
            course = c
            break

    if course is None:
        print("Course not found!")
        return
    print(f"Marks for course: {course['name']}")

    for student in students:
        if course_id in student["marks"]:
            print(f"Student {student['name']} (ID: {student['id']}): {student['marks'][course_id]}")
        else:
            print(f"Student {student['name']} (ID: {student['id']}): No marks entered")
    print("======================")

# Main program
def main():
    print("Handsome TMD program")

    prompt = input("Are you lazy and do NOT want to input data? (yes/no): ")
    if (prompt == "yes"):
        print("Great, I pre-entered some data for you, no need to thank me :D")
        students = pre_entered_students.copy()
        courses = pre_entered_courses.copy()
    else:
        students = input_student()
        courses = input_courses()
    
    while True:
        print("Options:")
        print("1. List students")
        print("2. List courses")
        print("3. Input marks for a course")
        print("4. Show student marks for a course")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            list_students(students)
        elif choice == 2:
            list_courses(courses)
        elif choice == 3:
            select_course_and_input_marks(students, courses)
        elif choice == 4:
            show_student_marks(students, courses)
        elif choice == 5:
            print("TMD peace out!")
            break
        else:
            print("Invalid choice. Please try again.")

#Driver code
if __name__ == "__main__":
    main()
