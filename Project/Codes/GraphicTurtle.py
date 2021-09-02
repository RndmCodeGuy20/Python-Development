import turtle as t

turt = t.Turtle()

def drawShape(numSides):
    angle = 360 / numSides
    for _ in range(numSides):
        turt.forward(100)
        turt.right(angle)

for shapeN in range(3,11):
    drawShape(shapeN)