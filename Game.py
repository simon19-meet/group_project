from turtle import *
import turtle
from player import *
from bullet import *
from target import *

turtle.tracer(1, 0)

SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

Running=True
UP_ARROW="Up"
DOWN_ARROW="Down"
SPACEBAR="space"
c=0
bullets=[]

    

player=Player(-200,0,5,5,"green",bullets)
for i in range(10):
    x=player.x
    y=player.y
    dx=5
    dy=5
    color="black"
    b=Bullet(x,y,dx,dy,color)
    bullets.append(b)
turtle.hideturtle()
turtle.pu()

turtle.goto(-SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.write("Score: ",font=("David",20,"normal"))
turtle.goto(0, SCREEN_HEIGHT)
turtle.write("Time: ",font=("David",20,"normal"))

def shoot_last():
    if len(bullets) != 0:
        b = bullets.pop()
        b.shoot()
    else:
        turtle.write("Game over!")
    
def move_up():
    global player
    global bullet
    global bullets
    global c
    player.up()
    for bullet in bullets:
        bullet.up()
    for b in bullets:
        b.hideturtle()
        b.goto(player.pos())
    
def move_down():
    global player
    global bullet
    global bullets
    global c
    for bullet in bullets:
        bullet.down()
    player.down()
    for b in bullets:
        b.hideturtle()
        b.goto(player.pos())
    

    
    
turtle.onkeypress(move_up,UP_ARROW)
turtle.onkeypress(move_down,DOWN_ARROW)
turtle.onkeypress(shoot_last,SPACEBAR)
turtle.listen()
turtle.listen()
