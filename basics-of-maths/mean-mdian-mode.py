x = [50, 70, 70, 80, 90, 100, 100, 100, 110, 120]
n = len(x)

# Mean
mean = sum(x) / n
print("Mean:", mean)

# Median
x.sort()
if n % 2 == 0:
    median = (x[n//2 - 1] + x[n//2]) / 2    
else:
    median = x[n//2]
print("Median:", median)

# Mode
from collections import Counter 
mode = Counter(x).most_common(1)[0][0]
print("Mode:", mode)