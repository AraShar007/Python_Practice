# nested loops

# multiplication table

for i in range(1,11):
    for j in range(2,3):
        print(f"{i}*{j} =",i*j)

#---------------------------------------------------

#finding a number is prime or not
#
num = int(input("enter the number you want to check for:"))
for i in range(2,num):  # upto num-1
    if num % i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")

#---------------------------------------------------

#finding prime nos in a range
lr= int(input("Enter the lower range"))
ur = int(input("Enter the upper range"))
if (ur> lr and lr>1):
    for num in range(lr, ur+1):  # from lr to ur
        for i in range(2, num):
            if(num%i ==0):
                break
        else:
            print(f"{num} is prime")

#---------------------------------------------------

