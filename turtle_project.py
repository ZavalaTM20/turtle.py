import turtle

screen = turtle.Screen()
screen.bgcolor("white")

flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)
flower.color("red")

# Function 1 
def draw_petal():
    flower.circle(100, 60)  # Draws an arc (petal shape)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)

# Function 2 
def draw_flower(petals):
    for _ in range(petals):
        draw_petal()
        flower.left(360 / petals)  # Rotate to draw the next petal

# Function 3
def bloom():
    flower.penup()
    flower.goto(0, -100)  # Move turtle to starting position
    flower.pendown()
    
    petals = 1  # Start with one petal and increase
    while petals <= 12:
        flower.clear()  # Clear the screen to show the blooming effect
        draw_flower(petals)
        petals += 1
        turtle.delay(200)  # Wait between steps to create animation

# Function 4
bloom()

# Run Statement 
flower.hideturtle()
turtle.done()
