import turtle
from player import Player
from bullet import Bullet

SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

Running=True
UP_ARROW="Up"
DOWN_ARROW="Down"
SPACEBAR="space"




player=Player(-200,0,5,5,"green")
bullet=Bullet(-200,0,5,5,"black")
turtle.hideturtle()
turtle.pu()

turtle.goto(-SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.write("Score: ",font=("David",20,"normal"))
turtle.goto(0, SCREEN_HEIGHT)
turtle.write("Time: ",font=("David",20,"normal"))

def move_up():
    global player
    global bullet
    player.up()
    bullet.hideturtle()
    bullet.goto(player.pos())
  #  player.pos()=bullet.pos()
def move_down():
    global player
    global bullet
    player.down()
    bullet.hideturtle()
    bullet.goto(player.pos())
    
turtle.onkeypress(move_up,UP_ARROW)
turtle.onkeypress(move_down,DOWN_ARROW)
turtle.onkeypress(bullet.shoot,SPACEBAR)
turtle.listen()
turtle.listen()
