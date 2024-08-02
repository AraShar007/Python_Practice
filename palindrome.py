a= input("enter string: ")

def pallindrome(a):
    x = len(a)
    for i in range(x//2):
        if(a[i] == a[x-i-1]):
            return True
if(pallindrome(a)):
    print("Pallindrome")
else:
    print("not")
