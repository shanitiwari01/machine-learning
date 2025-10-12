list = [1,2,3]

# Add at the end
list.append(4)
print(list)

# Insert at postion
list.insert(0, 0)
print(list)

# Remove by element
list.remove(4)
print(list)

# Remove from the end
list.pop()
print(list)

# Find lowest value

min = list[0]
for x in list:
    if x < min:
        min = x

print(min)