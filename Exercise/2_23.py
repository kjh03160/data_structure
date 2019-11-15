a = [-10,-7,5,-7,10,5,-2,17,-25,1]
max = 0
for i in range(len(a)):
    sum = 0
    for j in range(i+1, len(a)):
        sum += a[j-1]
        if sum > max:
            max = sum
print(max)