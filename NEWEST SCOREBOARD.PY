

####we need to define the player class
def show_status(self):

        self.pen.undo()

        msg = "PLAYER: %s" %(self.score)

        self.pen.penup()

        self.pen.goto(75,
200)

        self.pen.write(msg, 
font=("Times New Roman", 
18, "normal"))




            game.score += 1

            game.show_status()