import turtle
import pandas as pd

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("India States Game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("india_states.csv")
new_data = data["state_names"].to_list()
guessed_states = []

while len(guessed_states) < 29:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 correctly guessed State",
                                    prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        missing_states = [state for state in new_data if state not in guessed_states]
        remaining_data = pd.DataFrame(missing_states)
        remaining_data.to_csv("remaining_states.csv")
        break
    if answer_state in new_data:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state_names == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()