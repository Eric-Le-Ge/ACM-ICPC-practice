mod=1000000000
T = int(input())
for t in range(1, T+1):
    s = input()
    i = 0
    def run():
        global i
        h, w = 0, 0
        while i<len(s):
            c = s[i]
            if c == ')':
                i += 1
                break
            elif c== 'N':
                h = (h -1 )%mod
            elif c=='S':
                h = (h + 1)%mod
            elif c=='W':
                w = (w -1 )%mod
            elif c=='E':
                w = (w +1 )%mod
            elif c != '(':
                mul = int(c)
                i += 2
                th, tw = run()
                h += mul*th
                w += mul*tw
                h %= mod
                w %= mod
                continue
            i += 1
        return h, w
    resh, resw = run()
    print("Case #{}: {} {}".format(t, resw+1, resh+1))