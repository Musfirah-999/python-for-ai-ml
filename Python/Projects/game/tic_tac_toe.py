import tkinter as tk
from tkinter import messagebox

combos = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def check_winner():
    global winner, game_over
    # Check for winner
    for combo in combos:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")    
            buttons[combo[1]].config(bg="green")    
            buttons[combo[2]].config(bg="green")  
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")  
            winner = True
            game_over = True
            disable_buttons()
            return True
    
    # Check for tie (all buttons filled, no winner)
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        game_over = True
        disable_buttons()
        return True
    
    return False

def disable_buttons():
    """Disable all buttons when game ends"""
    for button in buttons:
        button.config(state="disabled")

def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not game_over:
        buttons[index]["text"] = current_player 
        if not check_winner():
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

def restart_game():
    """Restart the game"""
    global current_player, winner, game_over
    current_player = "X"
    winner = False
    game_over = False
    
    # Reset all buttons
    for button in buttons:
        button.config(text="", bg="SystemButtonFace", state="normal")
    
    label.config(text=f"Player {current_player}'s turn")

def center_grid():
    """Center the grid when window is resized"""
    # Configure grid weights to make it expandable
    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)
    
    # Center the buttons frame
    game_frame.grid(row=1, column=1, sticky="nsew")
    
    # Center the label
    label.grid(row=2, column=1, sticky="nsew", pady=10)
    
    # Center the restart button
    restart_button.grid(row=3, column=1, sticky="nsew", pady=10)

def on_resize(event):
    """Handle window resize events"""
    # Update the layout when window is resized
    center_grid()

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x500")  # Set initial size

# Make the root window responsive
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

# Create a frame to hold the game buttons
game_frame = tk.Frame(root)
game_frame.grid(row=1, column=1)

# Create buttons inside the frame
buttons = []
for i in range(9):
    button = tk.Button(game_frame, text="", font=("normal", 25), width=6, height=2,
                       command=lambda i=i: button_click(i))
    buttons.append(button)
    button.grid(row=i//3, column=i%3, padx=5, pady=5)

# Configure the game_frame grid to be centered
for i in range(3):
    game_frame.grid_rowconfigure(i, weight=1)
    game_frame.grid_columnconfigure(i, weight=1)

current_player = "X"
winner = False
game_over = False

# Create label
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16), anchor="center")
label.grid(row=2, column=1)

# Create restart button
restart_button = tk.Button(root, text="Restart Game", font=("normal", 12), 
                           command=restart_game)
restart_button.grid(row=3, column=1)

# Bind resize event
root.bind('<Configure>', on_resize)

# Initial centering
center_grid()

root.mainloop()