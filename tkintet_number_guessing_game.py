import tkinter as tk
import random
import math

def start_game():
    global x, min_guesses, c
    try:
        a = int(entry_lower.get())
        b = int(entry_upper.get())
        x = random.randint(a, b)
        min_guesses = round(math.log(b - a + 1, 2))
        c = 0
        label_feedback.config(text=f"You have {min_guesses} chances to guess the number!")
        button_guess.config(state="normal")
    except ValueError:
        label_feedback.config(text="Please enter valid numbers!")
   

def check_guess():
    global c
    try:
        guess = int(entry_guess.get())

        entry_guess.delete(0,tk.END)
        c += 1
        if guess == x:
            label_feedback.config(text=f"Congrats! You found the number {x} in {c} tries!")
            button_guess.config(state="disabled")
        elif guess < x:
            label_feedback.config(text="The guess is too low!")
        else:
            label_feedback.config(text="The guess is too high!")

        if c >= min_guesses and guess != x:
            label_feedback.config(text=f"Out of chances! The number was {x}. Try again?")
            button_guess.config(state="disabled")

    except ValueError:
        label_feedback.config(text="Please enter a valid number!")

# Set up the Tkinter window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x350")
root.config(background="#369AD9")

# Widgets for lower and upper bounds
tk.Label(root, text="Lower Bound:",bg="#369AD9",fg="black").pack()
entry_lower = tk.Entry(root)
entry_lower.pack(pady=5)

tk.Label(root, text="Upper Bound:",bg="#369AD9",fg="black").pack()
entry_upper = tk.Entry(root)
entry_upper.pack(pady=5)

button_start = tk.Button(root, text="Start Game", command=start_game,bg="#A7E4F2",fg="black")
button_start.pack(pady=15)

# Widgets for guessing
tk.Label(root, text="Enter your guess:",bg="#369AD9",fg="black").pack()
entry_guess = tk.Entry(root)
entry_guess.pack(pady=10)

button_guess = tk.Button(root, text="Guess", command=check_guess, state="disabled",bg="#A7E4F2",fg="black")
button_guess.pack(pady=10)

# Label for feedback
label_feedback = tk.Label(root,bg="#369AD9",fg="black")
label_feedback.pack()

# Run the Tkinter main loop
root.mainloop()
