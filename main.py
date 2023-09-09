import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")

state_dict = data.state.to_dict()
x_dict = data.x.to_dict()
y_dict = data.y.to_dict()

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.color("black")

bubble_title = "Guess the State"
state_num = 0
guessed_states = []

while state_num < 50:
    answer_state = screen.textinput(title=bubble_title, prompt="What's another state's name?")
    if answer_state.lower() == "exit":
        missing_states = [] #[state.title() for state in state_dict if state not in guessed_states]
        missing_x = [] #[x_dict for state in state_dict if state not in guessed_states] - Wrong?
        missing_y = [] #[y_dict for state in state_dict if state not in guessed_states] - Wrong?
        for state in state_dict:
            if state_dict[state] not in guessed_states:
                missing_states.append(state_dict[state].title())
                missing_x.append(x_dict[state])
                missing_y.append((y_dict[state]))
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        for index in range(len(missing_states)):
            tim.color("red")
            tim.goto(x=int(missing_x[index]), y=int(missing_y[index]))
            tim.write(missing_states[index])
        break
    for state in state_dict:
        if answer_state.lower() == state_dict[state].lower():
            guessed_states.append(state_dict[state])
            tim.goto(x=x_dict[state], y=y_dict[state])
            tim.write(state_dict[state])
            state_num += 1
            bubble_title = f"{state_num}/50 States Correct"

screen.exitonclick()
# states_to_learn.csv






