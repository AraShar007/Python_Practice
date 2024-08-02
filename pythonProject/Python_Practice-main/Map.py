# # Python program to demonstrate working
# # of map.
# #
# # Return double of n
# def addition(n):
#     return n + n
#
# # We double all numbers using map()
# class myMap(map):
#     def __str__(self):
#         return "Hi"
# numbers = (1, 2, 3, 4)
# result = myMap(addition, numbers)
# print((result))
t = (1, [2,3])
try:
    t[1] += [7,8]
except Exception as e:
    print(e)
finally:
    print(t)