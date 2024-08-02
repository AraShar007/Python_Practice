class Batch:
    age =  "20"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"{self.name} of age {self.age} has scored {self.marks} marks")

    @classmethod
    def update_age(cls, age):
        cls.age = age

    @staticmethod
    def check_marks(marks):
        if marks in range(90,100):
            print("First Grade")
        elif marks in range(80,90):
            print("Second Grade")
        else:
            print("Promoted")

student1 = Batch("Vani", 97)
student2 = Batch("Shani", 86)
student1.update_age(25)
student1.display()
student1.check_marks(97)
student2.display()
student2.check_marks(86)

