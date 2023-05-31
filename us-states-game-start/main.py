import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_coord_onclick(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_coord_onclick)
data = pandas.read_csv("50_states.csv")
is_game_on = True
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name ? ").title()
guess_states = []
states = data["state"].to_list()
missing_states = []
while is_game_on:
    if len(guess_states) == 0:
        pass
    else:
        answer_state = screen.textinput(title=f"{len(guess_states)}/50",
                                        prompt="What's another state's name ? ").title()
    if answer_state in states:
        state_row = data[data.state == answer_state]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_cor = int(state_row.x), int(state_row.y)
        t.goto(state_cor)
        t.write(answer_state)
    if answer_state == 'Exit':
        is_game_on = False
        missing_states = [state for state in states if state not in guess_states]

    guess_states.append(answer_state)
new_data = (pandas.DataFrame(missing_states))
new_data.to_csv('missed_states.csv')
