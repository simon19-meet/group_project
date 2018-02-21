from turtle import *
import turtle





UP_ARROW="Up"
DOWN_ARROW="Down"


turtle.register_shape("12970175675.gif")

class Player(Turtle):
    def __init__(self,x,y,dx,dy,color):
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
        
        current_x = self.xcor()
        #new_x = current_x + self.dx
        current_y = self.ycor()
        self.setheading(90)
        self.fd(self.dy)
        
        
    def down(self):
        current_x = self.xcor()
        #new_x = current_x + self.dx
        current_y = self.ycor()
        self.setheading(270)
        self.fd(self.dy)


player=Player(-200,0,0,5,"green")
turtle.onkeypress(player.up,UP_ARROW)
turtle.onkeypress(player.down,DOWN_ARROW)
turtle.listen()



        
