# explicit typecasting:
str1="77"
num1=7
str_num= int(str1)
print (str_num, type(str_num))
sum = str_num+num1;
print(sum)

# Python automatically converts
# a to int
a = 7
print(type(a))

# Python automatically converts b to float
b = 3.0
print(type(b))

# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))