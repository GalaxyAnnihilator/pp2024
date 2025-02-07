import os
#Ex1
class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
    
    def display_info(self):
        print(f"Employee {self.id}: {self.name} - Salary: {self.salary}")

emp1 = Employee("Alice Johnson","E12345",5000)

#Ex2
class Manager(Employee):
    def __init__(self,name,id,salary,team):
        super().__init__(name,id,salary)
        self.team = team

    def display_team(self):
        print(f"Manager: {self.name}")
        print(f"Members: {self.team}")

    def display_info(self):
        print(f"Manager {self.id}: {self.name} - Salary: {self.salary} - Number of team members: {len(self.team)}")

#Ex3
    def save_to_file(self,filename):
        try:
            with open(filename,"w") as f:
                f.write(f"{self.name}\n{self.id}\n{self.salary}\n{self.team}")
        except IOError as e:
            print(e)
#Ex4
    def save_with_os(self,filename):
        command = f"echo '{self.name}\n{self.id}\n{self.salary}\n{self.team}' > {filename} &"
        os.popen(command)

mng1 = Manager("TranMinhDuong","M6789",100000,["A","B","C"])
mng1.display_info()
mng1.display_team()
mng1.save_with_os("manager_info.txt")