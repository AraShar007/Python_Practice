x = input("Enter the no")
n = len(x)
# print(n)
sum = 0
for i in range(n):
    sum += int(x[i])**n
# print(sum)
if (sum == int(x)):
    print(f"{x} is an armstrong no")
else:
    print(f"{x} is NOT an armstrong no")
