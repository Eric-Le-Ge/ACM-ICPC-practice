n, t = [int(_) for _ in raw_input().split()]
data = []
for i in range(n):
	data.append([int(_) for _ in raw_input().split()])
total = 0.0
for i in range(n-1):
	total += (abs(data[i][0]-data[i+1][0])**2 + abs(data[i][1]-data[i+1][1])**2)**0.5
tt = sum([x[2] for x in data])
ct = 0
gps = [data[0]]
cx, cy = data[0][:2]
j = 0
usex, usey, uset = data[0]

def done():
	gpstotal = 0.0
	for i in range(len(gps)-1):
		gpstotal += (abs(gps[i][0]-gps[i+1][0])**2 + abs(gps[i][1]-gps[i+1][1])**2)**0.5
	print (float(total-gpstotal)/total*100.0)
	exit()

while ct < tt:
	need = min(t, tt-ct)
	while need > 0:
		if j == len(data):
			gps.append([cx, cy])
			done()
		nextx, nexty, nextt = data[j]
		if nextt > ct + need:
			cx, cy, ct = float(need)/(nextt-ct)*(nextx-cx)+cx, float(need)/(nextt-ct)*(nexty-cy)+cy, ct + need
			need = 0
		else:
			need -= nextt-ct
			cx, cy, ct = nextx, nexty, nextt
			j += 1
	gps.append([cx, cy])
done()


