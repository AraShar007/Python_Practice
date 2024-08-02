find_max=lambda a,b,c:a if a>b and a>c else (b if b>a and b>c else c)
print(find_max(6,15,1))