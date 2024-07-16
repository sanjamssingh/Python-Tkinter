from tkinter import*
root = Tk()

listvar= StringVar(value= ('Python', 'Java', 'Javascript', 'C++','apple','banana','mango','pineapple','watermelon','grapes'))
listbox= Listbox(root, listvariable= listvar, height= 3, selectmode= 'extended')
scroller= Scrollbar(root, orient= VERTICAL)
scroller.config(command=listbox.yview)
scroller.pack(side= RIGHT, fill= Y)
listbox.pack()
listbox.curselection()

# scroller= Scrollbar(root, orient= VERTICAL)
# listvar= StringVar(value= (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
# listbox= Listbox(root, listvariable= listvar, height= 10, yscrollcommand= scroller.set)
# scroller.config(command= listbox.yview)
# scroller.grid(row= 0, column=1, rowspan=2)
# listbox.grid(row= 0, column=0)
# scroller.pack(side= RIGHT, fill= Y)
# listbox.pack(side= LEFT)

# textbox= Text(root, width= 50, height= 20, background= "grey")
# textbox.insert('1.0','here is my default text.\n')
# wordsonline1= textbox.get('1.0', 'end')
# print(wordsonline1)
# textbox.grid(row=1)

# var= IntVar()
# scalebar= Scale(root, variable= var, bg= "black", fg= "white", tickinterval= 10, 
#                 resolution= 10, orient= HORIZONTAL, from_= 50, to= 80)
# scalebar.grid(row=2,sticky="news")
# currentvalue= scalebar.get()

root.title("Painting!")
root.geometry('300x200')
root.resizable(True,True)
root.mainloop()