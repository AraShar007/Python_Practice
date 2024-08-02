
list1 = [x for x in input("Enter elements of list1 ").split()]
list2 = [y for y in input("Enter elements of list2").split()]
def common(list1, list2):
    flag = False
    for i in list1:
        for j in list2:
            if i == j:
                flag = True
    if flag == True:
        return True
    else:
        return False
print(common(list1, list2))


