file = open("new_file.txt", "rt")
# print(file.read())

file1=open("C:\\Users\\Aravi Sharma\\Downloads\\demon slayer.txt")
# print(file1.read())

# to read only the parts of the file
print(file1.read(100))
print(file1.readlines())
# print(file.readline())
# print(file.readline())
for line in file:
    print(line)

# files should be closed when you are done with them as in some
# cases due to buffering , you may not be able to see the changes
# if the  file is not closed.

file.close()
file1.close()

#write
file= open("new_file.txt", "at+")
file.write("\nI am pursuing BTECH FROM SKIT COLlEGE IN JAIPOR, RAJASTHAN ")
print(file.read())
file.close()

file= open("new_file.txt", "wt+")
file.write("This message will overwrite the already existing message ")
print(file.read())
file.close()

# file=open("Text_File.txt", "x")

#  Deleting a file
import os
# os.remove("new_file.txt")

# to check if the file exists or not
# if os.path.exists("new_file.txt"):
#     print("file exists")
#     os.remove("new_file.txt")
# else:
#     print("File doesnt exists")

#removing a folder
os.mkdir("new_folder")
os.rmdir("new_folder")

#Basic python file handling.
# rest tommorrow
# file=open("Text_File.txt", "rb+")
# buffer= file.detach()
# file.close()
# buffer.close()