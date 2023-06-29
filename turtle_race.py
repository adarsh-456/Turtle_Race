from turtle import Turtle, Screen
import random 
scr=Screen()
scr.setup(width=1000, height=500)
user_bet=scr.textinput(title="make your bet", prompt="which turtle will win the race? enter the color: ")
colors=["red", "orange", "pink", "yellow", "blue", "black", "purple", "grey", "green"]
y_positions=[-120, -90, -60, -30, 0, 30, 60, 90, 120]
all_turtles=[]
for turtle_index in range(9):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-480,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True
    
while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor()>480:
            is_race_on=False
            winning_color = turtles.pencolor()
            if winning_color== user_bet:
                print(f"you won! The {winning_color} turtle is winner!")
            else:
                print(f"you have lost! The {winning_color} turtle is the winner!")
                
        rand_distance=random.randint(0, 18)
        turtles.forward(rand_distance)
    
scr.exitonclick()