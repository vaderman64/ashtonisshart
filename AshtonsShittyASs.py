import tkinter as tk

root = tk.Tk()

# Canvas
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Text
nameText = tk.Label(root, text="Button Clicker")
nameText.grid(columnspan=3, column=0, row=3)

# Score Functions
score = 0
scoreStr = tk.StringVar()
scoreStr.set(str(score))


def increasescore():
    global score
    global scoreStr
    score += 1
    scoreStr.set(str(score))

    # Score Label
    scoreLabel = tk.Label(root, text=scoreStr.get())
    scoreLabel.grid(columnspan=2, column=0, row=0)


# Button
scoreButton = tk.Button(root, text="CLICK!", height=2, width=10, bg="#445588", fg="white", command=lambda: increasescore())
scoreButton.grid(column=1, row=1)



root.mainloop()
