import threading
#Ex1
class LibraryBook:
    def __init__(self,title,author,available):
        self.title = title
        self.author = author
        self.available = available
    
    def borrow(self):
        if (self.available):
            print("Successfully borrowed")
            self.available = False
        else:
            print("Failed, book is already borrowed")

book1 = LibraryBook("1984","George Owell",True)
#Ex2
class SpecialEditionBook(LibraryBook):
    def __init__(self,title,author,available,extras):
        super().__init__(title,author,available)
        self.extras = extras

    def borrow(self):
        if (self.available):
            print("Successfully borrowed")
            print(f"Extras: {self.extras}")
            self.available = False
        else:
            print("Failed, book is already borrowed")
#Ex3
    def save_to_file(self,filename):
        try:
            with open(filename,"w") as f:
                f.write(f"{self.title}\n{self.author}\n")
                if (self.available):
                    f.write("Available\n")
                else:
                    f.write("Borrowed\n")    
                f.write(f"{self.extras}")
        except IOError as e:
            print(e)
#Ex4
    def save_in_background(self,filename):
        t = threading.Thread(target=self.save_to_file,args=(filename,))
        t.start()
        t.join()

book2 = SpecialEditionBook("Harry Potter","JKRowling",True,["Good book"])
book2.save_in_background("book_info.txt")