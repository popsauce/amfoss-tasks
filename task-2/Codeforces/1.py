n = int(input())
r = 1
for r in range(1, n+1):
    for j in range(1, n-r+1):
        print(" ", end='')
    k = 0
    while k != r:
        print("#", end='')
        k = k + 1
    print("")
