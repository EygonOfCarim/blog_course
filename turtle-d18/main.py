from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def move_turtle(faces: int, t: Turtle):
    tim.color(random.choice(colors))
    for i in range(faces):
        t.forward(100)
        t.right(360 / faces)


for faces in range(3, 10):
    move_turtle(faces, tim)

screen = Screen()
screen.exitonclick()
