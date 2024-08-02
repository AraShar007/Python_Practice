class add:
    first_num = 0
    second_num = 0
    result = 0
    def __init__(self, num1, num2):
        self.first_num = num1
        self.second_num = num2
    def display(self):
        print("First number = " ,self.first_num)
        print("Second number = " ,self.second_num)
        print("add of two numbers = " ,self.result)

    def calculate(self):
        self.result = self.first_num + self.second_num

obj1 = add(1000, 2000)

# creating second object of same class
obj2 = add(10, 20)

# perform add on obj1
obj1.calculate()

# perform add on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()
