# method overloading
class details:
    def person(self):
        print("this is a person")
        print("default function")
    def person(self, name= ' '):
        print("this is a person named" ,name)
        print("One parameter")
    def person(self,name= ' ', age= ' '):
        print("this is a person named and aged", name, age)
        print("two parameter")
person_object = details()
person_object.person()
person_object.person("Aravi")
person_object.person("Aravi", 21)
