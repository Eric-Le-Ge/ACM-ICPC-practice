from collections import deque
n = int(raw_input())
d = deque(raw_input())
def get_left():
    res = 0
    while d and d[0] == 'L':
        d.popleft()
        res += 1
    return res
i_left = get_left()
res = [i_left + 1] + list(range(i_left, 0, -1))
cur = i_left + 2
while d:
    d.popleft()
    i_left = get_left()
    res += [cur + i_left] + list(range(cur + i_left -1, cur-1, -1))
    cur += 1 + i_left
for _ in res:
    print (_)