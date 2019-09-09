
board = [0]*15
for i in range(5):
    data = [int(_) for _ in input().split()]
    board[((i+1)*i)//2:((i+1)*i)//2+i+1] = data
trans = [(0,1,3),(0,2,5),(1,3,6),(1,4,8),(2,4,7),(2,5,9),(3,1,0),(3,4,5),(3,6,10),(3,7,12),(4,7,11),(4,8,13),
(5,2,0),(5,4,3),(5,8,12),(5,9,14),(6,3,1),(6,7,8),(7,4,2),(7,8,9),(8,7,6),(8,4,1),(9,8,7),(9,5,2),(10,6,3),
(10,11,12),(11,7,4),(11,12,13),(12,7,3),(12,8,5),(12,11,10),(12,13,14),(13,8,4),(13,12,11),(14,9,5),(14,13,12)]

#     0
#    1 2
#   3 4 5
#  6 7 8 9
# 1011121314
def net(board):
	scores = []
	for dest, mid, src in trans:
		if board[dest] == 0 and board[mid] and board[src]:
			m, s = board[mid], board[src]
			score = board[mid] * board[src]
			board[mid], board[src], board[dest] = 0, 0, s
			op = net(board)
			scores.append(score - op)
			board[mid], board[src], board[dest] = m, s, 0
	return max(scores) if scores else 0
print(net(board))
