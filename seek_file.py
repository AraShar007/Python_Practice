# python seek() function

#file = open("seekText.txt", "x")
file = open("seekText.txt", "r")
file.seek(20)
print(file.tell())
# print(file.readlines())
file.seek(0)
print(len(file.readlines()))
file.close()