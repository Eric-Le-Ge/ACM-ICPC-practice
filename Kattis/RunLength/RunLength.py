d, s = input().split()
if d == 'D':
    buf = ''
    i = 0
    while i < len(s):
        buf += s[i]*int(s[i+1])
        i += 2
    print (buf)
else:
    buf = ''
    i = 0
    while i < len(s):
        c = s[i]
        cnt = 0
        while i < len(s) and s[i] == c:
            cnt += 1
            i += 1
        buf += c+str(cnt)
    print (buf)
