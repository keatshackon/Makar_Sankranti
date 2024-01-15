from turtle import Turtle, Screen

FONT = ("Courier", 20, "normal")


def Banner():
    kite.hideturtle()
    kite.penup()
    kite.goto(-300, 300)
    kite.color("Blue")
    kite.pensize(3)
    kite.write(f"Happy Makar Sankranti\nChacha!", align='left', font=FONT)


def creating_kite_tail():
    # tail_1 of kite
    kite.penup()
    kite.goto(286, 263)
    kite.setheading(230)
    kite.pendown()
    kite.pensize(3)
    kite.color("red")
    kite.forward(38)

    # tail_2 of kite
    kite.penup()
    kite.goto(286, 263)
    kite.setheading(265)
    kite.pendown()
    kite.pensize(3)
    kite.color("blue")
    kite.forward(35)

    # # tail_3 of kite
    kite.penup()
    kite.goto(286, 263)
    kite.setheading(290)
    kite.pendown()
    kite.pensize(3)
    kite.color("green")
    kite.forward(38)


def creating_kite():
    kite.penup()
    kite.goto(300, 350)
    kite.setheading(225)
    kite.pendown()
    kite.pensize(3)
    kite.forward(50)

    kite.penup()
    kite.goto(300, 350)
    kite.setheading(300)
    kite.pendown()
    kite.pensize(3)
    kite.forward(50)

    kite.penup()
    kite.goto(300, 350)
    kite.setheading(260)
    kite.pendown()
    kite.pensize(3)
    kite.forward(90)

    # # left lower part
    kite.penup()
    kite.goto(264, 317)
    kite.setheading(290)
    kite.pendown()
    kite.pensize(3)
    kite.forward(57)

    # Right lower part
    kite.penup()
    kite.goto(326, 308)
    kite.setheading(229)
    kite.pendown()
    kite.pensize(3)
    kite.forward(65)

    # knot first/upper
    kite.penup()
    kite.goto(297, 330)
    kite.setheading(240)
    kite.pendown()
    kite.pensize(3)
    kite.color("orange")
    kite.forward(40)

    # # knot Second/upper
    kite.penup()
    kite.goto(287, 290)
    kite.setheading(135)
    kite.pendown()
    kite.pensize(3)
    kite.color("orange")
    kite.forward(14)

    creating_kite_tail()

def Thread():
    kite.penup()
    kite.goto(280, 298)
    kite.setheading(220)
    kite.pendown()
    kite.pensize(3)
    kite.color("orange")
    kite.forward(616)

def creating_lattai():
    kite.penup()
    kite.color("black")
    kite.goto(-280, -30)
    kite.pendown()
    kite.pensize(3)
    kite.circle(30)

    # round wala part 2
    kite.penup()
    kite.goto(-200, -130)
    kite.pendown()
    kite.pensize(3)
    kite.circle(30)

    # kahri khari 1
    kite.penup()
    kite.goto(-280, -30)
    kite.pendown()
    kite.pensize(2)
    kite.setheading(310)
    kite.forward(135)

    # kahri khari 2
    kite.penup()
    kite.goto(-255, -28)
    kite.pendown()
    kite.pensize(2)
    kite.setheading(310)
    kite.forward(133)

    # kahri khari 3
    kite.penup()
    kite.goto(-292, -50)
    kite.pendown()
    kite.pensize(2)
    kite.setheading(310)
    kite.forward(130)

    # kahri khari 4
    kite.penup()
    kite.goto(-260, -75)
    kite.pendown()
    kite.pensize(2)
    kite.setheading(310)
    kite.forward(89)

    # rod 1_1
    kite.penup()
    kite.goto(-190, -150)
    kite.pendown()
    kite.pensize(2)
    kite.setheading(310)
    kite.forward(90)

    # rod 1_2
    kite.penup()
    kite.goto(-180, -150)
    kite.pendown()
    kite.pensize(2)
    kite.setheading(310)
    kite.forward(90)

    # rod 2_1
    kite.penup()
    kite.goto(-288, -39)
    kite.pendown()
    kite.pensize(2)
    kite.setheading(130)
    kite.forward(65)

    # rod 2_2
    kite.penup()
    kite.goto(-281, -32)
    kite.pendown()
    kite.pensize(2)
    kite.setheading(130)
    kite.forward(70)


screen = Screen()
screen.setup(width=790, height=800)
screen.title("Makkar Ka Chakkar")

kite = Turtle()

Banner()
creating_kite()
Thread()
creating_lattai()

screen.exitonclick()
