# Search if the word “learning” exists in the file or not.
with open("myfile.txt", "r") as file:
    data = file.read()
    if "learning" in data:
        print("library exists in data")
    else:
        print("library doesn't exist in data")
