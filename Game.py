from turtle import *
import turtle
from player import *
from bullet import *
from target import *
import random
import time
import math


turtle.tracer(2,0)
SLEEP=0.05
SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)

RUNNING=True
UP_ARROW="Up"
DOWN_ARROW="Down"
SPACEBAR="space"
c=0

bullets=[]
NUMBER_OF_BALLS = 10
MINIMUM_BALL_RADIUS = 30
MAXIMUM_BALL_RADIUS = 30
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

#BALLS = []

    

player=Player(-200,0,5,5,"green",bullets)
for i in range(20):
    x=player.x
    y=player.y
    dx=5
    dy=5
    r=10
    color="black"
    b=Bullet(x,y,dx,dy,r,color)
    bullets.append(b)
turtle.hideturtle()
turtle.pu()

turtle.goto(-SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.write("Score: "+str(Score),font=("David",20,"normal"))
##turtle.goto(0, SCREEN_HEIGHT)
##turtle.write("Level: "+str(level),font=("David",20,"normal"))

##for i in range(NUMBER_OF_BALLS):
##	x = random.randint(int(SCREEN_WIDTH-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
##	y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
##	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
##	while dx == 0:
##		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
##
##	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
##	while dy ==0:
##		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
##	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
##	color = (random.random(), random.random(), random.random())
##	s = "theway2.gif"
##	uk = Ball(x,y,dx,dy,radius,s,color)
##	BALLS.append(uk)

def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)
##def collide(b,uk):
##    if b==uk:
##        return False
##    
##    xa=b.xcor()
##    ya=b.ycor()
##
##    xb=uk.xcor()
##    yb=uk.ycor()
##
##    D = math.sqrt(math.pow((xa-xb),2)+math.pow((ya-yb),2))
##    if D<=b.r+uk.r:
##
##        return True
##    else:
##        return False

def shoot_last():
    global b
    
    if len(bullets) != 0:
        bullet = bullets.pop()
        bullet.goto(bullet.s_point)
##        for i in range(200):
##            for uk in BALLS:
##                #if(collide(bullet, uk)):
##                if bullet.pos() in uk.pos():
##                    bullet.ht()
##                    BALLS.remove(uk)
##                    del uk
##                    break
##            bullet.fd(bullet.dx)
        bullet.shoot()
##        for uk in BALLS:
##            while bullet.xcor() < 200:
##                if bullet.pos() in uk.pos():
##                    BALLS.remove(uk)
##                    del uk
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





def check_bullet_collision():
    for b in bullets:
        for uk in BALLS:
            #print(b.pos())
            #print(uk.pos())
            #if(b.xcor()==200):
                #print("hello")
            if b.pos()==uk.pos():
                b.pop()
##                uk.hideturtle()                
##               uk.pop()
                #print("Hit")
                #uk.goto(20,0)
                

    return True


t=30
##def countdown():
##    global t
##    if t>=0:
##        turtle.clear()
##        turtle.goto(SCREEN_WIDTH,SCREEN_HEIGHT)
##        turtle.write("Time: "+str(t), font=("David",20,"normal"))
##        t-=1
##        turtle.goto(SCREEN_WIDTH,SCREEN_HEIGHT)
##    else:
##        turtle.clear()
##        turtle.write("Time is up, Game over! ")
##
##turtle.ontimer(countdown, 1000)
##while len(bullets)!=0:
##    countdown()

    #turtle.goto(0,0)
    #turtle.write("Game over!",font=("David",20,"normal"),align='center')
    

    

        
    
        
turtle.onkeypress(move_up,UP_ARROW)
turtle.onkeypress(move_down,DOWN_ARROW)

turtle.listen()
while RUNNING:
    
    move_all_balls()
    turtle.onkeypress(shoot_last,SPACEBAR)
    turtle.getscreen().update()
    time.sleep(SLEEP)
    #check_bullet_collision()
        
    if len(bullets)==0:
        RUNNING = False
#turtle.mainloop()
    
    

