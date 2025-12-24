from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint

IMAGE_SIZE = (200, 200) 

window = Tk()
window.title("Game - Rock Paper Scissors")
window.configure(background="black")

# Configure ttk styles for rounded buttons
style = ttk.Style()

# Configure rounded button style
style.configure('Rounded.TButton', 
                font=('arial', 18, 'bold'),
                padding=10,
                relief='flat',
                borderwidth=0,
                focusthickness=0,
                focuscolor='none')

style.configure('Control.TButton',
                font=('arial', 14, 'bold'),
                padding=8,
                relief='flat',
                borderwidth=0,
                focusthickness=0,
                focuscolor='none')

# Configure label styles
style.configure('Score.TLabel',
                font=('arial', 60, 'bold'),
                background='orange',
                foreground='red',
                anchor='center')

style.configure('Indicator.TLabel',
                font=('arial', 40, 'bold'),
                background='orange',
                foreground='red',
                anchor='center')

style.configure('Message.TLabel',
                font=('arial', 30, 'bold'),
                background='red',
                foreground='white',
                anchor='center',
                padding=20)

style.configure('Instruction.TLabel',
                font=('arial', 14, 'bold'),
                background='black',
                foreground='white',
                anchor='center')


try:
    image_rock1 = ImageTk.PhotoImage(Image.open("D:/Learning/Python/Python/Projects/game/right_rock.png").resize(IMAGE_SIZE))
    image_paper1 = ImageTk.PhotoImage(Image.open("D:/Learning/Python/Python/Projects/game/img-3.png").resize(IMAGE_SIZE))
    image_scissors1 = ImageTk.PhotoImage(Image.open("D:/Learning/Python/Python/Projects/game/right_scissors.png").resize(IMAGE_SIZE))
    image_rock2 = ImageTk.PhotoImage(Image.open("D:/Learning/Python/Python/Projects/game/left_rock.png").resize(IMAGE_SIZE))
    image_paper2 = ImageTk.PhotoImage(Image.open("D:/Learning/Python/Python/Projects/game/left_paper.png").resize(IMAGE_SIZE))
    image_scissors2 = ImageTk.PhotoImage(Image.open("D:/Learning/Python/Python/Projects/game/left_scissors.png").resize(IMAGE_SIZE))
    
except Exception as e:
    print(f"Error loading images: {e}")
    from tkinter import messagebox
    messagebox.showwarning("Image Error", "Some image files not found. Using placeholders.")
    placeholder = Image.new('RGB', IMAGE_SIZE, color='gray')
    image_rock1 = image_paper1 = image_scissors1 = image_rock2 = image_paper2 = image_scissors2 = ImageTk.PhotoImage(placeholder)


def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1+radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Function to create rounded button
class RoundedButton(Canvas):
    def __init__(self, parent, width, height, corner_radius, color, text, text_color, command=None):
        Canvas.__init__(self, parent, width=width, height=height, highlightthickness=0)
        self.command = command
        
        # Draw rounded rectangle
        self.rect = create_rounded_rectangle(self, 0, 0, width, height, corner_radius, 
                                             fill=color, outline=color)
        
        # Add text
        self.text = self.create_text(width/2, height/2, text=text, fill=text_color, 
                                     font=('arial', 18, 'bold'))
        
        # Bind events
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        
        if command:
            self.bind("<ButtonRelease-1>", lambda e: command())
    
    def _on_press(self, event):
        self.itemconfig(self.rect, fill=self.darken_color(self.itemcget(self.rect, "fill")))
    
    def _on_release(self, event):
        self.itemconfig(self.rect, fill=self.lighten_color(self.itemcget(self.rect, "fill")))
    
    def darken_color(self, color):
        # Simple color darkening
        return color
    
    def lighten_color(self, color):
        # Simple color lightening
        return color

# Create labels for images
label_player = Label(window, image=image_rock1, bg="black")
label_computer = Label(window, image=image_rock2, bg="black")
label_computer.grid(row=1, column=0, padx=20, pady=10)
label_player.grid(row=1, column=4, padx=20, pady=10)

# Score labels with fixed size
score_width = 150
score_height = 100
computer_score_canvas = Canvas(window, width=score_width, height=score_height, bg="orange", highlightthickness=0)
computer_score_canvas.grid(row=1, column=1, padx=20, pady=10)
create_rounded_rectangle(computer_score_canvas, 0, 0, score_width, score_height, 25, fill="orange")
computer_score = Label(computer_score_canvas, text="0", font=("arial", 60, "bold"), bg="orange", fg="red")
computer_score.place(relx=0.5, rely=0.5, anchor="center")

player_score_canvas = Canvas(window, width=score_width, height=score_height, bg="orange", highlightthickness=0)
player_score_canvas.grid(row=1, column=3, padx=20, pady=10)
create_rounded_rectangle(player_score_canvas, 0, 0, score_width, score_height, 25, fill="orange")
player_score = Label(player_score_canvas, text="0", font=("arial", 60, "bold"), bg="orange", fg="red")
player_score.place(relx=0.5, rely=0.5, anchor="center")

# Player indicators with fixed size
indicator_width = 240
indicator_height = 60
computer_indicator_canvas = Canvas(window, width=indicator_width, height=indicator_height, bg="orange", highlightthickness=0)
computer_indicator_canvas.grid(row=0, column=1, padx=20, pady=10)
create_rounded_rectangle(computer_indicator_canvas, 0, 0, indicator_width, indicator_height, 20, fill="orange")
computer_indicator = Label(computer_indicator_canvas, text="COMPUTER", font=("arial", 30, "bold"), bg="orange", fg="red")
computer_indicator.place(relx=0.5, rely=0.5, anchor="center")

player_indicator_canvas = Canvas(window, width=indicator_width, height=indicator_height, bg="orange", highlightthickness=0)
player_indicator_canvas.grid(row=0, column=3, padx=20, pady=10)
create_rounded_rectangle(player_indicator_canvas, 0, 0, indicator_width, indicator_height, 20, fill="orange")
player_indicator = Label(player_indicator_canvas, text="PLAYER", font=("arial", 30, "bold"), bg="orange", fg="red")
player_indicator.place(relx=0.5, rely=0.5, anchor="center")

def updateMessage(a):
    final_message['text'] = a
    
def computer_update():
    final = int(computer_score['text'])
    final += 1
    computer_score["text"] = str(final)

def player_update():
    final = int(player_score['text'])
    final += 1
    player_score["text"] = str(final)

def winner_check(p, c):
    if p == c:
        updateMessage("It's a tie!")
        return
    
    if p == "rock":
        if c == "scissors":
            updateMessage("Player wins!!")
            player_update()
        else:
            updateMessage("Computer wins!!")
            computer_update()
    
    elif p == "paper":
        if c == "rock":
            updateMessage("Player wins!!")
            player_update()
        else:
            updateMessage("Computer wins!!")
            computer_update()
    
    elif p == "scissors":
        if c == "paper":
            updateMessage("Player wins!!")
            player_update()
        else:
            updateMessage("Computer wins!!")
            computer_update()

to_select = ["rock", "paper", "scissors"]    

def choice_update(a):
    choice_computer = to_select[randint(0, 2)]
    
    if choice_computer == "rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissors2)
    
    if a == "rock":
        label_player.configure(image=image_rock1)
    elif a == "paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissors1)
    
    winner_check(a, choice_computer)

# Result message with fixed size and rounded corners
message_width = 500
message_height = 80
message_canvas = Canvas(window, width=message_width, height=message_height, bg="red", highlightthickness=0)
message_canvas.grid(row=3, column=1, pady=20, padx=10, columnspan=3)
create_rounded_rectangle(message_canvas, 0, 0, message_width, message_height, 20, fill="red")
final_message = Label(message_canvas, text="", font=("arial", 25, "bold"), bg="red", fg="white", wraplength=450)
final_message.place(relx=0.5, rely=0.5, anchor="center")

# Create game buttons with rounded corners
def create_game_button(parent, text, command, color="yellow"):
    # Create canvas for rounded button
    btn_canvas = Canvas(parent, width=180, height=70, bg="black", highlightthickness=0)
    
    # Draw rounded rectangle
    create_rounded_rectangle(btn_canvas, 5, 5, 175, 65, 15, fill=color, outline=color)
    
    # Add text
    btn_canvas.create_text(90, 35, text=text, fill="red", font=('arial', 18, 'bold'))
    
    # Bind click event
    btn_canvas.bind("<Button-1>", lambda e: command())
    
    # Add hover effects
    def on_enter(e):
        btn_canvas.itemconfig(1, fill="#FFD700")  # Lighten color
    
    def on_leave(e):
        btn_canvas.itemconfig(1, fill=color)  # Restore color
    
    btn_canvas.bind("<Enter>", on_enter)
    btn_canvas.bind("<Leave>", on_leave)
    
    return btn_canvas

# Create and place game buttons
button_rock = create_game_button(window, "ROCK", lambda: choice_update("rock"), "yellow")
button_paper = create_game_button(window, "PAPER", lambda: choice_update("paper"), "yellow")
button_scissors = create_game_button(window, "SCISSORS", lambda: choice_update("scissors"), "yellow")

button_rock.grid(row=2, column=1, padx=10, pady=10)
button_paper.grid(row=2, column=2, padx=10, pady=10)
button_scissors.grid(row=2, column=3, padx=10, pady=10)

# Create control buttons
def create_control_button(parent, text, command, color, text_color):
    btn_canvas = Canvas(parent, width=150, height=60, bg="black", highlightthickness=0)
    
    create_rounded_rectangle(btn_canvas, 5, 5, 145, 55, 10, fill=color, outline=color)
    btn_canvas.create_text(75, 30, text=text, fill=text_color, font=('arial', 14, 'bold'))
    btn_canvas.bind("<Button-1>", lambda e: command())
    
    return btn_canvas

def reset_game():
    computer_score["text"] = "0"
    player_score["text"] = "0"
    final_message["text"] = "Game Reset!"
    label_player.configure(image=image_rock1)
    label_computer.configure(image=image_rock2)

def exit_game():
    from tkinter import messagebox
    if messagebox.askyesno("Exit Game", "Are you sure you want to exit the game?"):
        window.destroy()

# Create and place control buttons
button_reset = create_control_button(window, "RESET", reset_game, "lightblue", "darkblue")
button_exit = create_control_button(window, "EXIT", exit_game, "lightcoral", "darkred")

button_reset.grid(row=4, column=1, padx=5, pady=10)
button_exit.grid(row=4, column=3, padx=5, pady=10)

# Configure grid
for i in range(5):
    window.grid_columnconfigure(i, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)

window.resizable(True, True)

# Instruction label
instruction_canvas = Canvas(window, width=600, height=40, bg="black", highlightthickness=0)
instruction_canvas.grid(row=5, column=0, columnspan=5, pady=10)
create_rounded_rectangle(instruction_canvas, 0, 0, 600, 40, 10, fill="#222222", outline="#222222")
instruction = Label(instruction_canvas, text="Choose Rock, Paper, or Scissors to play!", 
                    font=("arial", 14, "bold"), bg="#222222", fg="white")
instruction.place(relx=0.5, rely=0.5, anchor="center")




window.mainloop()