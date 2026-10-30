n = 8
prev1 = 0
prev2 = 1

for i in range(n):
    curr = prev1 + prev2
    prev1 = prev2
    prev2 = curr

print(prev2)
