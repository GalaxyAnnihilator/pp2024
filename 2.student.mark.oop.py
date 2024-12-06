"""
Classes with their attributes + methods:

Person:
    Attributes: name, dob
    Methods: get_name, get_dob

Student: (inherited from Person)
    Attributes: id, name, dob, marks
    Methods: get_id, get_name, get_dob

Course:
    Attributes: id,name
    Methods: get_id, get_name

Utils:
    Methods: input_something(), show() - both use polymorphism

University:
    Attributes: num_stu, num_course, students, courses
    Methods: getters, setters, add_students, add_courses, enter_mark, load_students, load_courses, list_students, list_courses

"""

class Person:
    def __init__(self,name,dob):
        self.__name = name
        self.__dob = dob
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
class Student(Person):
    def __init__(self,id,name,dob,marks={}): #overloading the constructor
        super().__init__(name,dob)
        self.__id = id
        self.__marks = marks

    #getters
    def get_id(self):
        return self.__id

    def get_marks(self):
        return self.__marks
    
    #fill marks
    def fill_mark(self, course_id, point):
        self.__marks[course_id] = point

    #string display
    def __str__(self):
        return f"StudentID: {self.get_id()}, Name: {self.get_name()}, DoB: {self.get_dob()}"

class Course:
    def __init__(self,id,name):
        self.__id :str = id
        self.__name :str = name
    
    #getters
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    #string display
    def __str__(self):
        return f"CourseID: {self.get_id()}, Name: {self.get_name()}"


class Outils:
    def show(list):
        for instance in list:
            print(instance)

    def input_Integer(args) -> int:        
        return int(input(f"Enter the number of {args}: "))

class University:
    def __init__(self):
        self.__num_students : int = 0
        self.__num_courses : int = 0
        self.__students : list[Student] = []
        self.__courses : list[Course] = []

    #getters
    def get_num_students(self):
        return self.__num_students
    
    def get_num_courses(self):
        return self.__num_courses
    
    def get_students(self):
        return self.__students
    
    def get_courses(self):
        return self.__courses
    
    #setters
    def set_students(self, num):
        self.__num_students = num

    def set_courses(self, num):
        self.__num_courses = num    

    #setters through inputs
    def set_num_students(self):
        self.__num_students = Outils.input_Integer("students")

    def set_num_courses(self,):
        self.__num_courses = Outils.input_Integer("courses")

    #add students and courses
    def add_student(self):
        id = input("Enter the student's id: ")
        name = input("Enter the student's name: ")
        dob = input("Enter the student's dob: ")  
        self.__students.append(Student(id,name,dob))
    
    def add_course(self):
        id = input("Enter the course's id: ")
        name = input("Enter the course's name: ")
        self.__courses.append(Course(id,name))

    def input_students(self):
        if self.get_num_students() == 0:
            print("Please input the number of students first")  
        for _ in range(self.get_num_students()):
            self.add_student()

    def input_courses(self):
        if self.get_num_courses() == 0:
            print("Please input the number of course first")
        for _ in range(self.get_num_courses()):
            self.add_course()

    #preload some data - basically just setter methods :/
    def load_courses(self,courses):
        self.__courses = courses

    def load_students(self,students):
        self.__students = students 

    #enter marks or display marks for a specific course
    def enter_mark(self):
        course_id = input("Enter the course ID to input marks: ")
        course = None

        #search
        for c in self.__courses:
            if c.get_id() == course_id:
                course = c
                break
        
        if course is None:
            print("Course not found!")
            return
        
        print(f"Entering marks for course: {course.get_name()}")
        for student in self.__students:
            mark = float(input(f"Enter marks for student {student.get_name()} (ID: {student.get_id()}): "))
            student.get_marks()[course_id] = mark

    def display_mark(self):
        course_id = input("Enter the course ID to view marks: ")
    
        #search for the correseponding id
        course = None
        for c in self.__courses:
            if c.get_id() == course_id:
                course = c
                break

        if course is None:
            print("Course not found!")
            return
        print(f"Marks for course: {course.get_name()}")

        for student in self.__students:
            if course_id in student.get_marks():
                print(f"Student {student.get_name()} (ID: {student.get_id()}): {student.get_marks()[course_id]}")
            else:
                print(f"Student {student.get_name()} (ID: {student.get_id()}): No marks entered")

    #display
    def list_students(self):
        if not self.get_students():
            print("No students input yet")
            return
        
        print("Student list:")
        Outils.show(self.get_students())

    def list_courses(self):
        if not self.get_courses():
            print("No courses input yet")
            return

        print("Course list: ")
        Outils.show(self.get_courses())

def main():
    USTH = University()

    while True:
        print("\nOptions:")
        print("0. Load pre-entered data (highly recommended for the lazy guys)")
        print("1. Input number of students")
        print("2. Input number of  courses")
        print("3. Input students info")
        print("4. Input courses info")
        print("5. Enter mark of students in a specific course")
        print("6. Display all students")
        print("7. Display all courses")
        print("8. Display mark for a specific course")
        print("9. Exit\n")   

        choice = int(input("Enter your choice: "))
        if choice == 0:
            pre_entered_students:list[Student] = [
                Student("S001","An","12/01/2000",{"C001": 15.0, "C002": 19.0}),
                Student("S002","Binh","30/12/2005",{"C001": 18.0}),
                Student("S003","Cuong","03/03/2004",{"C002": 20.0})
            ]

            pre_entered_courses:list[Course] = [
                Course("C001","Python"),
                Course("C002","OOP")
            ]
            USTH.set_courses(len(pre_entered_courses))
            USTH.set_students(len(pre_entered_students))
            USTH.load_courses(pre_entered_courses)
            USTH.load_students(pre_entered_students)
            print("Successfully loaded")
        elif choice == 1:
            USTH.set_num_students()
        elif choice == 2:
            USTH.set_num_courses()
        elif choice == 3:
            USTH.input_students()
        elif choice == 4:
            USTH.input_courses()
        elif choice == 5:
            USTH.enter_mark()
        elif choice == 6:
            USTH.list_students()
        elif choice == 7:
            USTH.list_courses()
        elif choice == 8:
            USTH.display_mark()
        elif choice == 9:
            print("Au revoir")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
 
