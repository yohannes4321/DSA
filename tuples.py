# Read the length of the tuple (not used further)
leng = int(input())

# Read the input numbers, map them to integers, and convert to a tuple
num = map(int, input().split(" "))
nm = tuple(num)

# Print the hash of the tuple
print(hash(nm))
