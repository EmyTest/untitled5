import practise
def main():
    x = float(input("enter x-coordinate of point: "))
    y = float(input("enter y-coordinate of point: "))
    z = float(input("enter z-coordinate of point: "))
    h = float(input("enter h-coordinate of point: "))
    p=practise.Point(x,y,z,h)
    print("distance from origin:{0:,.2f}".format(p.distanceFromOrigin()))
main()