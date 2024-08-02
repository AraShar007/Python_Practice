class Mammals:
    print("This is a class of mammals")
class Humans:
    print("THis is a class of humans")
class Offspring(Mammals, Humans):
    print("This class can give  birth to a child")
obj1 = Offspring()
