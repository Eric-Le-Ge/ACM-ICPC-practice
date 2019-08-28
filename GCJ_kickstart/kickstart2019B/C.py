import math
T = int(raw_input())
#Merging function
merge = lambda x, y: (x[0]+y[0], max(x[0]+y[1], x[1]))
#Seg Tree Functions
def _build_util(arr, seg, low, high, pos):
    if low == high:
        seg[pos] = arr[low]
        return arr[low]
    mid = (low+high)//2
    seg[pos] = merge(_build_util(arr, seg, low, mid, pos*2+1), _build_util(arr, seg, mid+1, high, pos*2+2))
    return seg[pos]

def build(arr):
    h = math.ceil(math.log(len(arr))/math.log(2))
    seg = [0]*int(2**(h+1))
    seg[-1] = len(arr) #stores n at the back of seg
    _build_util(arr, seg, 0, len(arr)-1, 0)
    return seg

def _query_util(seg, ss, se, qs, qe, pos):
    if qs <= ss and qe >= se:
        return seg[pos]
    mid = (ss+se)//2
    if mid+1 > qe:
        return _query_util(seg, ss, mid, qs, qe, 2*pos+1)
    if mid < qs:
        return _query_util(seg, mid+1, se, qs, qe, 2*pos+2)
    return merge(_query_util(seg, ss, mid, qs, qe, 2*pos+1), _query_util(seg, mid+1, se, qs, qe, 2*pos+2))

def query(seg, qs, qe):
    return _query_util(seg, 0, seg[-1]-1, qs, qe, 0)

def _put_util(seg, index, value, low, high, pos):
    if index < low or index > high:
        return
    if low == high:
        if low == index:
            seg[pos] = value
    else:
        mid = (low+high)//2
        _put_util(seg, index, value, low, mid, 2*pos+1)
        _put_util(seg, index, value, mid+1, high, 2*pos+2)
        seg[pos] = merge(seg[2*pos+1], seg[2*pos+2])

def put(seg, index, value):
    _put_util(seg, index, value, 0, seg[-1]-1, 0)






def solve():
    m = [[] for _ in range(100001)]
    events = [(0,0)]*N
    for i in range(N):
        m[trinkets[i]] += [i]
        if len(m[trinkets[i]])<=S:
            events[i] = (1,1)
        elif len(m[trinkets[i]])==S+1:
            events[i] = (-S, -S)
    seg = build(events)
    res = query(seg, 0, N-1)[1]
    for j in range(N):
        put(seg, m[trinkets[j]][0], (0,0))
        m[trinkets[j]] = m[trinkets[j]][1:]
        indexs = m[trinkets[j]]
        if len(indexs)>=S:
            put(seg, indexs[S-1], (1,1))
        if len(indexs)>=S+1:
            put(seg, indexs[S], (-S,-S))
        res = max(res,query(seg, 0, N-1)[1])
    return res


for t in range(T):
    N, S = [int(_) for _ in raw_input().split()]
    trinkets = [int(_) for _ in raw_input().split()]
    res = solve()
    print "Case #{}: {}".format(t+1, res)

