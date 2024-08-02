list = [x for x in input("Enter the elements").split()]
print(list)

uniq_item = []
dup_item = set()
for x in list:
    if x not in dup_item:
        uniq_item.append(x)
        dup_item.add(x)
print(dup_item)
print(uniq_item)

