x=input("x coordinate on the plane: ")
x=int(x)
y=input("second coordinate on the plane: ")
y=int(y)
if x>0 and y>0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
if x<0 and y>0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
if x<0 and y<0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
if x>0 and y<0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
if x==0 and y>0:
    print(f"Point P({x},{y}) lies between the first and the second quadrant of the coordinate system")
if x==0 and y<0:
    print(f"Point P({x},{y}) lies between the third and the fourth quadrant of the coordinate system")
if x<0 and y==0:
    print(f"Point P({x},{y}) lies between the second and the third quadrant of the coordinate system")
if x>0 and y==0:
    print(f"Point P({x},{y}) lies between the first and the fourth quadrant of the coordinate system")
if x==0 and y==0:
    print(f"Point P({x},{y}) lies at the origin of the coordinate system")