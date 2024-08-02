info ={

    "name": "Aravi Sharma",
    "age" : 21,
    "branch" : "AI",
    "roll no": 24,
    "height": 5.3,
    "is_female": True,
    "subjects": ["python", "Networking", "Sql", "C++", "C"]
}
print(info)
print(type(info))
print(info["name"])
print(info["branch"])
info["height"] = 5.4
info["books"] = ("harry potter", "pride & prejudice", "little women")
print(info["height"])
print(info["books"])

dict ={}
dict["description"] = "it was a null dictionary"
print(dict)
