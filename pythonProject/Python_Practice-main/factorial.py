# using loops
n = int(input("Enter the number: "))
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)
factorial(n)

# using recursion
def fact(n):
    if n== 0 or n == 1:
        return 1
    else:
        print(n * fact(n-1))
# print(fact(n))
