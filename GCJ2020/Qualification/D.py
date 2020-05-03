T, B = [int(_) for _ in input().split()]
for t in range(1, T+1):
    left = []
    right = []
    m = 0

    def grow():
        global m
        for i in range(4):
            print(1 + len(left), flush=True)
            left.append(int(input()))
            print(B - len(right), flush=True)
            right.append(int(input()))
            m += 1
            if len(left) + len(right) == B:
                return True
        return False

    def recover():
        global left, right
        if not left:
            print(1, flush=True)
            input()
            print(1, flush=True)
            input()
            return
        # look for a diff and a same
        diff, same = False, False
        diff_ind, same_ind = 0, 0
        for i in range(m):
            if left[i] != right[i]:
                diff = True
                diff_ind = i
            else:
                same = True
                same_ind = i
        # if no diff, check for a flip
        if not diff:
            print(1, flush=True)
            rep = int(input())
            # flip
            if rep != left[0]:
                left = [1-num for num in left]
                right = [1-num for num in right]
            print(1, flush=True)
            input()
            return
        print(1 + diff_ind, flush=True)
        rep = int(input())
        # nothing or both
        if rep == left[diff_ind]:
            if not same:
                print(1, flush=True)
                input()
                return
            print(1 + same_ind, flush=True)
            rep = int(input())
            # both
            if rep != left[same_ind]:
                left, right = [1-num for num in right], [1-num for num in left]
            return
        # flip or rev
        if not same:
            left = [1-num for num in left]
            right = [1-num for num in right]
            print(1, flush=True)
            input()
            return
        print(1 + same_ind, flush=True)
        rep = int(input())
        # flip
        if rep != left[same_ind]:
            left = [1-num for num in left]
            right = [1-num for num in right]
        # rev
        else:
            left, right = right, left

    while True:
        recover()

        if grow():
            res = ''.join([str(_) for _ in left])
            res += ''.join([str(_) for _ in right[::-1]])
            print(res, flush=True)
            yn = input()
            if yn == 'N':
                exit()
            else:
                break


