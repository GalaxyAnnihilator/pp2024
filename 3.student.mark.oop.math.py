import math
import numpy as np
import curses

class Person:
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

class Student(Person):
    def __init__(self, id, name, dob, marks={}):
        super().__init__(name, dob)
        self.__id = id
        self.__marks = marks
        self.__GPA = None

    def get_id(self):
        return self.__id

    def get_marks(self):
        return self.__marks

    def get_GPA(self):
        return self.__GPA

    def set_GPA(self, gpa):
        self.__GPA = gpa

    def __str__(self):
        return f"StudentID: {self.get_id()}, Name: {self.get_name()}, DoB: {self.get_dob()}, GPA: {self.get_GPA()}"

class Course:
    def __init__(self, id, name, credits):
        self.__id = id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"CourseID: {self.get_id()}, Name: {self.get_name()}, Credits: {self.get_credits()}"

class Outils:
    @staticmethod
    def show(list_items, stdscr):
        stdscr.clear()
        for i, item in enumerate(list_items):
            stdscr.addstr(i, 0, str(item))
        stdscr.refresh()
        stdscr.getch()

    @staticmethod
    def input_string(prompt, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, prompt)
        stdscr.refresh()
        curses.echo()
        user_input = stdscr.getstr(1, 0).decode("utf-8")
        curses.noecho()
        return user_input

    @staticmethod
    def input_integer(prompt, stdscr):
        while True:
            try:
                user_input = Outils.input_string(prompt, stdscr)
                return int(user_input)
            except ValueError:
                stdscr.addstr(2, 0, "Invalid input. Please enter an integer.")
                stdscr.refresh()
                stdscr.getch()

class University:
    def __init__(self):
        self.__num_students = 0
        self.__num_courses = 0
        self.__students = []
        self.__courses = []

    def get_num_students(self):
        return self.__num_students

    def get_num_courses(self):
        return self.__num_courses

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def set_students(self, num):
        self.__num_students = num

    def set_courses(self, num):
        self.__num_courses = num

    def set_num_students(self, stdscr):
        self.__num_students = Outils.input_integer("Enter the number of students: ", stdscr)

    def set_num_courses(self, stdscr):
        self.__num_courses = Outils.input_integer("Enter the number of courses: ", stdscr)

    #preload some data - basically just setter methods :/
    def load_courses(self,courses):
        self.__courses = courses

    def load_students(self,students):
        self.__students = students 


    def add_student(self, stdscr):
        id = Outils.input_string("Enter the student's ID: ", stdscr)
        name = Outils.input_string("Enter the student's name: ", stdscr)
        dob = Outils.input_string("Enter the student's DoB: ", stdscr)
        self.__students.append(Student(id, name, dob))

    def add_course(self, stdscr):
        id = Outils.input_string("Enter the course's ID: ", stdscr)
        name = Outils.input_string("Enter the course's name: ", stdscr)
        credits = Outils.input_integer("Enter the course's credits: ", stdscr)
        self.__courses.append(Course(id, name, credits))

    def input_students(self, stdscr):
        if self.get_num_students() == 0:
            stdscr.addstr(0, 0, "Please input the number of students first.")
            stdscr.refresh()
            stdscr.getch()
            return

        for _ in range(self.get_num_students()):
            self.add_student(stdscr)

    def input_courses(self, stdscr):
        if self.get_num_courses() == 0:
            stdscr.addstr(0, 0, "Please input the number of courses first.")
            stdscr.refresh()
            stdscr.getch()
            return

        for _ in range(self.get_num_courses()):
            self.add_course(stdscr)

    def enter_mark(self, stdscr):
        course_id = Outils.input_string("Enter the course ID to input marks: ", stdscr)
        course = next((c for c in self.__courses if c.get_id() == course_id), None)

        if not course:
            stdscr.addstr(0, 0, "Course not found!")
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.addstr(1, 0, f"Entering marks for course: {course.get_name()}")
        for student in self.__students:
            prompt = f"Enter marks for student {student.get_name()} (ID: {student.get_id()}): "
            mark = float(Outils.input_string(prompt, stdscr))
            student.get_marks()[course_id] = mark

    def display_mark(self, stdscr):
        course_id = Outils.input_string("Enter the course ID to view marks: ", stdscr)
        course = next((c for c in self.__courses if c.get_id() == course_id), None)

        if not course:
            stdscr.addstr(0, 0, "Course not found!")
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.addstr(1, 0, f"Marks for course: {course.get_name()}")
        for student in self.__students:
            mark = student.get_marks().get(course_id, "No marks entered")
            stdscr.addstr(f"Student {student.get_name()} (ID: {student.get_id()}): {mark}\n")
        stdscr.refresh()
        stdscr.getch()

    def list_students(self, stdscr):
        if not self.get_students():
            stdscr.addstr(0, 0, "No students input yet.")
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.addstr(0, 0, "Student list:")
        Outils.show(self.get_students(), stdscr)

    def list_courses(self, stdscr):
        if not self.get_courses():
            stdscr.addstr(0, 0, "No courses input yet.")
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.addstr(0, 0, "Course list:")
        Outils.show(self.get_courses(), stdscr)

    def calculate_GPA(self, student):
        marks = []
        credits = []
        for course_id, mark in student.get_marks().items():
            course = next((c for c in self.__courses if c.get_id() == course_id), None)
            if course:
                marks.append(mark)
                credits.append(course.get_credits())

        if credits:
            marks_array = np.array(marks)
            credits_array = np.array(credits)

            # Calculate GPA
            weighted_sum = np.sum(marks_array * credits_array)
            total_credits = np.sum(credits_array)
            gpa = weighted_sum / total_credits
            student.set_GPA(round(gpa, 2))
        else:
            student.set_GPA(0.0)

    def display_GPA(self, stdscr):
        for student in self.__students:
            self.calculate_GPA(student)

        gpa_data = [(student.get_name(), student.get_GPA()) for student in self.__students]
        dtype = [('name', 'U50'), ('gpa', 'f4')]
        gpa_array = np.array(gpa_data, dtype=dtype)

        sorted_gpa_array = np.sort(gpa_array, order='gpa')[::-1]

        stdscr.clear()
        stdscr.addstr("GPA List (Descending Order):\n")
        for i, record in enumerate(sorted_gpa_array):
            stdscr.addstr(f"{i + 1}. {record['name']} - GPA: {record['gpa']:.2f}\n")
        stdscr.refresh()

    
# Preloaded data
def preload_data(university):
    pre_entered_students = [
        Student("S001", "An", "12/01/2000", {"C001": 15, "C002": 19}),
        Student("S002", "Binh", "30/12/2005", {"C001": 18, "C002" : 20}),
        Student("S003", "Cuong", "03/03/2004", {"C002": 20, "C002": 15})
    ]

    pre_entered_courses = [
        Course("C001", "Python", 3),
        Course("C002", "OOP", 4)
    ]

    university.set_courses(len(pre_entered_courses))
    university.set_students(len(pre_entered_students))
    university.load_courses(pre_entered_courses)
    university.load_students(pre_entered_students)

def curses_main(stdscr):
    USTH = University()

    # Clear screen
    stdscr.clear()

    # Menu options
    menu_text = [
        "0. Load pre-entered data (highly recommended for the lazy guys)",
        "1. Input number of students",
        "2. Input number of courses",
        "3. Input students info",
        "4. Input courses info",
        "5. Enter mark of students in a specific course",
        "6. Display all students",
        "7. Display all courses",
        "8. Display mark for a specific course",
        "9. Calculate and display GPA of all students in descending order",
        "10. Exit"
    ]

    while True:
        # Get terminal dimensions
        max_y, max_x = stdscr.getmaxyx()

        # Ensure terminal is large enough
        if len(menu_text) >= max_y:
            stdscr.addstr(0, 0, "Terminal too small for menu display")
            stdscr.refresh()
            stdscr.getch()
            return

        # Display menu
        stdscr.clear()
        for i, line in enumerate(menu_text):
            stdscr.addstr(i, 0, line)
        stdscr.addstr(len(menu_text), 0, "Enter your choice: ")
        stdscr.refresh()

        # Get user input and display it back
        try:
            curses.echo()
            choice = int(stdscr.getstr(len(menu_text), len("Enter your choice: ")).decode("utf-8"))
            curses.noecho()
        except ValueError:
            continue

        if choice == 0:
            preload_data(USTH)
            stdscr.addstr(len(menu_text) + 1, 0, "Preloaded data successfully.")
        elif choice == 1:
            USTH.set_num_students(stdscr)
        elif choice == 2:
            USTH.set_num_courses(stdscr)
        elif choice == 3:
            USTH.input_students(stdscr)
        elif choice == 4:
            USTH.input_courses(stdscr)
        elif choice == 5:
            USTH.enter_mark(stdscr)
        elif choice == 6:
            USTH.list_students(stdscr)
        elif choice == 7:
            USTH.list_courses(stdscr)
        elif choice == 8:
            USTH.display_mark(stdscr)
        elif choice == 9:
            USTH.display_GPA(stdscr)
        elif choice == 10:
            stdscr.addstr(len(menu_text) + 2, 0, "Au revoir")
            stdscr.refresh()
            stdscr.getch()
            break
        else:
            stdscr.addstr(len(menu_text) + 1, 0, "Invalid choice. Please try again.")

        stdscr.refresh()
        stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(curses_main)
