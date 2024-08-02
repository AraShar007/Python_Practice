# Tuples- ordered, unchangeable, allow duplicates
my_tuple = ("jin", "jimin", "rm", "jhope", "yoongi", "V", "JK", "jimin")
print(my_tuple, "\nlen:", len(my_tuple))
Atupple = ("harry", )
print(type(Atupple))
NotTupple = ("harry")
print(type(NotTupple))
tuple_new = ("Harry", "Potter", 22, 9.75)
print(type(tuple_new))

new_tup = tuple(("Nezuko", "Zenitsu", "Genya", "Tanjiro", "Inosuke"))
print(new_tup)
print(new_tup[3])
print(new_tup[-3])
print(len(new_tup))
print(new_tup[2:5])
print(new_tup[:3])
print(new_tup[3:])
print(new_tup[-4:-1])
if "Nezuko" in new_tup:
    print("we have nezuko here")

# tuples-> list-> make changes ->updated list-> tuple
updation = list(new_tup)   # converting to list
# doing changes
updation.insert(2, "Kanao")
updation.append("Murata")
print(updation)
# back to tuple
updation = tuple(new_tup)

#adding tuple to a tuple
add_demon=("Muzan", "Rui", "Akaza", "Doma", "Nakime", "Daki")
add_demon += new_tup
print(add_demon)

#tuples are unchangeable, items can't be removed. But convert it into list and then we can modify
list_of_demons = list(add_demon)
list_of_demons.remove("Daki")
add_demon = tuple(list_of_demons)
print("Daki is dead:\n" ,add_demon)

# sample_tuple = ("this", "is", "a", "sample", "tuple")
# del sample_tuple
# print(sample_tuple) # error because the tuple no longer exists

# ----------------------------

# UNPACK TUPLES
# assigning values to a tuple is k/a packing
houses= ("gryffindor", "ravenclaw", "hufflepuff" , "slytherin", "Beauxbatons", "Durmstrang", "Ilvermorny")
godric, rowena, *helga, salazar = houses
print(f"{godric}\t{rowena}\t{helga}\t{salazar}")
# print(godric)
# print(rowena)
# print(helga)
# print(salazar)

# --------------------------
# Loops
# For loop
for char in houses:
    print(char)

print("_________")
for char in houses:
    if "i" in char:
        print(char)

print("______")
for item in range(len(houses)):
    print(houses[item])

print("______")
# while loop
i=2
while(i<len(houses)):
    print(houses[i])
    i += 1

# ---------------------
# join 2 tuples
country=("India", "Pakistan", "Afghanistan", "Canada", "Hungary")
city=("Jaipur","Delhi", "Lahore", "Karachi", "Toronto", "J&K")
join= country + city
print(join)
print(city+country)

# mutliplying
print(country*2)

# count and index
num=(0,7, 2,4,6,7,8,10, 6,7,8,9)
print(num.count(7))
print(num.index(6))

