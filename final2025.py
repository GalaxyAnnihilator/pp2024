"""
Tank class:
- Attributes: HP, Damage, Armor, Price
- Implement all getters and setters
- display(): Display info about the tanks
- compute_strength(): strength = sqrt(HP**2+Damage**2+Armor**2)

input_handle(): Read a list of tanks info from input.txt, the file looks like this:
4
5 5 5 20
3 8 9 15
10 20 9 45
20 10 30 30

Tasks:
- Task 1: Sort the tanks by prices so user can buy the most tanks with 75 coins
- Task 2: Sort the tanks by strength descending so user can buy the most with 75 coins
- Using threading and return the results as array of tank indexes (the line which the tank's info belong)

output_handle(): perform both tasks above and write the result to the file output.txt as follow:
[2,3,1]
[1,2,3]

Assemble everything in the main() function
"""
import threading
class Tank:
    def __init__(self,HP,D,A,Price):
        self.HP = HP
        self.D = D
        self.A = A
        self.Price = Price
    def getHP(self):
        return self.HP
    def setHP(self,HP):
        self.HP = HP
    def getD(self):
        return self.D
    def setD(self):
        return self.D
    def getA(self):
        return self.A
    def setA(self,A):
        self.A = A
    def getPrice(self):
        return self.Price
    def setPrice(self,Price):
        self.Price = Price

    def display(self):
        print(f"Tank: {self.HP} HP, {self.D} Damage, {self.A} Armor, Price: {self.Price}")
    def compute_strength(self):
        return (self.HP**2 + self.A**2 + self.D**2)**0.5

def input_handle(file):
    try:
        with open(file,'r') as f:
            n = int(f.readline())
            tanklist = []
            for l in f.readlines():
                HP,D,A,Price = [int(i) for i in l.split()]
                tanklist.append(Tank(HP,D,A,Price))
    except Exception as e:
        print(e)

    return tanklist    

def buybyPrice(tanklistIndexed,result1=[]):
    gold = 75
    sortbyPrice = sorted(tanklistIndexed,key=lambda x: x[1].Price)
    for x in sortbyPrice:
        if gold >= x[1].Price:
            result1.append(x[0])
            gold-=x[1].Price

    return result1  

def buybyStrength(tanklistIndexed,result2=[]):
    gold = 75
    sortbyStrength = sorted(tanklistIndexed,key=lambda x: x[1].compute_strength(),reverse=True)
    # print(sortbyStrength)
    for x in sortbyStrength:
        if gold >= x[1].Price:
            result2.append(x[0])
            gold-=x[1].Price
            
    return result2   

def output_handle(file,result1,result2):
    try:
        with open(file,"w") as f:
            f.write(f"{result1}\n")
            f.write(f"{result2}")
    except Exception as e:
        print(e)        
    
def main():
    tanklist = input_handle("input.txt")
    tanklistIndexed = [(i+1,tank) for (i,tank) in enumerate(tanklist)]
    result1 = []
    result2 = []
    t1 = threading.Thread(target=buybyPrice,args=(tanklistIndexed,result1,))
    t2 = threading.Thread(target=buybyStrength,args=(tanklistIndexed,result2,))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    output_handle("output.txt",result1,result2)

main()