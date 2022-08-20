#program to replicate sporkle.com state quiz game
from turtle import Turtle, Screen

import pandas
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")

# code to set turtle object to an image
image = "blank_states_img.gif"
screen.addshape(image)
Turtle().shape(image)

# # Mouse click event in turtle
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
#converting the csv into dataframe
us_states_data = pd.read_csv("50_states.csv")

#converting the state column of the dataframe into a list
states_list = us_states_data['state'].tolist()

guessed_states = []
while len(guessed_states) < 50: # game would run till 50 turns until we manually exit from te game

    # taking the guess input from user and storing it to a variable named answer_state
    answer_state = screen.textinput(title="Guess the State", prompt="whats another state name").title()

    # game ending condition: before breaking from the loop creating a list of states user missed to guess
    # and converting it to a csv file
    if answer_state == 'Exit':
        #using list comprehension
        missing_states = [state for state in states_list if state not in guessed_states]
    #     missing_states = []
    #     for state in states_list:
    #         if state not in guessed_states: # checking for each state in states_list if not present
    #             missing_states.append(state) # in guessed list then append that state in missing state

        new_data = pandas.DataFrame(missing_states) # converting the list into a dataframe
        new_data.to_csv("missed_states.csv") # converting the dataframe into a csv
        break # Exit from the game



    # if guess is present in states_list enter in below condition
    if answer_state in states_list:

        #appending the state in guessed_states list
        guessed_states.append(answer_state)

        #retrieving the row of answer_state like : Alabama 139 -77
        row_state = us_states_data[us_states_data.state == answer_state]

        x_cor = int(row_state.x) # from the row taking the x cell value and converting to int
        #as this would give only the cell value like 139
        y_cor = int(row_state.y) # like -77

        # creating a new turtle
        turtle1 = Turtle()
        turtle1.penup()
        turtle1.goto(x_cor, y_cor) # turtle moving to corresponding state's x and y positio
        turtle1.hideturtle()
        turtle1.write(answer_state) # turtle writing the state name in the specified position












#screen.exitonclick()
