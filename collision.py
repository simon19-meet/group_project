from turtle import Turtle
import math

class Bullets(Turtle):
    def __init__(self, x, y, dx, dy, r):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
Bullet = Bullets(0, 0, 10, 10, 10)

BULLETS = []

BULLETS.append(Bullet)

def collision(bullet, target):
    if bullet.pos() == target.pos():
        return False
    d = math.sqrt(math.pow((target.xcor()-bullet.xcor()),2) + math.pow((target.ycor()-bullet.ycor()),2))
    if d <= bullet.r + target.r:
        return True
    
