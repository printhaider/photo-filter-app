import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import image_filters  # This is the file with your filter functions

def load_image():
    global img, tk_img, history
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(20, 20, anchor='nw', image=tk_img)
        history = [img.copy()]

def apply_filter(filter_function):
    global img, tk_img, history
    if img:
        history.append(img.copy())  # Save current state before applying the filter
        img = filter_function(img)
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(20, 20, anchor='nw', image=tk_img)

def redo():
    global img, tk_img, history
    if len(history) > 1:  # Check if there is a state to revert to
        history.pop()  # Remove the current state
        img = history[-1]  # Revert to the previous state
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(20, 20, anchor='nw', image=tk_img)

root = tk.Tk()
root.title("Image Filter App")

img = None
tk_img = None
history = []  # Initialize history

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack()

sepia_button = tk.Button(root, text="Apply Sepia", command=lambda: apply_filter(image_filters.apply_sepia))
sepia_button.pack()

vintage_button = tk.Button(root, text="Apply Vintage", command=lambda: apply_filter(image_filters.apply_vintage))
vintage_button.pack()

redo_button = tk.Button(root, text="Redo", command=redo)
redo_button.pack()

root.mainloop()
