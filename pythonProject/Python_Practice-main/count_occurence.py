# Python3 code to program to find occurrence
# to each character in given string

# initializing string
inp_str = input("Enter the string")

# frequency dictionary
freq = {}

for ele in inp_str:
	if ele in freq:
		freq[ele] += 1
	else:
		freq[ele] = 1

# printing result
print ("Occurrence of all characters in GeeksforGeeks is :\n ", freq)
