### @export "imports"
from turtle import *

### @export "setup"
s = Screen()
s.setworldcoordinates(-22,-22,22,22)

### @export "pen-color"
pencolor("#697C82")

### @export "draw"
for i in range(24):
    circle(10)
    rt(15)

### @export "postscript"
print s.getcanvas().postscript()
