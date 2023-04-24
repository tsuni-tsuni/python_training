from geom2d.point import Point

l1 = [Point(3, 1), Point(0, 0), Point(1, 2)]
l2 = sorted(l1, key=lambda p: p.distance(Point(0,0)))
print(l1)
print(l2)

# l = [Point(i, i*i) for i in range(-5, 6)]
# l2 = [Point(el.x, -el.y) for el in l]

# l = []
# for i in range(-5, 6):
#     l.append(Point(i, i*i))

l = list(map(lambda i: Point(i, i*i), range(-5, 6)))
# l2 = list(map(lambda p: Point(p.x, -p.y), l))
l2 = list(filter(lambda p: p.x % 2 == 0, l))

# l2 = []
# for el in l:
#     l2.append(Point(el.x, -el.y))

print(l)
print(l2)