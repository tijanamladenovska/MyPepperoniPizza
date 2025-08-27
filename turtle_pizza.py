import turtle  # Python's built-in graphics library for drawing

# --- Constants for colors and pepperoni placement ---
BACKGROUND_COLOR = "#9EC388"
CRUST_COLOR = "#ECA84F"
SAUCE_COLOR = "#AD0509"
CHEESE_COLOR = "#FBC70F"

# Each pair [x, y] defines where a pepperoni will be drawn on the pizza
PEPPERONI_LOCATIONS = [
    [-70, 105], [-85, 175], [-25, 50], [-15, 100],
    [-25, 150], [-30, 205], [15, 50], [20, 120],
    [60, 156], [71, 215], [80, 90], [95, 150]
]

# --- Screen setup ---
screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR)  # background color (like a plate/tablecloth)
screen.title("My Pizza")  # window title

# --- Turtle setup ---
my_turtle = turtle.Turtle()
my_turtle.pensize(5)     # line thickness
my_turtle.shape("circle")  # gives the turtle a circle shape for fun

# --- Helper functions ---

def draw_circle(radius, line_color, fill_color):
    """
    Draws a filled circle with the given radius and colors.
    Used to draw the crust, sauce, cheese, and pepperoni.
    """
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()

def move_turtle(x, y):
    """
    Moves the turtle to a specific (x, y) coordinate
    without drawing on the way.
    """
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()

# --- Draw the pizza base ---
draw_circle(150, CRUST_COLOR, CRUST_COLOR)  # crust
move_turtle(0, 25)
draw_circle(125, SAUCE_COLOR, CHEESE_COLOR)  # sauce + cheese layer

# --- Add pepperoni toppings ---
for location in PEPPERONI_LOCATIONS:
    move_turtle(location[0], location[1])
    draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)

# --- Slice the pizza into 8 pieces ---
move_turtle(0, 150)
my_turtle.color(BACKGROUND_COLOR)  # use background color for slice lines

for x in range(8):
    my_turtle.pendown()
    my_turtle.left(45)  # angle between slices (360/8)
    my_turtle.forward(150)
    my_turtle.penup()
    my_turtle.backward(150)

# --- Finish drawing ---
turtle.done()


