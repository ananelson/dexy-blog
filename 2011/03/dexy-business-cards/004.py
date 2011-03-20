from turtle import *

s = Screen()
s.setworldcoordinates(-22,-22,22,22)
pencolor("#697C82")

### @export "turtle"
for i in range(24):
    circle(10)
    rt(15)
### @end               

print s.getcanvas().postscript()
