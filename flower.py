from turtle import*
import colorsys
speed(0)
pensize(2)
bgcolor ("black")
h=0.0
for i in range (250):
      c=colorsys.hsv_to_rgb(h,0.8,1)
      pencolor (c)
      h+=4.105
      circle(6-i, 150)
      lt (180)
      circle(6-1, 150)
      rt (100)
done()
