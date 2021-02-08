import turtle
import pandas
screen = turtle.Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)
guessed_states = []
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Type a state name").title()
    state_data = data[data["state"] == answer_state]
    if answer_state == 'Exit':
        not_guessed_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(not_guessed_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(float(state_data.x), float(state_data.y))
        t.write(f"{answer_state}")
        guessed_states.append(answer_state)








turtle.mainloop()
