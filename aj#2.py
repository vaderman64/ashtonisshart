from win10toast import ToastNotifier
import tkinter as tk
import ctypes
import atexit

user32 = ctypes.windll.user32
# toaster = ToastNotifier()
# f = open("demofile.txt", "r")
# toaster.show_toast(f.read(), "hot milfs in your area")
# f.close()

root = tk.Tk()

# Canvas
canvas = tk.Canvas(root, width=user32.GetSystemMetrics(0), height=user32.GetSystemMetrics(1))
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
scoreButton = tk.Button(root, text="CLICK!", height=2, width=10, bg="#445588", fg="white",
                        command=lambda: increasescore())
scoreButton.grid(column=1, row=1)

root.mainloop()


def exit_handler():
    f = open("highscores.txt", "x")
    f.write(score)
    f.close()
    atexit.register(exit_handler)
