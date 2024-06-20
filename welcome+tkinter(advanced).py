from tkinter import *

root = Tk()
c=Canvas(root,height=600,width=600, bg='yellow')
# c.create_line(50,50,350,350)
# c.create_line(350,50,50,350)
# c.create_rectangle(175,175,225,225)
# c.create_oval(175,175,225,225)
# img=PhotoImage(file='sample.png')
# c.create_image(10,200,image = img)
# c.pack()
def print_loc(event):
    print(event.x, event.y)

c.create_rectangle(50, 50, 550, 550, fill="light blue",
tags=('frame'))
c.create_polygon(210, 285, 175, 200, 260, 225, fill='white',
outline='black', tags=('ears'))
c.create_polygon(250, 285, 175, 200, 260, 225, fill='brown',
outline='black', tags=('ears'))
c.create_polygon(344,210,387,255,404,179, fill='brown',
outline='black', tags=('ears'))
c.create_polygon(370,229,387,255,404,179, fill='white',
outline='black', tags=('ears'))
c.create_oval(200, 200, 400, 400, fill="brown", tags=('head'))
c.create_line(300, 350, 325, 370, tags=('mouth'))
c.create_line(279, 366, 301, 349, tags=('mouth'))
c.create_oval(285,348,310,330,fill="lightpink",tags=("nose"))
c.create_oval(245,270,296,327,fill="white",tags=("eyes"))
c.create_oval(270,306,281,323,fill="black",tags=("pupil"))
c.create_oval(310,270,360,327,fill="white",tags=("eyes"))
c.create_oval(340,306,330,323,fill="black",tags=("pupil"))
c.pack() # put it all on the screen!


root.bind("<Button-1>", print_loc)
root.mainloop()