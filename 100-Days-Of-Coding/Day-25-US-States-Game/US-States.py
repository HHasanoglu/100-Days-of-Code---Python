import stat
import turtle
import pandas

screen=turtle.Screen()
screen.title("US-States")
img="Day-25-US-States-Game/blank_states_img.GIF"
dataURL="Day-25-US-States-Game/50_states.csv"
screen.addshape(img)
turtle.shape(img)


data=pandas.read_csv(dataURL)
states=data.state.tolist()
GuessedStates=[]
while len(GuessedStates)<len(states):
    state=screen.textinput(f"{len(GuessedStates)}/{len(states)}","Please Write a city name").title()
    if state=="Exit":
        break 
    if state in states:
        GuessedStates.append(state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        row=data[data["state"]==state]
        t.goto(int(row.x),int(row.y))
        t.write(row.state.item())

remainedstates=[]
for state in states:
    if state not in GuessedStates:
        remainedstates.append(state)

rdata=pandas.DataFrame(remainedstates)
rdata.to_csv("statestoLearn.csv")
screen.mainloop()




