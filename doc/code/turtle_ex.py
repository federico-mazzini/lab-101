import turtle
import random

t = turtle.Turtle()
t.speed(0)  # velocità massima
turtle.bgcolor("black")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(100):
    t.color(random.choice(colors))
    t.pensize(i / 10 + 1)
    t.forward(i * 2)
    t.left(59)  # angolo strano = effetto spirale
turtle.done()