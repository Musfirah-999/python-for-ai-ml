
from tkinter import *
from PIL import Image, ImageTk
from random import randint
IMAGE_SIZE = (200, 200) 

window = Tk()
window.title("Game---- Rock paper scissors")
window.configure(background="black")


image_rock1 = ImageTk.PhotoImage(Image.open("d:\\Learning\\python-for-ai-ml\\python-for-ai-ml\\Projects\\game\\right_rock.png").resize(IMAGE_SIZE))
image_peper1 = ImageTk.PhotoImage(Image.open("d:\\Learning\\python-for-ai-ml\\python-for-ai-ml\\Projects\\game\\img-3.png").resize(IMAGE_SIZE))
image_scissors1 = ImageTk.PhotoImage(Image.open("d:\\Learning\\python-for-ai-ml\\python-for-ai-ml\\Projects\\game\\right_scissors.png").resize(IMAGE_SIZE))
image_rock2 = ImageTk.PhotoImage(Image.open("d:\\Learning\\python-for-ai-ml\\python-for-ai-ml\\Projects\\game\\left_rock.png").resize(IMAGE_SIZE))
image_paper2 = ImageTk.PhotoImage(Image.open("d:\\Learning\\python-for-ai-ml\\python-for-ai-ml\\Projects\\game\\left_paper.png").resize(IMAGE_SIZE))
image_scissors2 = ImageTk.PhotoImage(Image.open("d:\\Learning\\python-for-ai-ml\\python-for-ai-ml\\Projects\\game\\left_paper.png").resize(IMAGE_SIZE))



label_player = Label(window, image=image_scissors1)
label_computer = Label(window, image=image_scissors2)
label_computer.grid(row=1, column=0)
label_player.grid(row=1,column=4)


computer_score = Label(window, text=0, font=("arial", 60, "bold"), bg="orange", fg= "red")
player_score = Label(window, text=0, font=("arial", 60, "bold"),  bg="orange", fg= "red")
computer_score.grid(row = 1, column=0)
player_score.grid(row = 1, column=3)



button_rock = Button(window, width=16, height=3, text="Rock", font = ("arial", 20, "bold"), bg="yellow", fg= "red").grid(row=2, column=1)
button_paper = Button(window, width=16, height=3, text="Paper", font = ("arial", 20, "bold"), bg="yellow", fg= "red").grid(row=2, column=2)
button_scissors = Button(window, width=16, height=3, text="Scissors", font = ("arial", 20, "bold"), bg="yellow", fg= "red").grid(row=2, column=3)


window.mainloop()
