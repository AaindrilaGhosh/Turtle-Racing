import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'yellow', 'purple', 'pink', 'brown', 'cyan', 'orange', 'black']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            continue
        
        if 2<= racers <= 10:
            return racers
        else:
            print("Number is not in  range 2-10. Try again!")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

    # Force window to the front (works on most systems)
    try:
        screen._root.attributes('-topmost', 1)  # Bring to front
        screen._root.attributes('-topmost', 0)  # Allow normal behavior
    except:
        pass  # Ignore errors if unsupported

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1) 
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)                  #By default, the objects the pointed right (this way the turtle will be pointing upwards.)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color: ", winner)
time.sleep(5)