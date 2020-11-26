import turtle # using the turtle module to add graphics and open windows ect.. | good for simple games


wn = turtle.Screen() #created the window screen
wn.title('PongGame') #created the title
wn.bgcolor('blue') #set the background color of the screen to blue
wn.setup(width=800, height=600) #set the with and height of the window, starts at the center so its +800 right then -800 left for width
wn.tracer(0)  #stops the window from updating and allow us to manually do this. increases game speed

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation , sets speed to the maximum
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # to modify the shape size , will be 20px by 20px by default
paddle_a.penup() # so we dont draw lines
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation , sets speed to the maximum
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # to modify the shape size , will be 20px by 20px by default
paddle_b.penup() # so we dont draw lines
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation , sets speed to the maximum
ball.shape("circle")
ball.color("yellow")
ball.penup() # so we dont draw lines
ball.goto(0, 0) # balls starting position
# seperate ball movement into two parts x and y
ball.dx = .25 # delta or change
ball.dy = -.25 # everytime the ball moves, it will move by 2px

# Create a pen to write player scores
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function , goals move paddles and the ball
def paddle_a_up(): # define the function
    y = paddle_a.ycor() # returns the y coordinates of the paddle
    y += 20 # moves the ball up, increase the y by 20px
    paddle_a.sety(y) # set the old y to the new y

def paddle_a_down(): #define the function
    y = paddle_a.ycor() # returns the y coordinates of the paddle
    y -= 20 # moves the ball up, increase the y by 20px
    paddle_a.sety(y) # set the old y to the new y

def paddle_b_up(): #define the function
    y = paddle_b.ycor() # returns the y coordinates of the paddle
    y += 20 # moves the ball up, increase the y by 20px
    paddle_b.sety(y) # set the old y to the new y

def paddle_b_down(): #define the function
    y = paddle_b.ycor() # returns the y coordinates of the paddle
    y -= 20 # moves the ball up, increase the y by 20px
    paddle_b.sety(y) # set the old y to the new y

# Keyboard binding
wn.listen() # listen for keyboard entry
wn.onkeypress(paddle_a_up, "e")
wn.onkeypress(paddle_a_down, "z")
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, "m")

#Main game loop
while True:
    wn.update() #updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290: # if the ball y coordinated reached the top of the screen then this
        ball.sety(290)
        ball.dy *= -1 # reverses the direction of the ball

    if ball.ycor() < -290: # if the ball y coordinate reached the bottom of the screen then this
        ball.sety(-290)
        ball.dy *= -1 # reverses the direction of the ball

    if ball.xcor() > 390: # if the ball get by one of the paddle we will reset the position of the ball
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()  # will clear the previous draw
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390: # if the ball get by one of the paddle we will reset the position of the ball
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear() # will clear the previous draw
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision | if the balls coordinates aline with the coordinates of the paddle than the ball will reverse
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
