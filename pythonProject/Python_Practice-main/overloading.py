class Family:
    def man(self):
        print("This is a man function")
    def woman(self):
        print("This is a Woman function")

class Child(Family):
    def man(self, name = ''):
        print("This is class 2 man function",name)
    def woman(self, hair_color = ''):
        print(f"This is {hair_color} colored woman")

obj = Child()
obj1= Family()

obj1.man()
obj.man('Ellis')
obj1.woman()
obj.woman('Red')
