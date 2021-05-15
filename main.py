import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state:
        (answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # t.write(state_data.state.item())







    #if right:
    #create a turtle to write the name of the state at X Y coordinate



# answer_l = answer_state.lower()
# state_check = data["state"]
# state_list = state_check.to_list()
# low_state = [item.lower() for item in state_list]

# print(state_list)
# # state_set = set(state_list)
# def check_answer():
#     if(answer_state.lower() in low_state):
#         print("fuck Yeah")
#         # print(data.state == answer_state)
#
#         return answer_state.capitalize()
#         # print(data.state == answer_state)
#     else:
#         print("Fuck")
#
# fucker = answer_state.capitalize()
# print(fucker)
#
# def check_in_data():
#         if data.state != fucker:
#             return
#         print("yahoo")
#
#
# check_answer()
# check_in_data()


# for i in state_list:
#     if(i == "California") :
#         print("Element Exists")

# if answer_l in state_list:
#      print("WTF")
# else:
#     print("Shieeet")




