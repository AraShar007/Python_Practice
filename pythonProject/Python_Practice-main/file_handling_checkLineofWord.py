# WAF to find in which line of the file does the word “learning” occur first.
# Print -1 if word not found.
def check_line():
    word = "learning"
    data = True
    lineNo = 1
    with open("myfile.txt", "r") as file:
        while data:
            data = file.readline()
            if(word in data):
                print(lineNo)
                return    # only returns first occurence
            lineNo += 1
    print(-1)
check_line()

