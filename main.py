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
		objects.append(Label(bg = 'red'))
		objects[len(objects)-1].place(x = mouse_x - 10, y = mouse_y - 10, width = 20, height = 20)

root = Tk()
root.config(cursor = 'plus')

mouse = False

objects = []
root.bind('<ButtonPress-1>', mouse_pressed)
root.bind('<ButtonRelease-1>', mouse_released)
root.bind('<Motion>', mouse_moved)

root.mainloop()