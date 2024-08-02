set1 = {1, 3, 3, 7, 5, 2, 1, 4}
# sets are mutable but its elements are immutable
myset = set()
myset.add(3)
myset.add(7)
myset.add(7)
print(myset)
myset.remove(7)
print(myset)
# myset.remove(8)   # will give key error
myset.add("aravi")
myset.add((1,3,4))
print(myset)
print(len(myset))
# myset.add([1,2,3])  # TypeError: unhashable type: 'list'
myset.clear()
print(myset)
print(len(myset))
set1.pop()
print(set1)
set1.pop()
print(set1)
set_a = {"Aravi", "Jaipur", 21, 5.3, "Female"}
set_b = {"Sharma", "Jaipur", 21, 5.8, "Male"}
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_b.intersection(set_a))
