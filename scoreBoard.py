from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(100,200)
        self.penup()
        self.left_score =0
        self.right_score=0
        self.font = ("Courier",80,"normal")

    def update_scoreBoard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.left_score,align="center",font=self.font)
        self.goto(100,200)
        self.write(self.right_score,align="center",font=self.font)

    def l_score_update(self):
        self.left_score+=1
        self.update_scoreBoard()

    def r_score_update(self):
        self.right_score+=1
        self.update_scoreBoard()