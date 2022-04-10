# coding: cp1252
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1920x1080")
window.configure(bg="#010001")

canvas = Canvas(
    window,
    bg="#010001",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0003662109375,
    30.5,
    1920.0125732421875,
    31.81439208984375,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    651.0003662109375,
    1054.0,
    1251.0001831054688,
    1054.4107666015625,
    fill="#000000",
    outline="")

canvas.create_text(
    8.0,
    8.0,
    anchor="nw",
    text="FUTURISTIC OS",
    fill="#54828B",
    font=("ZenDots Regular", 12 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1896.0,
    19.0,
    image=image_image_1
)

canvas.create_text(
    255.0,
    36.0,
    anchor="nw",
    text="Uptime: 0h 17m 34s",
    fill="#54828B",
    font=("Consolas Bold", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: messagebox.showinfo("Button", "Button Clicked"),
    relief="flat"
)
button_1.place(
    x=729.0,
    y=1059.0,
    width=33.0,
    height=14.0
)

canvas.create_text(
    783.0,
    1059.0,
    anchor="nw",
    text="File Explorer",
    fill="#54828B",
    font=("Consolas Bold", 12 * -1)
)

canvas.create_text(
    889.0,
    1059.0,
    anchor="nw",
    text="Terminal",
    fill="#54828B",
    font=("Consolas Bold", 12 * -1)
)

canvas.create_text(
    960.0,
    1059.0,
    anchor="nw",
    text="Virtual Keyboard",
    fill="#54828B",
    font=("Consolas Bold", 12 * -1)
)

canvas.create_text(
    1083.0,
    1059.0,
    anchor="nw",
    text="System Monitor",
    fill="#54828B",
    font=("Consolas Bold", 12 * -1)
)

canvas.create_text(
    383.0,
    36.0,
    anchor="nw",
    text="Forecast: 22�C 18�C",
    fill="#54828B",
    font=("Consolas Bold", 12 * -1)
)

canvas.create_text(
    520.0,
    36.0,
    anchor="nw",
    text="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et "
         "dolore magna aliqua. Ut enim Processes: 33 DownSpeed: 7Kb/s Upspeed: 3Kb/s",
    fill="#54828B",
    font=("Consolas Bold", 12 * -1)
)
window.resizable(True, True)
window.mainloop()