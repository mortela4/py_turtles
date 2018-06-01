# Oppgave:
# skriv "HEDDA" med turtle!
# =========================
# Eksempel-bokstav:
#
# 100 -   |      |
#         |      |
# 50  -   |------|
#         |      |
# 0   -   |      |
#         0      50     100

import turtle

# Step 2: Create a new turtle. We'll call it "hedda"
h = turtle.Turtle()
h.shape('turtle')
h.color('red')

# Write HEDDA ...
# ***************
# bokstaven 'H':
h.left(90)
h.forward(100)
h.right(90)   # Må snu retning til forover igjen (d.v.s. 90 grader til høyre igjen)
h.penup()
h.setposition(0, 50)
h.pendown()
h.forward(50)
h.penup()
h.setposition(50, 0)
h.pendown()
h.left(90)
h.forward(100)
h.back(50)
h.right(90)
h.penup()
h.setposition(100,50)
h.left(90)
h.forward(50)
h.right(180)
h.pendown()
h.forward(100)
h.left(90)
h.forward(50)
h.back(50)
h.left(90)
h.forward(40)
h.right(90)
h.forward(30)
h.penup()
h.setposition(100,100)
h.pendown()
h.forward(50)
h.penup()
h.setposition(200,100)
h.pendown()
h.right(90)
h.forward(100)
h.left(135)
h.forward(70)
h.left(80)
h.setposition(200,100)
h.penup()
h.setposition(300,100)
h.pendown()
h.right(215)
h.forward(100)
h.left(135)
h.forward(70)
h.left(80)
h.setposition(300,100)
h.penup()
h.setposition(400,100)
h.left(145)
h.left(30)
h.pendown()
h.forward(100)
h.setposition(400,100)
h.right(60)
h.forward(100)
h.setposition(400,100)
h.forward(50)
h.left(120)
h.forward(50)
h.penup()
h.setposition(100,100)

# Step 4: We're done!
turtle.done()
