T = int(input())
for t in range(1, T+1):
    n  = int(input())
    data = [int(_) for _ in input().split()]
    res= 0
    for i in range(1, len(data)-1):
        res += data[i]>data[i-1] and data[i]>data[i+1]


    print("Case #{}: {}".format(t, res))