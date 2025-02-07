import subprocess
class Task:
    def __init__(self,name,priority,completed):
        self.name = name
        self.priority = priority
        self.completed = completed
    
    def mark_complete(self):
        self.completed = True
        print("Task completed!")

t1 = Task("Submit project",2,False)

class RecurringTask(Task):
    def __init__(self,name,priority,compelted,frequency):
        super().__init__(name,priority,compelted)
        self.frequency = frequency
    
    def mark_complete(self):
        self.completed = True
        print(f"Task completed! Repeating {self.frequency}")

    def save_to_file(self,filename):
        try:
            with open(filename,"w") as f:
                f.write(f"Name: {self.name}\n")
                f.write(f"Priority: {self.priority}\n")
                f.write(f"Completed: {self.completed}\n")
                f.write(f"Frequency: {self.frequency}")
        except Exception as e:
            print(e)
    
    def save_with_subprocess(self,filename):
        with open(filename,"w") as f:
            p = subprocess.Popen(["tee"],stdin=subprocess.PIPE,stdout=f,text=True)
            p.communicate(f"Name:{self.name}\nPriority:{self.priority}\nCompelted:{self.completed}\nFrequency:{self.frequency}")

t2 = RecurringTask("Feed the dog",4,False,"daily")
t2.mark_complete()
t2.save_with_subprocess("task_info.txt")