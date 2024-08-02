class add:
    first_num = int(input("Enter first num "))
    second_num = int(input("Enter second num "))
    result = 0
    def __init__(self):
        num1 = self.first_num
        num2 = self.second_num
        self.result = num1+num2
        print(f"The sum of {num1} and {num2} is {self.result}")
obj_add = add()
