# From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("numbers.txt", "r") as file:
    data = file.read()
    print(data)
    num = data.split(sep=',')
    print(num)
    for val in num:
        if int(val) % 2 == 0 :
            count += 1
    print(count)



