with open("seekText.txt", "rb") as file:
    print(file.readlines())
    # file.seek(0)
    print(file.tell())
    # file.seek(10,0)
    file.seek(-10,2)
    print(file.tell())