from tkinter import *

def mouse_done():
	global color, regym, canv
	mouse_y = root.winfo_pointery() - root.winfo_rooty()
	mouse_x = root.winfo_pointerx() - root.winfo_rootx()
	size = int(size_entry.get()) // 2
	if regym == 'draw':
		canv.append([c.create_oval(mouse_x - size, mouse_y - size, mouse_x + size, mouse_y + size, fill = color, width = 0), [mouse_x, mouse_y], size])
	elif regym == 'lastic':
		i = 0
		while i <= len(canv) - 1:
			if abs(canv[i][1][0] - mouse_x) <= canv[i][2] + size and abs(canv[i][1][1] - mouse_y) <= canv[i][2] + size:
				c.delete(canv[i][0])
				del canv[i]
				i += 1
			i += 1

def mouse_pressed(event):
	global mouse, color
	mouse = True
	mouse_done()

def mouse_released(event):
	global mouse
	mouse = False

def mouse_moved(event):
	global mouse
	if mouse:
		mouse_done()
	c['width'] = root.winfo_width()
	c['height'] = root.winfo_height()

def color_change_0():
	global color, colors
	color = colors[0]

def color_change_1():
	global color, colors
	color = colors[1]

def color_change_2():
	global color, colors
	color = colors[2]

def color_change_3():
	global color, colors
	color = colors[3]

def color_change_4():
	global color, colors
	color = colors[4]

def change_draw():
	global regym
	regym = 'draw'

def change_lastic():
	global regym
	regym = 'lastic'

root = Tk()
root.geometry('750x750')
root.config(cursor = 'plus')
root['bg'] = 'white'

c = Canvas(root, width = 750, height = 750, bg = 'white')
c.pack()
canv = []

mouse = False
colors = ['black', 'white', 'red', 'green', 'blue']
color = colors[0]
regym = 'draw'

objects = []
root.bind('<ButtonPress-1>', mouse_pressed)
root.bind('<ButtonRelease-1>', mouse_released)
root.bind('<Motion>', mouse_moved)

up_bar = Label(root, bg = 'grey')
side_bar = Label(root, bg = 'grey')
up_bar.place(x = 0, y = 0, width = 750, height = 40)
side_bar.place(x = 0, y = 0, width = 40, height = 750)

size_entry = Entry(root)
size_entry.insert(0, '15')
size_entry.place(x = 0, y = 5, width = 50, height= 30)

color_buttons = []
for i in range(len(colors)):
	exec(f'color_buttons.append(Button(bg = colors[i], command = color_change_{i}))')
	color_buttons[len(color_buttons)-1].place(x = 50 + i * 30, y = 5, width = 30, height = 30)

draw_button = Button(root, text = 'D', bg = 'black', fg = 'white', command = change_draw)
draw_button.place(x = 5, y = 45, width = 30, height = 30)

lastic_button = Button(root, text = 'L', bg = 'black', fg = 'white', command = change_lastic)
lastic_button.place(x = 5, y = 80, width = 30, height = 30)

root.mainloop()