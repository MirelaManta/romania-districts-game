import turtle
import pandas

screen = turtle.Screen()
screen.title("Regions of Romania Game")
image = "mute_map_romania.gif"
screen.addshape(image)

turtle.shape(image)

# where the x, y coordinates came from
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("42_regions.csv")
all_regions = data.region.to_list()
guessed_regions = []

# don't use diacritics
while len(guessed_regions) < 42:
    answer_region = screen.textinput(title=f"{len(guessed_regions)}/42 Regions Guessed",
                                     prompt="What's another region's name?").title()
    if answer_region == "Exit":
        missing_regions = [region for region in all_regions if region not in guessed_regions]
        new_data = pandas.DataFrame(missing_regions)
        new_data.to_csv("regions_to_learn.csv")
        break
    if answer_region in all_regions:
        guessed_regions.append(answer_region)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        region_data = data[data.region == answer_region]
        t.color("black")
        t.goto(int(region_data.x), int(region_data.y))
        t.write(answer_region, align="center", font=("Arial", 8, "bold"))
# turtle.mainloop()
