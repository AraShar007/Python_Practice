class Living_beings:
    def __init__(self):
        print("parent's init")
    def breath(self):
        print("Living beings breath")
class Humans(Living_beings):
    def __init__(self):
        print("humans init")
    def talk(self):
        print("Humans can talk")
class Females(Humans):
    def reproduce(self):
        print("females can reproduce")
fem_obj = Females()
fem_obj.talk()
fem_obj.breath()
fem_obj.reproduce()