T = int(input())
for t in range(1, T+1):
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append([int(_) for _ in input().split()])
    trace = 0
    for i in range(n):
        trace += matrix[i][i]
    r = 0
    c = 0
    for i in range(n):
        r += (len(set(matrix[i])) != n)
    for j in range(n):
        s = set()
        for k in range(n):
            num = matrix[k][j]
            if num in s:
                c += 1
                break
            s.add(num)
    print("Case #{}: {} {} {}".format(t, trace, r, c))