from point import Point
from line import Line
def main():
    p1=Point(3,8)
    p2=Point(6,8)
    line=Line(p1,p2)
    print(line)
    print(line.length())
    p1.x=5
    print(p1)
main()
