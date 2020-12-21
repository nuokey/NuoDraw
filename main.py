from tkinter import *

def mouse_pressed(event):
	global mouse, color
	mouse = True
	mouse_y = root.winfo_pointery() - root.winfo_rooty()
	mouse_x = root.winfo_pointerx() - root.winfo_rootx()
	size = int(size_entry.get()) // 2
	c.create_oval(mouse_x - size, mouse_y - size, mouse_x + size, mouse_y + size, fill = color)

def mouse_released(event):
	global mouse
	mouse = False

def mouse_moved(event):
	global mouse, color
	if mouse:
		mouse_y = root.winfo_pointery() - root.winfo_rooty()
		mouse_x = root.winfo_pointerx() - root.winfo_rootx()
		size = int(size_entry.get()) // 2
		c.create_oval(mouse_x - size, mouse_y - size, mouse_x + size, mouse_y + size, fill = color)

def color_change(color_now):
	global color
	color = color_now

root = Tk()
root.geometry('750x750')
root.config(cursor = 'plus')

c = Canvas(root, width = 750, height = 750, bg = 'white')
c.pack()

mouse = False
colors = ['black', 'white', 'red', 'green', 'blue']
color = colors[0]

objects = []
root.bind('<ButtonPress-1>', mouse_pressed)
root.bind('<ButtonRelease-1>', mouse_released)
root.bind('<Motion>', mouse_moved)

size_entry = Entry(root)
size_entry.insert(0, '15')
size_entry.place(x = 0, y = 0, width = 50, height= 30)

color_buttons = []
for i in range(len(colors)):
	color_buttons.append(Button(bg = colors[i], command = lambda: color_change(colors[i])))
	color_buttons[len(color_buttons)-1].place(x = 50 + i * 30, y = 0, width = 30, height = 30)

root.mainloop()