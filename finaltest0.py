import threading
class Character:
    def __init__(self,name,level,health):
        self.name = name
        self.level = level
        self.health = health

c1 = Character("Stone Giant",1,780)

class PlayerCharacter(Character):
    def __init__(self,name,level,health,inventory):
        super().__init__(name,level,health)
        self.inventory = inventory

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, Health: {self.health}, Inventory: {self.inventory}"

    def save(self,filename):
        try:
            with open(filename,"w") as f:
                f.write(self.name+"\n")
                f.write(str(self.level)+"\n")
                f.write(str(self.health)+"\n")
                f.write(str(self.inventory)+"\n")
        except IOError as e:
            print(e)

    def save_in_background(self,filename):
        t = threading.Thread(target=self.save,args=(filename,))
        t.start()

c2 = PlayerCharacter("Duong",1,100,"Apple")
print(c2)
c2.save_in_background("player.txt")        

