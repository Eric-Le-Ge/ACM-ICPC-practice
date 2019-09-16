'''Usage:
line {a,b,c}: ax+by+c = 0
point {x,y}: (x,y)
'''
def pd2line(a, b, c, x, y):
    return (a*x+b*y+c)/(a*a+b*b)**.5
