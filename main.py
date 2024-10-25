import turtle as t
import time
import random

#-----game configuration----
torterracolor = "Green"
torterrasize = 3
torterrashape = "turtle"
score = 0
high_score = 0
time_left = 60

#-----initialize turtle-----
torterra = t.Turtle()
torterra.shape(torterrashape)
torterra.color(torterracolor)
torterra.shapesize(torterrasize)
torterra.speed(0)

scoreboard = t.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(-300, 300)
scoreboard.pendown()

timer = t.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(300, 300)
timer.pendown()

#-----game functions--------
def update_score():
    global score, high_score
    scoreboard.clear()
    score += 10
    if score > high_score:
        high_score = score
    scoreboard.write(f"Score: {score}  High Score: {high_score}", font=("Calibri", 15, "normal"))

def game_over():
    timer.clear()
    timer.write("Game Over", font=("Calibri", 15, "normal"))
    timer.goto(0, 0)
    timer.write(f"High Score: {high_score}", align="center", font=("Calibri", 15, "normal"))
    torterra.hideturtle()
    t.onkey(play_again, "space")

def torterraClicked(x, y):
    global time_left
    if time_left > 0:
        torterra.penup()
        torterra.goto(random.randrange(-400, 400), random.randrange(-300, 300))
        
        # Leave a blue circle stamp
        torterra.color("blue")
        torterra.stamp()
        
        # Reset the color back to green
        torterra.color(torterracolor)

        update_score()


def countdown():
    global time_left
    timer.clear()
    if time_left <= 0:
        game_over()
    else:
        timer.write("Timer: " + str(time_left), font=("Calibri", 15, "normal"))
        time_left -= 1
        timer.getscreen().ontimer(countdown, 1000)

def play_again():
    global score, time_left
    score = 0
    time_left = 60
    torterra.showturtle()
    scoreboard.clear()
    countdown()
    torterra.goto(random.randrange(-400, 400), random.randrange(-300, 300))
    update_score()

#-----events----------------
t.listen()
torterra.onclick(torterraClicked)
wn = t.Screen()
wn.bgcolor("light gray")
countdown()
wn.mainloop()
