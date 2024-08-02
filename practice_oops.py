# class Dog:
#     pass
# a = Dog()
# b = Dog()
# print(a, b)
class Car:
    company = "Tata Motors"

    def __init__(self, name, color):
        self.name = name
        self.color = color

    # def description(self):
    def __str__(self):
        return f"{self.name} is {self.color} colored"

    def wheels(self, num_of_wheel):
        return f"{self.name} has {num_of_wheel} wheels"



car_obj1 = Car("Nano", "White")
print(car_obj1.company)
# print(car_obj1.description())
print(car_obj1.wheels(4))
# car_obj2 = Car("I20", "Black")
# car_obj2.company = "Maruti"
# print(car_obj2.company)
# print(car_obj2.description())
# print(car_obj2.wheels(5))
# print(car_obj1.company)
print(car_obj1)
# print(car_obj2.__str__())