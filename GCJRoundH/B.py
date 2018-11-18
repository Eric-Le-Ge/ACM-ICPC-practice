# t = int(input())
# for i in range(1, t + 1):
#   n, m = [int(s) for s in input().split(" ")]
#   print("Case #{}: {} {}".format(i, n + m, n * m))

t = int(input())
for i in range(1, t + 1):
    res = 0
    n = int(input())
    s = input()
    numbers = []
    for j in s:
        numbers.append(int(j))
    tracker = (len(numbers)+1)//2
    left = 0
    slide = sum(numbers[0:((len(numbers)+1)//2)])
    maximum = slide
    while tracker < len(numbers):
        slide+=numbers[tracker]
        tracker += 1
        slide -= numbers[left]
        left += 1
        maximum = max(maximum, slide)


    print("Case #{}: {}".format(i, maximum))
