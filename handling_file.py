# to count no of lines in a text file
# use readlines()
# with open("Text_File.txt", "r")as file:
#     # print(file.readlines())
#     num_of_line = len(file.readlines())
#     print("No of lines:", num_of_line)
#
#using for loop
with open("Text_File.txt", "rt") as file:
    num_of_line=0
    for line in file:
        num_of_line += 1
    print("No of lines:", num_of_line)



