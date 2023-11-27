import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import image_filters

def load_image():
    global img, tk_img, history
    hide_sepia_slider()  # Hide sepia slider when a new image is loaded
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(20, 20, anchor='nw', image=tk_img)
        history = [img.copy()]

def apply_filter(filter_function, *args):
    global img, tk_img, history
    hide_sepia_slider()  # Hide sepia slider when applying any filter
    if img:
        history.append(img.copy())
        img = filter_function(img, *args)
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(20, 20, anchor='nw', image=tk_img)

def show_sepia_slider():
    sepia_intensity_slider.pack()
    apply_sepia_with_intensity()

def hide_sepia_slider():
    sepia_intensity_slider.pack_forget()

def apply_sepia_with_intensity(*args):
    apply_filter(image_filters.apply_sepia, sepia_intensity.get())

def redo():
    global img, tk_img, history
    hide_sepia_slider()  # Hide sepia slider when redoing
    if len(history) > 1:
        history.pop()
        img = history[-1].copy()
        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(20, 20, anchor='nw', image=tk_img)

root = tk.Tk()
root.title("Image Filter App")

img = None
tk_img = None
history = []

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack()

bw_button = tk.Button(root, text="Black and White", command=lambda: apply_filter(image_filters.apply_black_and_white))
bw_button.pack()

sepia_button = tk.Button(root, text="Sepia", command=show_sepia_slider)
sepia_button.pack()

vintage_button = tk.Button(root, text="Vintage", command=lambda: apply_filter(image_filters.apply_vintage))
vintage_button.pack()

redo_button = tk.Button(root, text="Redo", command=redo)
redo_button.pack()

# Sepia intensity slider (initially hidden)
sepia_intensity = tk.DoubleVar(value=1)
sepia_intensity_slider = tk.Scale(root, from_=0, to=1, resolution=0.01, orient='horizontal', label='Sepia Intensity', variable=sepia_intensity, command=apply_sepia_with_intensity)

root.mainloop()
