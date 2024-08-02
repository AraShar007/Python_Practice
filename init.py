# When we add the __init__() function in a parent class, the child class will no longer be able to
# inherit the parent class’s __init__() function.
# The child’s class __init__() function overrides the parent class’s __init__() function.
class Parent1:
    def __init__(self , fname, fage):
        self.firstname = fname
        self.age = fage
    def display(self):
       print(self.firstname , self.age)
class Child1(Parent1):
      def __init__(self , fname , fage):
            Parent1.__init__(self, fname, fage)
            self.lastname = "Miller"
      def display(self):
            print("Student" , self.firstname,self.lastname, "is"  ,self.age , "years old")
ob = Child1("Maddy" , '28')
ob.display()