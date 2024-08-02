def func(key):
    return key[2]

aList = ['123', 'xyz', 'zara', 'abc', 'xyz']
aList.sort(key=func)
print("List : ", aList)

#reverse is set to True
aList.sort(reverse=True, key=func)
print("List : ", aList)