# n, m, r = [int(_) for _ in raw_input().split()]
# pieces = [[]]
# cuts = []
# for i in range(n):
# 	pieces[0].append([int(_) for _ in raw_input().split()])
# for i in range(m):
# 	cuts.append([int(_) for _ in raw_input().split()])
# def cut(a, b, c, pc):
# 	tp, dn = [], []
# 	for p in pc:
# 		x, y = p
# 		if a*x+b*y+c>0:
# 			tp.append(p)
# 		else:
# 			dn.append(p)
# 	if not tp or not dn:
# 		print ("no")
# 		exit()
# 	return tp, dn
# for a, b, c in cuts:
# 	newpieces = []
# 	for piece in pieces:
# 		for ret in cut(a, b, c, piece):
# 			newpieces.append(ret)
# 	pieces = newpieces
# print ("yes")
