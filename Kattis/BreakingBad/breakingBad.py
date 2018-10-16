import sys
n = int(sys.stdin.readline())
assignments = [0]*n
graph = {}
items = []
anti_item = {}
a, b = [], []

for i in range(n):
    items.append(sys.stdin.readline()[:-1])
    anti_item[items[i]] = i
m = int(sys.stdin.readline())
for i in range(m):
    line = sys.stdin.readline()[:-1].split(' ')
    itema, itemb =  line[0], line[1]
    if itema in graph:
        graph[itema].append(itemb)
    else:
        graph[itema] = [itemb]
    if itemb in graph:
        graph[itemb].append(itema)
    else:
        graph[itemb] = [itema]

def solve():
    for i in range(n):
        t = []
        if assignments[i]:
            continue
        assignments[i] = 1
        a.append(items[i])
        if items[i] not in graph:
            continue
        for item in graph[items[i]]:
            index = anti_item[item]
            if assignments[index] == 1:
                print('impossible')
                return
            elif assignments[index] == 0:
                assignments[index] = -1
                b.append(items[index])
                for item2 in graph[item]:
                    index2 = anti_item[item2]
                    if assignments[index2] == -1:
                        print('impossible')
                        return
                    elif assignments[index2] == 0:
                        assignments[index2] = 1
                        a.append(item2)
                        t.append(index2)

        while t:
            k = t.pop()
            for item in graph[items[k]]:
                index = anti_item[item]
                if assignments[index] == 1:
                    print('impossible')
                    return
                elif assignments[index] == 0:
                    b.append(items[index])
                    assignments[index] = -1
                    for item2 in graph[item]:
                        index2 = anti_item[item2]
                        if assignments[index2] == -1:
                            print('impossible')
                            return
                        elif assignments[index2] == 0:
                            assignments[index2] = 1
                            a.append(item2)
                            t.append(index2)
    for item in a:
        print(item, end=" ")
    print()
    for item in b:
        print(item, end=" ")
    print()
solve()
