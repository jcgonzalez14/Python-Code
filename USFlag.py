#  File: USFlag.py
#  Description:
#  Student's Name: Julio Gonzalez
#  Student's UT EID: jcg3245
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 9/12/16
#  Date Last Modified: 9/15/16

def main():


    a = eval (input ("Enter height of the flag: ")) 
    b = a*1.9
    c = a*(7/13)
    d = b*(2/5)
    e = c/10
    g = d/12
    l = a/13
    k = l*(4/5)

    
    import turtle 
    
    ttl = turtle.Turtle()
    
    screen = turtle.Screen()
    screen.setup(b+100,a+100, 0, 0)
    screen.title ("Class demo of Turtle Graphics")

    ttl.speed(3)
    ttl.penup() 
    ttl.goto(-b/2,-a/2) 
    ttl.pendown()

    ttl.fillcolor("red")
    ttl.begin_fill()
    ttl.forward(b)
    ttl.left(90)
    ttl.forward(a)
    ttl.left(90)
    ttl.forward(b)
    ttl.end_fill()

    for i in range(6):

        ttl.fillcolor("white")
   
        ttl.left(90)
        ttl.begin_fill()
        ttl.forward(l)
        ttl.left(90)
        ttl.forward(b)
        ttl.right(90)
        ttl.forward(l)
        ttl.right(90)
        ttl.forward(b)
        ttl.end_fill()
        
    ttl.fillcolor("black")
    ttl.begin_fill()
    ttl.left(90)
    ttl.forward(l)
    ttl.left(180)
    ttl.forward(a)
    ttl.right(90)

    ttl.fillcolor("blue")
    ttl.begin_fill()
    ttl.forward(d)
    ttl.right(90)
    ttl.forward(c)
    ttl.right(90)
    ttl.forward(d)
    ttl.end_fill()
    ttl.right(90)
    ttl.forward(e)
   
    ttl.penup()
    ttl.right(90)
    ttl.forward(g/2)
    ttl.pendown

    for i in range(5):
        for i in range(6):           
            ttl.fillcolor("white")
            ttl.begin_fill()
            ttl.forward(k/3)
            ttl.left(72)
            ttl.forward(k/3)
            ttl.right(144)
            ttl.forward(k/3)
            ttl.left(72)
            ttl.forward(k/3)
            ttl.right(144)
            ttl.forward(k/3)
            ttl.left(72)
            ttl.forward(k/3)
            ttl.right(144)
            ttl.forward(k/3)
            ttl.left(72)
            ttl.forward(k/3)
            ttl.right(144)
            ttl.forward(k/3)
            ttl.left(72)
            ttl.forward(k/3)
            ttl.end_fill()
            ttl.right(144)
            
            ttl.forward(g*2)
        
        ttl.right(180)
        ttl.forward(d)
        ttl.right(90)
        ttl.forward(2*e)
        ttl.right(90)

    ttl.right(90)
    ttl.forward(c-e)
    ttl.left(90)
    ttl.forward(g)
    
    for i in range(4):
        for i in range(5):           
            ttl.fillcolor("white")
            ttl.begin_fill()
            ttl.forward(k/3)
            ttl.left(72)
            ttl.forward(k/3)
            ttl.right(144)
            ttl.forward(k/3)
            ttl.left(72)
            ttl.forward(k/3)
            ttl.right(144)
            ttl.forward(k/3)
            ttl.left(72)
            ttl.forward(k/3)
            ttl.right(144)
            ttl.forward(k/3)
            ttl.left(72)
            ttl.forward(k/3)
            ttl.right(144)
            ttl.forward(k/3)
            ttl.left(72)
            ttl.forward(k/3)
            ttl.end_fill()
            ttl.right(144)
            
            ttl.forward(g*2)
        
        ttl.right(180)
        ttl.forward(d-g-g)
        ttl.right(90)
        ttl.forward(2*e)
        ttl.right(90)

main()
