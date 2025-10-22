table = [[] for _ in range(0,10)]

def getKeyIndex(data):
    return hash(data) % len(table)

def add(key, value):
    index = getKeyIndex(key)
    table[index].append([key, value])

def get(key):
    index = getKeyIndex(key)
    for pair in table[index]:
        if pair[0] == key:
            return pair[1]

def delete(key):
    index = getKeyIndex(key)
    for pair in table[index]:
        if pair[0] == key:
            table[index].remove(pair)



add("Shani", 10)
add("Shiwansh", 20)
add("Pramod", 30)
add("Subhashana", 40)
add("Anjali", 50)
print(table)
print(get("Shiwansh"))

delete("Shiwansh")

print(table)

