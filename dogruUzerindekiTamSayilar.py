p1 = (658000, 4207400)
p2 = (659000, 4208280)

x1, y1 = p1[0], p1[1]
x2, y2 = p2[0], p2[1]


# y - b = m*(x-a)
# y = m*(x-a) + b
# x = ((y-b)/m)+a
a, b = p1
if p1[1] == p2[1]:
    y = p1[1]
    for x in range(p1[0], p2[0]+1):
        print(x, y)
elif p1[0] == p2[0]:
    x = p1[0]
    for y in range(p1[1],p2[1]+1):
        print(x, y)
else:
    m = (y2-y1)/(x2-x1)
    for y in range(p1[1],p2[1]+1):
        x = ((y-b)/m)+a
        if x - int(x) == 0:
            print(y, int(x))
