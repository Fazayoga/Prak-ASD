#Dien Azizah
#L200210046

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def distance(self, other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return (x_diff ** 2 + y_diff ** 2) ** 0.5

# create two Point instances
p1 = Point(1, 2)
p2 = Point(3, 4)

# print the points
print("p1 =", p1)
print("p2 =", p2)

# add the points
p3 = p1 + p2
print("p1 + p2 =", p3)

# subtract the points
p4 = p2 - p1
print("p2 - p1 =", p4)

# calculate the distance between the points
dist = p1.distance(p2)
print("Distance between p1 and p2:", dist)

