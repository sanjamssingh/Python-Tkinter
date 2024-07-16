from tkinter import*
root= Tk()
# num = IntVar()
# def add():
#     num.set(num.get() + 1)
# desc_label = Label(root, text = 'How many clicks: ', bg = 'blue',
# fg = 'white')
# num_label = Label(root, textvariable=num, bg = 'blue', fg = 'white')
# clicker = Button(root, text = 'CLICK ME', bg = 'blue', fg = 'white',
# command = add) 
# desc_label.pack(side = TOP, fill = X)
# num_label.pack(side = TOP, fill = X)
# clicker.pack(side = BOTTOM, fill = X)
# posvar = StringVar()
# def update_pos(event):
#     posvar.set('(%d, %d)'%(round(event.x), round(event.y)))
# loc_label = Label(root, textvariable=posvar, bg = 'grey',
# justify = 'center')
# loc_label.pack(fill = X)
# f = Frame(root, width = 400, height = 400, bg = 'white')
# f.pack(side = BOTTOM)
# f.bind('<Motion>', update_pos)
from random import choice
c = Canvas(root, width = 400, height = 400, bg = 'white')
c.pack(side = BOTTOM)
# def change_color(event): 
#     event.widget.itemconfigure(circle, fill = choice(['blue','orange',
# 'yellow', 'green','black','purple','red','white','lightblue','grey']))
# circle = c.create_oval(180, 180, 220, 220, fill ='red')
# c.tag_bind(circle, '<ButtonPress>', change_color)
# def change_color(event):
#     event.widget.itemconfigure('dot',fill = choice(['blue', 'orange',
# 'yellow', 'green']))
# d1 = c.create_oval(180, 180, 220, 220, fill ='red', tags = ('dot'))
# d2 = c.create_oval(0, 0, 40, 40, fill ='red', tags = ('dot'))
# d3 = c.create_oval(360, 360, 400, 400, fill ='red', tags = ('dot'))
# c.tag_bind('dot', '<ButtonPress>', change_color)
root.mainloop()
# widget.unbind('<Event>', function_name)
# root.bind('<Motion>', function_name)