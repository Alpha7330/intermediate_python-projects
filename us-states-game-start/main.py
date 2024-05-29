import turtle as t
import pandas
screen=t.Screen()
screen.title("us-states-game")
img="blank_states_img.gif"
screen.addshape(img)
t.shape(img)
# def get_mouse_click_coor(x,y):
#     print(x,y)
# t.onscreenclick(get_mouse_click_coor)
# t.mainloop()


# data=pandas.read_csv("50_states.csv")
# all_states=data.state.to_list()
# ans_state=screen.textinput(title="guess the state",prompt="enter state name")
# if ans_state in all_states:
#     ug=t.Turtle()
#     ug.hideturtle()
#
#     screen = t.Screen()
#     screen.title("us-states-game")
#     img = "blank_states_img.gif"
#     screen.addshape(img)
#     t.shape(img)
    # def get_mouse_click_coor(x,y):
    #     print(x,y)
    # t.onscreenclick(get_mouse_click_coor)
    # t.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states=[]
while len(guessed_states)<50:
    ans_state = screen.textinput(title=f"{len(guessed_states)}/50 guess the state", prompt="enter state name").title()
    if ans_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state  not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.sv")
        break
    if ans_state in all_states:
       guessed_states.append(ans_state)
       pik = t.Turtle()
       pik.penup()
       pik.hideturtle()
       st = data[data.state == ans_state]
       st=data[data.state==ans_state]
       pik.goto(int(st.x),int(st.y))
       pik.write(st.state.item())


screen.exitonclick()