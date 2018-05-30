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

# Write HEDDA ...
# ***************
# bokstaven 'H':
h.left(90)
h.forward(100)
h.right(90)
h.penup()
h.setposition(0, 50)
h.pendown()
h.forward(50)
h.penup()
h.setposition(50, 0)
h.pendown()
h.left(90)
h.forward(100)

# Step 4: We're done!
turtle.done()
