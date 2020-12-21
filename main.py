from tkinter import *

def mouse_pressed(event):
	global mouse
	mouse = True

def mouse_released(event):
	global mouse
	mouse = False

def mouse_moved(event):
	global mouse
	if mouse:
		mouse_y = root.winfo_pointery() - root.winfo_rooty()
		mouse_x = root.winfo_pointerx() - root.winfo_rootx()
		c.create_oval(mouse_x - 10, mouse_y - 10, mouse_x + 10, mouse_y + 10, fill = 'black')

root = Tk()
root.geometry('750x750')
root.config(cursor = 'plus')

c = Canvas(root, width = 750, height = 750, bg = 'white')
c.pack()

mouse = False

objects = []
root.bind('<ButtonPress-1>', mouse_pressed)
root.bind('<ButtonRelease-1>', mouse_released)
root.bind('<Motion>', mouse_moved)

root.mainloop()