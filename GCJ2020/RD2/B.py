from collections import defaultdict
import heapq
T = int(input())

for t in range(1, T+1):
    C, D = [int(_) for _ in input().split()]
    data = [int(_) for _ in input().split()]
    time_assignment = {1:0}

    mylinks = defaultdict(list)
    links = []
    res = []
    for i in range(D):
        l1, l2 = [int(_) for _ in input().split()]
        mylinks[l1].append((l2, i))
        mylinks[l1].append((l1, i))
        links.append((l1, l2))

    neg, pos = [], []
    for i, num in enumerate(data):
        if num < 0:
            neg.append((-num, i+2))
        else:
            pos.append((num, i+2))
    heapq.heapify(pos)
    heapq.heapify(neg)

    last_time = 0
    processed_count = 1

    def process(arr, time):
        global processed_count
        processed_count += len(arr)
        for ind in arr:
            time_assignment[ind] = time

    while neg:
        rank, ind = heapq.heappop(neg)
        inds = [ind]
        while neg and neg[0][0] == rank:
            inds.append(heapq.heappop(neg)[1])
        # case where there are no prior positives
        if processed_count == rank:
            while pos and pos[0][0] == last_time + 1:
                inds.append(heapq.heappop(pos)[1])
            time_ = last_time + 1
            process(inds, time_)
            last_time = time_
        # need to insert a few positives
        else:
            num = rank - processed_count
            for i in range(num):
                insert_time, ind = heapq.heappop(pos)
                process([ind], insert_time)
                last_time = insert_time
            while pos and pos[0][0] == last_time + 1:
                inds.append(heapq.heappop(pos)[1])
            time_ = last_time + 1
            process(inds, time_)
            last_time = time_
    while pos:
        time_, ind = heapq.heappop(pos)
        process([ind], time_)

    for l1, l2 in links:
        res.append(str(abs(time_assignment[l1]-time_assignment[l2])))

    for i in range(len(res)):
        if res[i] == '0':
            res[i] = '1000000'
    print("Case #{}: {}".format(t, " ".join(res)))
