import turtle

def draw_hex():

    window = turtle.Screen()
    window.bgcolor("#d17e47")

    #  Initialize Turtle:
    A = turtle.Turtle()
    A.shape("turtle")
    A.color("yellow","red")
    A.speed(300000)
    
 
    #  Draw Hexagons:
    
    for i in range(36):
        A.right(10)
        for i in range(6):
            A.forward(100)
            A.right(60)
            A.begin_fill()
    A.right(90)
    A.forward(300)
    
    
    A.home() 
    A.end_fill()
    window.exitonclick()

draw_hex()
