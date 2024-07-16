#This is a practice code for variables in Python. 
a = "07-02-2003"
b = 21
print("Aravi's bday is on", a, "and she is", b, "years old")

x = 7
print(type(x))
x = "seven"
print(type(x))

# casting
x = str(3)
y = int(3)
z = float(3)
print(x, type(x))
print(y, type(y))
print(z, type(z))

# allowed variable names
myvar = "JK"
my_var = "V"
_my_var = "jimin"
myVar = "jin"
MYVAR = "jhope"
myvar2 = "rm"
Myvar = "yoongi"
_my_var = "aravi"

F1, F2, F3 = "apple", "banana", "cherry"
print(F1, F2, F3)
F1 = F2 = F3 = "apple"
print(F1, F2, F3)

dob = ["07", "02", "2003"]
X, Y, Z = dob
print(X, Y, Z)

#output variables
x = "aravi is awesome"
print(x)
x = "aravi"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)
a = 10
b = 8
print(a + b)
a = 10
b = "ara"
print(b, a)
# print(b+a) error TypeError: unsupported operand type(s) for +: 'int' and 'str'
#global variables 

def game():
  print("her favourite game is " , a)
  # a="basketball" throws error
game()
print("she likes to play", a )
#global keyword
def global_keyword():
  global sport
  sport = "cricket"
global_keyword()
print("her favourite game is " , sport)

fav1="ice hockey"
def fav_game():
  global fav1
  fav1="badminton"
fav_game()
print("her favourite childhood game is " + fav1)
x = ["apple", "banana", "cherry"]
print(type(x))
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))