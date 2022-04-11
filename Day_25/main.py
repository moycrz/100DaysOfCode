import turtle
import pandas

score = 0
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("U.S. State Game")

data = pandas.read_csv("50_states.csv")
states = data["state"]


def find_state(state):
    """Read, find and separate the state"""
    state_actual = data[data.state == f"{state}"]
    state_x = int(state_actual.x)
    state_y = int(state_actual.y)
    coord = (state_x, state_y)
    return coord


list_states = [state for state in states]
guessed_states = []

while score < len(states):

    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in list_states:
        guessed_states.append(answer_state)
        t_state = turtle.Turtle()
        t_state.penup()
        t_state.hideturtle()
        t_state.goto(find_state(answer_state))
        t_state.write(f"{answer_state}")

        score += 1










