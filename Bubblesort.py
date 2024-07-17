list1 = [67,89,3,5,99,12]
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] >= list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)