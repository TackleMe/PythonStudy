from turtle import *
shape("turtle")
col = ["orange","limegreen","gold","plum","tomato","red","blue","yellow","silver","black"]
for i in range(10):
    color(col[i])
    circle(100)
    left(72)
    right(66)
    circle(40)
    left(72)
done()