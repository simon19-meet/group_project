def collide(ball_a,ball_b):
    if ball_a==ball_b:
        return False
    xa=ball_a.xcor()
    ya=ball_a.ycor()

    xb=ball_b.xcor()
    yb=ball_b.ycor()

    D = math.sqrt(math.pow((xa-xb),2)+math.pow((ya-yb),2))

    if D+10<=ball_a.r+ball_b.r:       
        return True
    else:
        return False



def check_bullet_collision():
    for bullet in bullets:
        for uk in BALLS:
            if collide(bullet,uk)==True:
                  uk.hideturtle()
                  uk.pop()                 

    return True
