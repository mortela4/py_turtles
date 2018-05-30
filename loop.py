import turtle

smart_turtle = turtle.Turtle()

# Loop 4 times. Everything I want to repeat is
# *indented* by four spaces.
for i in range(4):
    smart_turtle.forward(50)
    smart_turtle.right(90)

# This isn't indented, so we aren't repeating it.
turtle.done()
