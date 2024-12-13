import curses
class OutputOutils:
    @staticmethod
    def show(list_items, stdscr):
        stdscr.clear()
        for i, item in enumerate(list_items):
            stdscr.addstr(i, 0, str(item))
        stdscr.refresh()
        stdscr.getch()