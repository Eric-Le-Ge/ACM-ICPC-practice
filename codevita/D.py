# from collections import deque
from collections import defaultdict

N = int(input())
trades = []
for i in range(N):
	pcs = input().split()
	trades.append((pcs[1], pcs[2], int(pcs[3]), int(pcs[4])))

prices = {}
sells = defaultdict(list)
buys = defaultdict(list)
# [price, quantity]
for action, stock, price, quantity in trades:
	if quantity == 0:
		continue
	if action == 'Sell':
		ind = 0
		while quantity > 0 and ind < len(buys[stock]):
			if buys[stock][ind][0] >= price:
				deal = min(quantity, buys[stock][ind][1])
				quantity -= deal
				buys[stock][ind][1] -= deal
				prices[stock] = min(price, buys[stock][ind][0])
				if buys[stock][ind][1] == 0:
					buys[stock].pop(ind)
					ind -= 1
			ind += 1
		if quantity > 0:
			sells[stock].append([price, quantity])
	elif action == 'Buy':
		ind = 0
		while quantity > 0 and ind < len(sells[stock]):
			if sells[stock][ind][0] <= price:
				deal = min(quantity, sells[stock][ind][1])
				quantity -= deal
				sells[stock][ind][1] -= deal
				prices[stock] = min(price, sells[stock][ind][0])
				if sells[stock][ind][1] == 0:
					sells[stock].pop(ind)
					ind -= 1
			ind += 1
		if quantity > 0:
			buys[stock].append([price, quantity])
	else:
		pass
#print(buys, sells, prices)
for ks in sorted(prices.keys()):
	print("{}:{}".format(ks, prices[ks]), end='')
	# print(' ', end='')
if not prices.keys():
	print("Stocks not traded", end='')

