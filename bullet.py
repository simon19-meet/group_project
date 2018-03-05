from turtle import *
import turtle



UP_ARROW="Up"
DOWN_ARROW="Down"
SPACEBAR="space"

class Bullet(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.pu()
        self.x=x
        self.y=y
        self.goto(x,y)
        self.dx=dx
        self.dy=dy
        self.r=r
        self.shape("square")
        self.color(color)
        self.shape("circle")
        self.shapesize(r/10)
        self.s_point = [-200,0]

    def up(self):
        
        current_x = self.xcor()
        #new_x = current_x + self.dx
        current_y = self.ycor()
        self.setheading(90)
        self.fd(self.dy)
        self.s_point[1]= self.s_point[1]+self.dy
        #print(self.s_point[1])
        
        
    def down(self):
        current_x = self.xcor()
        #new_x = current_x + self.dx
        current_y = self.ycor()
        self.setheading(270)
        self.fd(self.dy)
        self.s_point[1]= self.s_point[1]-self.dy
        
    def shoot(self):
        self.goto(self.s_point)
        current_y=self.ycor()
        current_x=self.xcor()
        self.showturtle()
        self.setheading(0)
        for i in range(200):
            
            self.fd(self.dx)
        self.ht()
            
    

##bullet=Bullet(-200,0,5,5,"black")
##turtle.onkeypress(bullet.up,UP_ARROW)
##turtle.onkeypress(bullet.down,DOWN_ARROW)
##turtle.onkey(bullet.shoot,SPACEBAR)
##turtle.listen()


