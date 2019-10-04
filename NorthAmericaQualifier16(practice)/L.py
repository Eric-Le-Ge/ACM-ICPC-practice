T = int(raw_input())
eps = 10e-5

import math

def distance(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

def on_segment(p, q, r):
    '''Given three colinear points p, q, r, the function checks if 
    point q lies on line segment "pr"
    '''
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False

def orientation(p, q, r):
    '''Find orientation of ordered triplet (p, q, r).
    The function returns following values
    0 --> p, q and r are colinear
    1 --> Clockwise
    2 --> Counterclockwise
    '''

    val = ((q[1] - p[1]) * (r[0] - q[0]) - 
            (q[0] - p[0]) * (r[1] - q[1]))
    if val == 0:
        return 0  # colinear
    elif val > 0:
        return 1   # clockwise
    else:
        return 2  # counter-clockwise

def do_intersect(p1, q1, p2, q2):
    '''Main function to check whether the closed line segments p1 - q1 and p2 
       - q2 intersect'''
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if (o1 != o2 and o3 != o4):
        return True

    # Special Cases
    # p1, q1 and p2 are colinear and p2 lies on segment p1q1
    if (o1 == 0 and on_segment(p1, p2, q1)):
        return True

    # p1, q1 and p2 are colinear and q2 lies on segment p1q1
    if (o2 == 0 and on_segment(p1, q2, q1)):
        return True

    # p2, q2 and p1 are colinear and p1 lies on segment p2q2
    if (o3 == 0 and on_segment(p2, p1, q2)):
        return True

    # p2, q2 and q1 are colinear and q1 lies on segment p2q2
    if (o4 == 0 and on_segment(p2, q1, q2)):
        return True

    return False # Doesn't fall in any of the above cases

def inline(p0, p1, cp):
	dx0, dy0 = cp[0]-p0[0], cp[1]-p0[1]
	dx1, dy1 = cp[0]-p1[0], cp[1]-p1[1]
	return dx1*dy0 == dx0*dy1

def PolygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

def intersect(i):
	for j in range(len(config)-2):
		if do_intersect(points[config[j]], points[config[j+1]], points[config[-1]], points[i]):
			return True
	if len(config) >= 2 and inline(points[config[-2]], points[i], points[config[-1]]):
		return True
	if len(config) == 6:
		if inline(points[config[1]], points[i], points[config[0]]):
			return True
		for j in range(1, 5):
			if do_intersect(points[config[j]], points[config[j+1]], points[config[0]], points[i]):
				return True
	return False

def backtrak():

	if len(config) == 7:
		if acc - eps < (PolygonArea(map(lambda x: points[x], config))/4.0)**3 < acc + eps:
			return True
		return False
	for i in range(1, 7):
		if i not in config and not intersect(i):
			config.append(i)
			if backtrak():
				return True
			config.pop()
	return False

for t in range(T):
	points = []
	for i in range(7):
		points.append([float(_) for _ in raw_input().split()])
	acc = float(raw_input())
	config = [0]
	backtrak()
	print (' '.join(map(lambda x: str(x+1), config)))

