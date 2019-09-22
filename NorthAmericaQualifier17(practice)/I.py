t = int(raw_input())
for _ in range(t):
	data = [int(_) for _ in raw_input().split()]
	done = False
	for i in range(1, len(data)-2):
		if data[i+1] < data[i] and data[i+2] < data[i]:
			print (i)
			done = True
			break;
		elif data[i+1] < data[i] and data[i+2] > data[i]:
			print (i+1)
			done = True
			break;
	if not done:
		print (len(data) - 2)
