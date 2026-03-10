# 10. Find repeated elements in a list using set

lst = [1, 2, 3, 2, 4, 1, 5]

seen = set()
repeated = set()

for i in lst:
    if i in seen:
        repeated.add(i)
    else:
        seen.add(i)

print(repeated)