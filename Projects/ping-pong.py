import turtle

name1 = input()
name2 = input()

#окно
window = turtle.Screen()
window.title('Ping-Pong')
window.setup(width=1.0, height = 1.0)
window.bgcolor('black')
window.tracer(0)

#поле для игры 1000 на 600
border = turtle.Turtle()
border.color('green')
border.speed(0) #мнговенно
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()
border.goto(0, 300)
border.setheading(270)
border.color('white')
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

#левая рокетка 
rocet_left = turtle.Turtle(shape = 'square')
rocet_left.speed(0)
rocet_left.color('white')
rocet_left.shapesize(stretch_len=1, stretch_wid=5)
rocet_left.up()
rocet_left.goto(-450,0)

def move_up_left():
    y = rocet_left.ycor() + 10
    if y > 250:
        y = 250
    rocet_left.sety(y)

def move_down_left():
    y = rocet_left.ycor() - 10
    if y < -250:
        y = -250
    rocet_left.sety(y)

#правая рокетка 
rocet_right = turtle.Turtle(shape = 'square')
rocet_right.speed(0)
rocet_right.color('white')
rocet_right.shapesize(stretch_len=1, stretch_wid=5)
rocet_right.up()
rocet_right.goto(450,0)

def move_up_right():
    y = rocet_right.ycor() + 10
    if y > 250:
        y = 250
    rocet_right.sety(y)

def move_down_right():
    y = rocet_right.ycor() - 10
    if y < -250:
        y = -250
    rocet_right.sety(y)

#движение ракеток
window.listen()
window.onkeypress(move_up_left, 'w')
window.onkeypress(move_down_left, 's')
window.onkeypress(move_up_right, 'Up')
window.onkeypress(move_down_right, 'Down')

#мячик
ball = turtle.Turtle(shape = 'circle')
ball.color('white')
ball.speed(0)
ball.penup()
ball.goto(0, 0)

dx = 0.4
dy = 0.4

#счет
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 340)
pen.write('{}: 0  {}: 0'.format(name1, name2), align='center', font=('Times New Roman', 24, 'normal'))

score_left = 0
score_right = 0

while True:
    window.update()

    #движение мяча
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)
    
    if ball.ycor() > 290:
        ball.sety(290)
        dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        dy *= -1
        
    if ball.xcor() > 490:
        ball.goto(0, 0)
        dx *= -1
        score_left += 1
        pen.clear()
        pen.write('{}: {}  {}: {}'.format(name1, score_left, score_right, name2), align='center', font=('Times New Roman', 24, 'normal'))
        
    if ball.xcor() < -490:
        ball.goto(0, 0)
        dx *= -1
        score_right += 1
        pen.clear()
        pen.write('{}: {}  {}: {}'.format(name1, score_left, score_right, name2), align='center', font=('Times New Roman', 24, 'normal'))
        
    #столкновение мяча с рокетками
    if ball.xcor() > 440 and ball.xcor() < 450 and (ball.ycor() < rocet_right.ycor()+50 and ball.ycor() > rocet_right.ycor()-50):
        ball.setx(440)
        dx *= -1
    if ball.xcor() < -440 and ball.xcor() > -450 and (ball.ycor() < rocet_left.ycor()+50 and ball.ycor() > rocet_left.ycor()-50):
        ball.setx(-440)
        dx *= -1

    
window.mainloop()
