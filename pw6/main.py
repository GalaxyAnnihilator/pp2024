from input import InputOutils
from output import OutputOutils
from domains import Student, Course, University
import curses

def curses_main(stdscr):
    USTH = University()

    #attempt to load from pickle file
    message = USTH.load_pickle()

    # Clear screen
    stdscr.clear()
    # Menu options
    menu_text = [
        message,
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

        if choice == 1:
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