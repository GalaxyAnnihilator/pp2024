import zipfile, os, numpy as np
from input import InputOutils
from output import OutputOutils
import pickle, gzip

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
        return f"StudentID: {self.get_id()}, Name: {self.get_name()}, DoB: {self.get_dob()}"

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
        self.__num_students = InputOutils.input_integer("Enter the number of students: ", stdscr)

    def set_num_courses(self, stdscr):
        self.__num_courses = InputOutils.input_integer("Enter the number of courses: ", stdscr)

    #preload some data - basically just setter methods :/
    def load_courses(self,courses):
        self.__courses = courses

    def load_students(self,students):
        self.__students = students 


    def add_student(self, stdscr):
        id = InputOutils.input_string("Enter the student's ID: ", stdscr)
        name = InputOutils.input_string("Enter the student's name: ", stdscr)
        dob = InputOutils.input_string("Enter the student's DoB: ", stdscr)
        self.__students.append(Student(id, name, dob))

    def add_course(self, stdscr):
        id = InputOutils.input_string("Enter the course's ID: ", stdscr)
        name = InputOutils.input_string("Enter the course's name: ", stdscr)
        credits = InputOutils.input_integer("Enter the course's credits: ", stdscr)
        self.__courses.append(Course(id, name, credits))

    def input_students(self, stdscr):
        if self.get_num_students() == 0:
            stdscr.addstr(0, 0, "Please input the number of students first.")
            stdscr.refresh()
            stdscr.getch()
            return

        for _ in range(self.get_num_students()):
            self.add_student(stdscr)

        OutputOutils.writeToFile(self.get_students(),"students.txt")

    def input_courses(self, stdscr):
        if self.get_num_courses() == 0:
            stdscr.addstr(0, 0, "Please input the number of courses first.")
            stdscr.refresh()
            stdscr.getch()
            return

        for _ in range(self.get_num_courses()):
            self.add_course(stdscr)

        OutputOutils.writeToFile(self.get_courses(),"courses.txt")    

    def enter_mark(self, stdscr):
        course_id = InputOutils.input_string("Enter the course ID to input marks: ", stdscr)
        course = next((c for c in self.__courses if c.get_id() == course_id), None)

        if not course:
            stdscr.addstr(0, 0, "Course not found!")
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.addstr(1, 0, f"Entering marks for course: {course.get_name()}")
        for student in self.__students:
            prompt = f"Enter marks for student {student.get_name()} (ID: {student.get_id()}): "
            mark = float(InputOutils.input_string(prompt, stdscr))
            student.get_marks()[course_id] = mark    

        OutputOutils.write_marks_to_file(self, "marks.txt")    

    def display_mark(self, stdscr):
        course_id = InputOutils.input_string("Enter the course ID to view marks: ", stdscr)
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
        OutputOutils.show(self.get_students(), stdscr)

    def list_courses(self, stdscr):
        if not self.get_courses():
            stdscr.addstr(0, 0, "No courses input yet.")
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.addstr(0, 0, "Course list:")
        OutputOutils.show(self.get_courses(), stdscr)

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

    def load_data_from_compressed_file(self, compressed_file="students.dat"):
        # Resolve the path to the compressed file and extraction folder
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.data_folder = os.path.join(self.base_path, "data")
        
        compressed_path = os.path.join(self.base_path, compressed_file)
        extraction_folder = self.data_folder
        
        # Ensure the extraction folder exists
        if not os.path.exists(extraction_folder):
            os.makedirs(extraction_folder)

        # Check if the compressed file exists
        if os.path.exists(compressed_path):
            with zipfile.ZipFile(compressed_path, "r") as zipf:
                for member in zipf.namelist():
                    # Extract only the file name to avoid nested folders
                    filename = os.path.basename(member)
                    if filename:  # Skip directories
                        source = zipf.open(member)
                        target_path = os.path.join(extraction_folder, filename)
                        with open(target_path, "wb") as target:
                            target.write(source.read())
                
                # Load data from extracted files
                self.load_courses_from_file(os.path.join(extraction_folder, "courses.txt"))
                self.load_students_from_file(os.path.join(extraction_folder, "students.txt"))
                self.load_marks_from_file(os.path.join(extraction_folder, "marks.txt"))

                return f"Data successfully extracted from {compressed_path}."
        else:
            return f"{compressed_path} not found. Starting fresh."

    def load_courses_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split(", ")
                    course_id = parts[0].split(": ")[1]
                    name = parts[1].split(": ")[1]
                    credits = int(parts[2].split(": ")[1])
                    self.__courses.append(Course(course_id, name, credits))
        except FileNotFoundError:
            print(f"{filename} not found. No courses loaded.")

    def load_students_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split(", ")
                    student_id = parts[0].split(": ")[1]
                    name = parts[1].split(": ")[1]
                    dob = parts[2].split(": ")[1]
                    self.__students.append(Student(student_id, name, dob))
        except FileNotFoundError:
            print(f"{filename} not found. No students loaded.")

    def load_marks_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                current_course = None
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    # Detect course name
                    if not line.startswith("Student") and ":" not in line:
                        current_course = next(
                            (c for c in self.__courses if c.get_name() == line), None
                        )
                    else:
                        # Parse student marks
                        name, mark = line.split(": ")
                        student = next(
                            (s for s in self.__students if s.get_name() == name),
                            None,
                        )
                        if current_course and student:
                            student.get_marks()[current_course.get_id()] = float(mark)
        except FileNotFoundError:
            print(f"{filename} not found. No marks loaded.")

    def load_pickle(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        if os.path.basename(current_dir) == "pw6":
            data_file_path = os.path.join(current_dir, "data.pkl.gz")
        else:
            data_file_path = os.path.join(current_dir, "pw6", "data.pkl.gz")

        with gzip.open(data_file_path, "rb") as file:
            loaded_students, loaded_courses = pickle.load(file)
            self.set_courses(len(loaded_courses))
            self.set_students(len(loaded_students))
            self.load_courses(loaded_courses)
            self.load_students(loaded_students)
            return f"Data successfully extracted from data.pkl.gz"