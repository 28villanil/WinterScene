import turtle
t=turtle.Turtle()
import random
screen = turtle.Screen()


screen.bgcolor('royalblue4')


t.speed(0)
t.penup()
t.goto(-325,-100)
t.pencolor('red')
t.fillcolor('red')
t.begin_fill()
t.pendown()
t.pensize(4)
t.forward(900)
t.right(90)
t.forward(900)
t.right(90)
t.forward(900)
t.right(90)
t.forward(900)
t.right(90)
t.end_fill()




t.fillcolor('SpringGreen')
t.pencolor('SpringGreen')
for i in range(20):
   t.penup()
   t.goto(-1000+i*100,-100)
   t.pendown()
   t.begin_fill()
   t.forward(50)
   t.right(90)
   t.forward(1000)
   t.right(90)
   t.forward(50)
   t.right(90)
   t.forward(1000)
   t.right(90)
   t.end_fill()




for i in range(20):
   t.pencolor('white')
   x = random.randint(-245,-155)
   y = random.randint(155,245)
   t.penup()
   t.goto(x,y)
   t.pendown()
   z = random.randint(0,2)
   t.pensize(z)
   t.dot()


for i in range(20):
   t.pencolor('white')
   x = random.randint(155,245)
   y = random.randint(155,245)
   t.penup()
   t.goto(x,y)
   t.pendown()
   z = random.randint(0,2)
   t.pensize(z)
   t.dot()


t.pencolor('black')
t.pensize(8)
t.penup()
t.goto(-250,250)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.penup()
t.goto(-200,250)
t.pendown()
t.right(90)
t.forward(100)
t.penup()
t.goto(-250,200)
t.pendown()
t.left(90)
t.forward(100)


t.penup()
t.goto(150,250)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.penup()
t.goto(200,250)
t.pendown()
t.right(90)
t.forward(100)
t.penup()
t.goto(150,200)
t.pendown()
t.left(90)
t.forward(100)


t.pencolor('brown')
t.pensize(15)
t.penup()
t.goto(-175,-200)
t.pendown()
t.goto(-175,-300)


t.pensize(1)
t.pencolor('Green')
t.fillcolor('Green')
t.begin_fill()
t.penup()
t.goto(-250,-250)
t.pendown()
t.goto(-100,-250)
t.goto(-175,50)
t.goto(-250,-250)
t.end_fill()


t.fillcolor('pink')
t.begin_fill()
t.pencolor('pink')
t.pensize(7)
t.penup()
t.goto(-250,-300)
t.pendown()
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.pencolor('yellow')
t.end_fill()
t.penup()
t.goto(-250,-325)
t.pendown()
t.right(90)
t.forward(50)
t.penup()
t.goto(-225,-300)
t.pendown()
t.right(90)
t.forward(25)
t.forward(25)




t.fillcolor('purple')
t.begin_fill()
t.pencolor('purple')
t.pensize(7)
t.penup()
t.goto(-100,-300)
t.pendown()
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.pencolor('blue')
t.end_fill()
t.penup()
t.goto(-100,-325)
t.pendown()
t.right(180)
t.forward(50)
t.penup()
t.goto(-125,-300)
t.pendown()
t.left(90)
t.forward(25)
t.forward(25)




t.pensize(6)
t.pencolor('yellow')
t.penup()
t.goto(-219,-187)
t.pendown()
t.dot()


t.pencolor('red')
t.penup()
t.goto(-169,-29)
t.pendown()
t.dot()


t.pencolor('orange')
t.penup()
t.goto(-179,-107)
t.pendown()
t.dot()


t.pencolor('purple')
t.penup()
t.goto(-148,-198)
t.pendown()
t.dot()


t.pencolor('white')
t.penup()
t.goto(-175,-201)
t.pendown()
t.dot()




t.pencolor('pink')
t.penup()
t.goto(-158,-89)
t.pendown()
t.dot()


t.pencolor('silver')
t.penup()
t.goto(-163,-228)
t.pendown()
t.dot()


t.pencolor('gold')
t.penup()
t.goto(-178,-178)
t.pendown()
t.dot()


t.hideturtle()


t.setheading(0)
t.pensize(3)
t.pencolor('gold')




t.penup()
t.fillcolor('gold')


t.goto(-195,65)


t.begin_fill()
t.pendown()
t.forward(40)
t.right(144)
t.forward(40)
t.right(144)
t.forward(40)
t.right(144)
t.forward(40)
t.right(144)
t.forward(40)
t.right(144)
t.forward(40)
t.end_fill()


t.pensize(12)
t.pencolor('green')
t.penup()
t.goto(0,250)
t.pendown()
t.circle(40)


t.pensize(12)
t.pencolor('royalblue4')
t.penup()
t.goto(0,275)
t.pendown()
t.circle(20)


t.pensize(4)
t.pencolor('red')
t.penup()
t.goto(0,328)
t.pendown()
t.dot()
t.penup()
t.goto(35,300)
t.pendown()
t.dot()
t.penup()
t.goto(0,250)
t.pendown()
t.dot()
t.penup()
t.goto(-35,300)
t.pendown()
t.dot()


t.showturtle()

t.fillcolor('tan')
t.begin_fill()
t.pencolor('tan')
t.penup()
t.goto(100,-250)
t.pendown()
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.end_fill()


t.fillcolor('firebrick4')

t.pencolor('firebrick4')
t.penup()
t.goto(160,-160)
t.begin_fill()
t.pendown()
t.forward(170)
t.left(90)
t.forward(170)
t.left(90)
t.forward(170)
t.left(90)
t.forward(70)
t.end_fill()

t.pencolor('red')
t.penup()
t.goto(0,175)
t.pendown()
t.write("Merry Christmas!!! ", font=("Arial", 24, "bold"), align="center")
turtle.done()

