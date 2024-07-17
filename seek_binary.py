with open("seekText.txt","rb") as file:
    print(file.readlines())
    # file.seek(0)
    print(file.tell())
    file.seek(10,0)
    print(file.tell())
    file.write("new")

    # print(file.readline().decode('utf-8'))
    # file.close()