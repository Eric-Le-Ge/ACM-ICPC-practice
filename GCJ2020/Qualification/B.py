T = int(input())
for t in range(1, T+1):
    s = input()
    p = 0
    i = 0
    res = ""
    while i < len(s):
        if int(s[i]) > p:
            p += 1
            res += '('
        elif int(s[i]) < p:
            p -= 1
            res += ')'
        else:
            res += s[i]
            i += 1
    res += ')'*p
    print("Case #{}: {}".format(t, res))