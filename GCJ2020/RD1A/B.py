T = int(input())

pas = [[1]]
for i in range(500):
    tmp = []
    for j in range(len(pas[-1])-1):
        tmp.append(pas[-1][j]+pas[-1][j+1])
    pas.append([1]+tmp+[1])


for t in range(1, T+1):
    n = int(input())
    if n == 1:
        print("Case #{}:".format(t))
        print("1 1")
        continue
    if n == 2:
        print("Case #{}:".format(t))
        print("1 1")
        print("2 1")
        continue
    res = [(1, 1)]
    done = False
    def finishoff():
        global res, done
        do = n%2 == 1
        rounds = n // 2
        buffer = []
        for _ in range(rounds):
            buffer.append((2, 1))
            buffer.append((1, 1))

        if do:
            buffer.append((2, 1))

        res = [res[0]] + buffer + res[1:]
        print("Case #{}:".format(t))
        su  = 0
        for x, y in res:
            su += pas[x-1][y-1]
            print(str(x)+" "+str(y))
        #print(su)

        done = True

    extends = []
    n -= 1
    for i in range(1, 7):
        n -= 1
        res.append((i+1, i+1))
        if n == 0:
            finishoff()
            break
    if done:
        continue

    n -= 1

    row, col = 9, 8
    extend7 = [(8, 8)]
    while n > pas[row-1][col-1]:
        n -= pas[row-1][col-1]
        extend7.append((row, col))
        row, col = row+1, col + 1


    for i in range(6, 0, -1):
        # row, col = i + 2, i + 1
        # tmp = []
        # tail = []
        # did = False
        # while n > 2 * pas[row-1][col-1] + pas[row][col]:
        #     n -= 2 * pas[row-1][col-1]
        #     tmp.append((row, col))
        #     row, col = row+1, col + 1
        # if n > pas[row-1][col-1]:
        #     n -= pas[row-1][col-1]
        #     tail.append((row, col))
        #     did = True
        # extends.append(tmp + tail + tmp[::-1])
        # if did:
        #     n -= 1
        #     extends[-1] += [(i+1, i+1)]
        #
        extends.append([])

    extends = extends[::-1]

    res = [[_] for _ in res]
    for i in range(6):
        res[i+1].extend(extends[i])
    res[6].extend(extend7)
    nres = []
    for l in res:
        for k in l:
            nres.append(k)
    res = nres
    finishoff()

