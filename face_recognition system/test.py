from tkinter import *

def on_button_click():
    print("Button clicked")

root = Tk()
root.geometry("200x100")

# Create a canvas
canvas = Canvas(root, width=200, height=100)
canvas.pack()

# Draw a rounded rectangle on the canvas
rounded_rectangle = canvas.create_rounded_rectangle(10, 10, 190, 90, 10, fill="blue", outline="black")

# Create a button with transparent background
button = Button(canvas, text="Click Me", command=on_button_click, bd=0, highlightthickness=0)

# Place the button on the canvas at the center of the rounded rectangle
button_window = canvas.create_window(100, 50, window=button, width=180, height=80)

root.mainloop()
