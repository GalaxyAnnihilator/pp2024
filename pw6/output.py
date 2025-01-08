import zipfile, os 

class OutputOutils:
    global base_path
    base_path = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def show(list_items, stdscr):
        stdscr.clear()
        for i, item in enumerate(list_items):
            stdscr.addstr(i, 0, str(item))
        stdscr.refresh()
        stdscr.getch()

    @staticmethod
    def writeToFile(list_items, fileDestination):
        # Combine the base path with the relative destination
        full_path = os.path.join(base_path, fileDestination)
        with open(full_path, 'w') as f:
            for i in list_items:
                f.write(str(i) + '\n')

    def write_marks_to_file(uni, filename="marks.txt"):
        full_path = os.path.join(base_path, filename)
        with open(full_path, 'w') as f:
            for course in uni.get_courses():
                f.write(f"{course.get_name()}\n")
                for student in uni.get_students():
                    marks = student.get_marks()
                    if course.get_id() in marks:
                        f.write(f"{student.get_name()}: {marks[course.get_id()]}\n")
                f.write("\n")

    def compress_data(self, output_filename="students.dat"):
        # Files to compress
        files_to_compress = ["marks.txt", "students.txt", "courses.txt"]
        # Create full paths for all files
        files_to_compress = [os.path.join(self.base_path, file) for file in files_to_compress]
        output_path = os.path.join(self.base_path, output_filename)
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in files_to_compress:
                zipf.write(file, os.path.basename(file))  # Store files without their full path