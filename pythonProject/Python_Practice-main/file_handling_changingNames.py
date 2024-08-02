# WAF that replace all occurrences of “aravi” with “hermoine” in above file.
with open("name.txt", "r+") as file:
    data = file.read()
    replaced_data = data.replace('aravi', 'hermoine')
    print(replaced_data)
    file.seek(0)
    file.write(replaced_data)

