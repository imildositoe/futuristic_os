import socket
import tkinter

top = tkinter.Tk()
top.title("Network Checker")
top.configure(background="#006666")

l = tkinter.Label(top, text='Checking ...')
l.pack()


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        state = "Online"
    except OSError:
        state = "Offline"
    l.config(text=state)
    print(state)
    top.after(1000, is_connected)
