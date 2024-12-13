import curses
from output import OutputOutils
class InputOutils:

    def preload_data(university, pre_entered_courses, pre_entered_students):
        university.set_courses(len(pre_entered_courses))
        university.set_students(len(pre_entered_students))
        university.load_courses(pre_entered_courses)
        university.load_students(pre_entered_students)
        OutputOutils.writeToFile(university.get_students(),"students.txt")
        OutputOutils.writeToFile(university.get_courses(),"courses.txt")    
        OutputOutils.write_marks_to_file(university, "marks.txt")  
        OutputOutils.compress_data()  

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
                user_input = InputOutils.input_string(prompt, stdscr)
                return int(user_input)
            except ValueError:
                stdscr.addstr(2, 0, "Invalid input. Please enter an integer.")
                stdscr.refresh()
                stdscr.getch()
