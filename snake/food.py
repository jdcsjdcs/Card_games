from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.6, 0.6)
        self.shape('square')
        self.color('red')
        self.speed('fastest')
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
        self.refresh()
                
                
    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
                  
            