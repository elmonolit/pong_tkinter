from tkinter import *
from random import choice

ball_radius = 10

root = Tk()

c = Canvas(root, height=900, width=300, bg='green')
c.focus_set()

c.create_line(0, 450, 300, 450, fill='white')
ball = c.create_oval(150 - ball_radius, 450 - ball_radius, 150 + ball_radius, 450 + ball_radius, fill='white')
c.pack()
pad1 = c.create_rectangle(150 - 50, 900 - 10, 150 + 50, 900, fill='white')
pad2 = c.create_rectangle(150 - 50, 10, 150 + 50, 0, fill='white')

randlist = [-1, 1]
dx = choice(randlist)
dy = choice(randlist)
pad1_count = 0
pad2_count = 0
speed = 2
root.title(f'{pad1_count}:{pad2_count}')


def motion():
    global dx
    global dy
    global pad1_count
    global pad2_count
    global speed
    c.move(ball, speed * dx, speed * dy)

    if c.coords(ball)[2] >= 300:
        dx = dx * -1

    elif c.coords(ball)[2] <= 20:
        dx = dx * -1
    elif c.coords(pad1)[0] <= c.coords(ball)[2] <= c.coords(pad1)[2] and c.coords(ball)[3] >= c.coords(pad1)[1]:
        dy = dy * -1
        speed += 1
    elif c.coords(pad2)[0] <= c.coords(ball)[2] <= c.coords(pad2)[2] and c.coords(ball)[1] <= c.coords(pad2)[3]:
        dy = dy * -1
        speed += 1
    elif c.coords(ball)[3] <= 20:
        pad1_count += 1
        root.title(f'{pad1_count}:{pad2_count}')
        c.coords(ball, 140, 440, 160, 460)
        dx = choice(randlist)
        dy = choice(randlist)
        speed = 2
    elif c.coords(ball)[3] >= 900:
        pad2_count += 1
        root.title(f'{pad1_count}:{pad2_count}')
        c.coords(ball, 140, 440, 160, 460)
        dx = choice(randlist)
        dy = choice(randlist)
        speed = 2

    root.after(10, motion)


motion()
c.bind('<a>', lambda event: c.move(pad2, -4, 0))
c.bind('<d>', lambda event: c.move(pad2, 4, 0))
c.bind('<Left>', lambda event: c.move(pad1, -4, 0))
c.bind('<Right>', lambda event: c.move(pad1, 4, 0))

root.mainloop()
