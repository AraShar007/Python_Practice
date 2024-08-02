student = {
   "name": "Peter Parker",
    "aliases" : "Spider man",
    "abilities" : {
        "dance" : -100,
        "basketball": 90,
        "climb": 100
    },
    "is_human": True
}
print(student)
print(student["abilities"]["dance"])
print(student.keys())
print(student["abilities"].keys())
print(len(student))
print(list(student.keys()))

print(student.values())
print(student.items())

print(student.get("name2"))    # No error if the key is not present just returns none
# print(student["name2"])      # returns an error as we are accessing an invalid key
new_student = {
    "name" : "Harry Potter ",
    "aliases" : "The Chosen One",
    "house" :"gryffindor"
}
student.update(new_student)
print(student)