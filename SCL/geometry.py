''' Make Line from Two Points
line {a,b,c}: ax+by+c = 0
point {x,y}: (x,y)
'''
def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

''' Point Distance to Line
line {a,b,c}: ax+by+c = 0
point {x,y}: (x,y)
'''
def pd2line(a, b, c, x, y):
    return (a*x+b*y+c)/(a*a+b*b)**.5

'''Area of a Polygon
point {x,y}: (x,y)
corners: [point]
'''
def polygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

'''Intersection point of two lines
line {a,b,c}: ax+by+c = 0
Example:
>>> L1 = line([0,1], [2,3])
>>> L2 = line([2,3], [0,4])
>>> R = intersection(L1, L2)
>>> if R:
>>>     print "Intersection detected:", R
>>> else:
>>>     print "No single intersection point detected"
'''
def intersection(L1, L2):
    D  = float(L1[0] * L2[1] - L1[1] * L2[0])
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False #Parallel or Colinear

'''Given three colinear points p, q, r, checks if point q lies on line segment "pr"
point {x,y}: (x,y)
'''
def on_segment(p, q, r):
    
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False

'''Find orientation of ordered triplet (p, q, r).
The function returns following values
0 --> p, q and r are colinear
1 --> Clockwise
2 --> Counterclockwise
'''
def orientation(p, q, r):
    val = ((q[1] - p[1]) * (r[0] - q[0]) - 
            (q[0] - p[0]) * (r[1] - q[1]))
    if val == 0:
        return 0  # colinear
    elif val > 0:
        return 1   # clockwise
    else:
        return 2  # counter-clockwise

'''Main function to check whether the closed line segments p1 - q1 and p2 - q2 intersect'''
def segment_intersect(p1, q1, p2, q2):
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

