# import turtle module
import turtle

# Screen setup
wind = turtle.Screen()
wind.title("Ping Pong By MhmdEssamEldin")
wind.bgcolor("Black")
wind.setup(width=800, height=600)     # Set the wedth and height of the window
wind.tracer(0)   # Screen cannot make update automatic

#stick 1
stick1 = turtle.Turtle()  # intializes turtle object(shape)
stick1.speed(0)        #set the speed of the animation
stick1.shape("square")  #set the shape of the object
stick1.color("blue")    #set the color of the shape
stick1.shapesize(stretch_wid=5, stretch_len=1)  #stretches the shape to meet the size
stick1.penup()   #stops object from drawing lines
stick1.goto(-350, 0)  #set the position

#stick 2
stick2 = turtle.Turtle()
stick2.speed(0)
stick2.shape("square")
stick2.color("red")
stick2.shapesize(stretch_wid=5, stretch_len=1)
stick2.penup()
stick2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.0
ball.dy = 1.0

#score
Blue = 0
Red = 0
score = turtle.Turtle()
score.speed(0)
score.color("yellow")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Blue: 0 | Red: 0", align="center", font=["gaierror", 24, "normal"])

#function
def stick1_up():
    y = stick1.ycor() #get the y cordinate of the stick1
    y += 20    #set the y to increase by 20
    stick1.sety(y)

def stick1_down():
    y = stick1.ycor()
    y -= 20   #set the y to decrease by 20
    stick1.sety(y)

def stick2_up():
    y = stick2.ycor()
    y += 20
    stick2.sety(y)

def stick2_down():
    y = stick2.ycor()
    y -= 20
    stick2.sety(y)

#keyboard bindings
wind.listen()  #tell the window to expect keyboard input
wind.onkeypress(stick1_up, "w") #when press 'w' the function stick1_up move up
wind.onkeypress(stick1_down, "s") #when press 's' the function stick1_down move down
wind.onkeypress(stick2_up, "Up")  #when press 'Up' the function stick2_up move up
wind.onkeypress(stick2_down, "Down")  #when press 'Down' the function stick2_down move down

#main game loop
while True:
    wind.update()   #update the screen everytime the game start

    #move the ball
    ball.setx(ball.xcor() + ball.dx) #ball start at 0 and everytime loop run ball increase 2
    ball.sety(ball.ycor() + ball.dy)

    #border check: top border +300px, bottom border -300px, ball is 20px 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
       

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        Blue += 1
        score.clear()
        score.write(f"Blue: {Blue}   |   Red: {Red}", align="center", font=["gaierror", 24, "normal"])

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        Red += 1
        score.clear()
        score.write(f"Blue: {Blue}   |   Red: {Red}", align="center", font=["gaierror", 24, "normal"])

    #stick and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < stick2.ycor() +40 and ball.ycor() > stick2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < stick1.ycor() +40 and ball.ycor() > stick1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1