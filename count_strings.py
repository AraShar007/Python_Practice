#  Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more
#  and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
list = [x for x in input("Enter the strings").split()]
print(list)
count = 0
for x in list:
    if (len(x) >= 2 and x[0] == x[-1]):  # strings -> x
        count +=1
print(count)


