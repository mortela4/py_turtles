import turtle

spiral = turtle.Turtle()

# Dette er startfargen:
spiral.pencolor("green")

for i in range(100):
    spiral.forward(i * 10)
    spiral.right(144)
    # Sjekker hvilken iterasjon i sløyfen vi er i:
    if i > 25 and i < 50:
        spiral.pencolor("blue")
    if i > 50 and i < 75:
        spiral.pencolor("yellow")
    if i > 75 and i < 100:
        spiral.pencolor("red")

turtle.done()

