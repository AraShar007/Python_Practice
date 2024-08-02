class Humans:
    def walk(self):
        can_walk = True
class Males(Humans):
    def talk(self):
        can_talk = True
class Females(Humans):
    def reproduce(self):
        can_birth = True
        can_talk = True

f1 = Females()
m1 = Males()
f1.walk()
f1.reproduce()
m1.walk()
m1.talk()
print(type(Humans)) # Shows that Humans itself is a class object created by the metaclass type.
print(type(Humans())) #Shows that Humans() is an instance of the Humans class.
print(type(f1))


