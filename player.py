from turtle import *
import turtle
from bullet import Bullet



UP_ARROW="Up"
DOWN_ARROW="Down"
list_of_bullets=[]

turtle.register_shape("12970175675.gif")

class Player(Turtle):
    def __init__(self,x,y,dx,dy,color,list_of_bullets):
        Turtle.__init__(self)
        self.pu()
        self.x=x
        self.y=y
        self.goto(x,y)
        self.dx=dx
        self.dy=dy
        self.shape("square")
        self.color(color)
        self.shape("12970175675.gif")

    def up(self):
        for bullet in list_of_bullets:
            bullet.up()
        current_x = self.xcor()
        #new_x = current_x + self.dx
        current_y = self.ycor()
        self.setheading(90)
        self.fd(self.dy)
        
        
    def down(self):
        for bullet in list_of_bullets:
            bullet.down()
        current_x = self.xcor()
        #new_x = current_x + self.dx
        current_y = self.ycor()
        self.setheading(270)
        self.fd(self.dy)


##player=Player(-200,0,0,5,"green")
##turtle.onkeypress(player.up,UP_ARROW)
##turtle.onkeypress(player.down,DOWN_ARROW)
##turtle.listen()



        
