import turtle 
import random 

#Screen 
screen = turtle.Screen()
screen.title("Guess_the_Number_Game")
screen.bgcolor("aqua")


#turtle
Pen = turtle.Turtle()
Pen.speed(0)
Pen.penup()
Pen.goto(0,200)            #Postion in coordinates
Pen.hideturtle()


#Generating a random number that the user will guess
target_number = random.randint(1,20)   #Generate a number btw 1 and 20 that will be our targeted number


def make_a_guess():
    guess = screen.numinput("Guess a Number", "Enter your Guess:")
    Pen.clear()

    if guess is None:
        return
    Pen.goto(10,100)
    Pen.write("Your guess: {}".format(guess), align="center", font=("Arial", 16, "normal") )

    if guess<target_number:
        Pen.goto(0,0)
        Pen.write("Too Low!", align="center", font=("Arial", 16, "normal"))
    elif guess>target_number:
        Pen.goto(0,0)
        Pen.write("Too High!", align="center", font=("Arial", 16, "normal"))
    elif guess==target_number :
        Pen.goto(0,0)
        Pen.write("Congratulations", align="center", font=("Arial", 16, "normal"))

    else:
        return

for i in range(10):{
    make_a_guess()
}



    
#close
screen.exitonclick()

turtle.done()



