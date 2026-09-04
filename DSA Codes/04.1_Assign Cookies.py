child = [2,6,8,14]
cookie = [4,2,7,1,2,3]

child.sort()   # [2, 6, 8, 14]
cookie.sort()  # [1, 2, 2, 3, 4, 7]

i = j = count = 0

while i < len(child) and j < len(cookie):
    if child[i] <= cookie[j]:
        count += 1
        i += 1
        j += 1
    else:
        j += 1

print(count)