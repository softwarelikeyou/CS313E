import turtle

## Hoist (height) of the flag: A = 1.0
## Fly (width) of the flag: B = 1.9[54]
## Hoist (height) of the canton ("union"): C = 0.5385 (A × 7/13, spanning seven stripes)
## Fly (width) of the canton: D = 0.76 (B × 2/5, two-fifths of the flag width)
## E = F = 0.0538 (C/10, One-tenth of the height of the canton)
## G = H = 0.0633 (D/12, One twelfth of the width of the canton)
## Diameter of star: K = 0.0616 (L × 4/5, four-fifths of the stripe width, the calculation only gives 0.0616 if L is first rounded to 0.077)
## Width of stripe: L = 0.0769 (A/13, One thirteenth of the flag height)

## https://docs.python.org/3.1/library/turtle.html

RED = "#B22234"
WHITE = "#FFFFFF"
BLUE = "#3C3B6E"

def border(t, screen_x, screen_y):
    # Lift the pen and move the turtle to the center.
    t.penup()
    t.home()
    print(str(screen_x) + "," + str(screen_y))
    t.forward(screen_x / 2)
    t.right(90)
    t.forward(screen_y / 2)
    t.setheading(180)           
    t.pencolor('black')
    t.pendown()
    t.pensize(1)
    for distance in (screen_x, screen_y, screen_x, screen_y):
        t.forward(distance)
        t.right(90)
        print(t.position())
    t.penup()
    t.home()

def drawCanton(t, hoist, fly):
    C = round(hoist * (7/13),4)
    D = round(fly * (2/5),4)
    t.penup()
    t.home()
    t.forward((fly/2) * -1)
    t.left(90)
    t.forward(hoist/2)
    t.setheading(180)
    t.pencolor(BLUE)
    t.pendown()
    t.pensize(1)
    t.fillcolor(BLUE)
    t.begin_fill()
    for distance in (D, C, D, C):
        t.backward(distance)
        t.right(90)
        print(t.position())
    t.end_fill()
    t.penup()
    t.home()

def drawStrips(t, A, B):
    color = RED
    offset = 0
    for i in range(0, 14):
        t.penup()
        t.home()
        t.forward(B/2)
        t.right(90)
        t.forward((A/2) - offset)
        t.setheading(180)
        t.pencolor(color)
        t.pendown()
        t.pensize(1)
        t.fillcolor(color)
        t.begin_fill()
        for distance in (B, A/13, B, A/13):
            t.forward(distance)
            t.right(90)
        t.end_fill()
        t.penup()
        t.home()
        if color == RED:
            color = WHITE
        else:
            color = RED
        offset += A/13

def drawStars(t, A, B):
    C = round(A * (7/13),4)
    D = round(B * (2/5),4)
    L = round(A/13,4)
    K = round(L * (4/5),4)
    F = round(C/9,4)
    H = round(D/11,4)
    X = (B/2) * -1
    Y = A/2
    t.penup()
    t.home()
    t.forward(X)
    t.left(90)
    t.forward(Y)
    t.right(90)
    t.pencolor('red')
    t.pensize(5)
    t.goto(X,Y)
    #X += H
    Y -= F*.90
    for y in range(9):
        if y%2 == 0:
            X += H
            P = 6
        else:
            X += H*1.85
            P = 5
        
        for h in range(P):
            t.goto(X, Y)
            drawStar(t, A, B)
            X += H * 1.75
        X = (B/2) * -1
        Y -= F*.90

def drawStar(t, A, B):
        C = round(A * (7/13),4)
        D = round(B * (2/5),4)
        L = round(A/13,4)
        K = round(L * (4/5),4)
        t.setheading(72)
        t.pencolor(WHITE)
        t.pendown()
        t.pensize(1)
        t.fillcolor(WHITE)
        t.begin_fill()
        t.left(72)
        for i in range(5):
            t.forward(K/3)
            t.right(144)
            t.forward(K/3)
            t.left(72)
        t.end_fill()
        t.penup()
        
def main():
    #A = 300
    A = eval(input("Enter hoist size: "))
    
    B = round(A * 1.954,4)
    C = round(A * (7/13),4)
    D = round(B * (2/5),4)
    E = round(C/10,4)
    F = round(E,4)
    G = round(D/12,4)
    H = round(G,4)
    L = round(A/13,4)
    K = round(L * (4/5),4)


    
    window_width = 100 + B + 100
    window_height = 100 + A + 100
    screen = turtle.Screen()
    screen.title('Raise The Flag!')
    screen.setup(width = window_width, height = window_height, startx = None, starty = None)
    screen.screensize(B, A, "white")
    screen_x, screen_y = screen.screensize()
    t = turtle.Turtle()
    t.speed(0)
    #border(t, screen_x, screen_y)
    print("\n")
    print("\n")
    drawStrips(t, A, B)
    drawCanton(t, A, B)
    print("\n")
    print("\n")
    drawStars(t, A, B)

    t.pen(shown=False)
    screen.mainloop()
main()
