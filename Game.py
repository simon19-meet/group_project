from turtle import *
import turtle
from player import *
from bullet import *
from target import Ball
import random
import time

turtle.tracer(1,0)
SLEEP=0.05
SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)

RUNNING=True
UP_ARROW="Up"
DOWN_ARROW="Down"
SPACEBAR="space"
c=0
score=0
level=1
bullets=[]
NUMBER_OF_BALLS = 10
MINIMUM_BALL_RADIUS = 30
MAXIMUM_BALL_RADIUS = 30
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

    

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
turtle.write("Score: "+str(score),font=("David",20,"normal"))
turtle.goto(0, SCREEN_HEIGHT)
turtle.write("Level: "+str(level),font=("David",20,"normal"))

for i in range(NUMBER_OF_BALLS):
	x = random.randint(int(SCREEN_WIDTH-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	while dx == 0:
		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)

	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	while dy ==0:
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	s = "theway2.gif"
	uk = Ball(x,y,dx,dy,radius,s,color)
	BALLS.append(uk)

def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def shoot_last():
    
    if len(bullets) != 0:
        b = bullets.pop()
        b.shoot()
    else:
        turtle.goto(0,0)
        turtle.write("Game over!",font=("David",20,"normal"),align='center')
    
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

turtle.listen()
while RUNNING:
    move_all_balls()
    turtle.onkeypress(shoot_last,SPACEBAR)
    turtle.getscreen().update()
    time.sleep(SLEEP)
    if len(bullets)==0:
        RUNNING = False
turtle.mainloop()
    
    

