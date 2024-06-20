#FruitNinja
from tkinter import *
from random import randrange, choice
root = Tk()
c = Canvas(root, height=600, width=600, bg='white')
c.pack()


class Fruit():
    def __init__(self, x, y, Fruit_image):
        self.obj = c.create_image(x, y, image=Fruit_image)
        c.tag_bind(self.obj, '<ButtonPress-1>', self.destroy)
        self.move()

    def destroy(self, event):
        c.delete(self.obj)

    def move(self):
        c.move(self.obj, 0, 2)
        root.after(50, self.move)


class Banana(Fruit):
    img = PhotoImage(file='bananas.png')

    def __init__(self, x, y):
        super().__init__(x, y, Banana.img)


class Watermelon(Fruit):
    img = PhotoImage(file='watermelon.png')

    def __init__(self, x, y):
        super().__init__(x, y, Watermelon.img)


class Coconut(Fruit):
    img = PhotoImage(file='coconut.png')

    def __init__(self, x, y):
        super().__init__(x, y, Coconut.img)


class Bomb():
    img = PhotoImage(file='bomb.png')
    
    def __init__(self, x, y):
        self.obj = c.create_image(x, y, image=Bomb.img)
        c.tag_bind(self.obj, '<ButtonPress-1>', self.destroy)
        self.move()

    def destroy(self, event):
        print('You hit a bomb!')
        root.destroy()

    def move(self):
        c.move(self.obj, 0, 2)
        root.after(50, self.move)


fruits = ['bomb', 'coconut', 'watermelon', 'banana']


def new_fruit():
    for i in range(3):
        fruit = choice(fruits)
        if fruit == 'bomb':
            Bomb(randrange(0, 400), randrange(0, 200))
        elif fruit == 'watermelon':
            Watermelon(randrange(0, 400), randrange(0, 200))
        elif fruit == 'banana':
            Banana(randrange(0, 400), randrange(0, 200))
        else:
            Coconut(randrange(0, 400), randrange(0, 200))

    root.after(2000, new_fruit)


new_fruit()


root.mainloop()
