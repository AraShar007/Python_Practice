def remove_line(fileName, specific_line):
    with open(fileName, 'r+') as read_file:
        lines = read_file.readlines()

    currentLine = 1
    with open(fileName, 'w') as write_file:
        for line in lines:
            if currentLine == specific_line:
                pass
            else:
                write_file.write(line)
            currentLine += 1


# call the function, passing the file and line to skip
remove_line("Del_file.txt", 2)

