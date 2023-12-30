from firstclass import Line
A=input("coor1x: ")
B=input("coord2x: ")

A=tuple((float(x) for x in A.split()))
B=tuple((float(x) for x in B.split()))

li=Line(A,B)
print(li.distance())