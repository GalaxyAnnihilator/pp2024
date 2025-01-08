class Number:
    def min(a: float, b:float):
        return a if a<b else b
    def min(a: int, b:int):
        return a if a<b else b

a = 1
b = 2
c = 3.5
d = 4.7
print(Number.min(a,b))
print(Number.min(c,d))