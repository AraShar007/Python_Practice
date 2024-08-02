# Write a recursive function to print all elements in a list. use list and index as parameters

n = input("Enter the elements separated by space: ")
def print_ele(list, i= 0):
    if i == len(list):
        return
    print(list[i], end=' ')
    print_ele(list, i+1)
print_ele(n)




