from tkinter import*
root= Tk()
l= Label(root, text= "Enter your name.")
l.pack()
textbox= StringVar()
entry= Entry(root, textvariable=textbox)
entry.pack()
# def print_number():
#     num= int(input("Enter your number: "))
#     print(num)
# b1= Button(root, text="Click here to enter your number", command= print_number, fg="black", state="normal", justify= "center")
# b1.pack()
r3 = StringVar()


l1= Label(root, text= "Enter your number.")
l1.pack()
num= StringVar()
entry= Entry(root, textvariable=num)
entry.pack()

def check():
    a = num.get()
    if len(a)!=10:
        return r3.set('Try again')
    else:
        return r3.set("Good to go")

release= StringVar()
b2= Button(root, text= "check",command= check)
b2.pack()

l3= Label(root, textvariable=r3)
l3.pack()

l2= Label(root, text= "Enter your number.")
l2.pack()
listvar= StringVar(value= ('January','Febuary','March','April','May','June','July','August','September','October','November','December'))
listbox= Listbox(root, listvariable= listvar, height= 1, selectmode= 'extended',justify='center')
scroller= Scrollbar(root, orient= VERTICAL)
scroller.config(command=listbox.yview)
scroller.pack(side= RIGHT)
listbox.pack()
listbox.curselection()

release= StringVar()
listvar= StringVar(value= ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'))
listbox= Listbox(root, listvariable= listvar, height= 1, selectmode= 'extended', justify= "center")
listbox.pack()
listbox.curselection()

release= StringVar()
listvar= StringVar(value= ('1990','1991','1992','1993','1994','1995','1996','1997','1998','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'))
listbox= Listbox(root, listvariable= listvar, height= 1, selectmode= 'extended', justify= "center")
listbox.pack()
listbox.curselection()
root.mainloop()