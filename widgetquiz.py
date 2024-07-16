'''
Project Title: Widgets
Author: Sanjam Singh
Date: June 11, 2024

[insert description of project and instructions for use]

'''


'''
TODO:
- fill out titleblock
- create at least 5 questions
    - each question requires:
        - it's own frame
        - a label to ask the question (in this frame)
        - a widget to get input (in this frame) ex. Button, Entry, RadioButton

- each question must use a different type of widget for input - Get creative!
- stylize the test to show off what you know! Use background and foreground
colours, alignment settings, images, frame padding etc. to make it appealing

'''
from tkinter import *
root = Tk()

# These lists will hold each of your StringVars (1 per question)
# and expected answers (1 per question)
# As you create your questions, append to these lists so that stringvars[i]
# is considered correct if it's value is equal to answers[i]
stringvars = []
answers = []
result = StringVar()
result.set("0")

def check_answers():
    points = 0
    for i in range(len(answers)):
        if stringvars[i].get() == answers[i]:
            points += 1
    result.set(str(points))

# Add all your questions and widgets here


f= Frame(root,padx=15,pady=15,bg= "black")
f.pack()


f1= Frame(f, padx= 10, pady= 10, bg= "black")
l1= Label(f1,text= "What is 2 + 2?", bg="black",fg= "white",justify= "center")
l1.pack()
a1= StringVar()
r1= Radiobutton(f1, text= "1", variable= a1, value='1')
r2= Radiobutton(f1, text= "3", variable= a1, value= '3')
r3= Radiobutton(f1, text= "4", variable= a1, value= '4')
r1.pack()
r2.pack()
r3.pack()

answers.append('4')
stringvars.append(a1)
print(answers)
print(stringvars)
f1.pack()



f2= Frame(f, padx= 10, pady= 10, bg= "lightblue")
l2= Label(f2, text= "What is my favourite color?",bg= "lightblue", fg= "black", justify= "center")
l2.pack()
a2= StringVar()
e1= Entry(f2, textvariable= a2)
e1.pack()
answers.append("black")
stringvars.append(a2)
f2.pack()

a3=StringVar()
def print_singh():
    global a3
    a3.set("singh")
    answers.append("singh")
    stringvars.append(a3)
def print_sidhu():
    global a3
    a3.set("sidhu")
    stringvars.append(a3)
def print_gill():
    global a3
    a3.set("gill")
    stringvars.append(a3)

f3= Frame(f, padx= 10, pady= 10, bg= "red")
l3= Label(f3, text= "What is my middle name?",bg= "black",fg= "white",justify= "center")
l3.pack()
b1= Button(f3, text= "singh", bg= "white", fg= "black", state= "normal", command= print_singh)
b1.pack()
b2= Button(f3, text= "sidhu", bg= "white", fg= "black", state= "normal", command= print_sidhu)
b2.pack()
b3= Button(f3, text= "gill", bg= "white", fg= "black", state= "normal", command= print_gill)
b3.pack()
f3.pack()


f4= Frame(f, height= 600, width= 600,bg= "purple")
l4= Label(f4, text= "What grade am I in?",bg= "white", fg= "black", justify= "center")
l4.pack()

a41 = StringVar()
c= Checkbutton(f4,text='Grade 9',fg='black',state='normal',variable=a41,onvalue='9',offvalue='0')
c.pack()

a42= StringVar()
c1= Checkbutton(f4,text='Grade 10',fg='black',state='normal',variable=a42,onvalue='10',offvalue='0')
c1.pack()

a43= StringVar()
c2= Checkbutton(f4,text='Grade 11',fg='black',state='normal',variable=a43,onvalue='11',offvalue='0')
c2.pack()

a44= StringVar()
c3= Checkbutton(f4,text='Grade 12',fg='black',state='normal',variable=a44,onvalue='12',offvalue='0')
c3.pack()
answers.append('10')
stringvars.append(a42)
f4.pack()


f5= Frame(f,height= 600, width= 600, bg= "pink")
l5= Label(f5, text= "How old am I?",bg= "black",fg= "white",justify= "center")
l5.pack()
a5= StringVar()
r4= Radiobutton(f5, text= "14", variable= a5, value='14')
r5= Radiobutton(f5, text= "15", variable= a5, value= '15')
r6= Radiobutton(f5, text= "16", variable= a5, value= '16')
r4.pack()
r5.pack()
r6.pack()
answers.append('16')
stringvars.append(a5)
print(answers)
print(stringvars)
f5.pack()
# This submit button should be at the end of your test
# It is meant to be clicked once the user has answered all questions
submitButton = Button(root, text='Submit Answers',
                      bg='white', command=check_answers)
submitButton.pack()

# This results label will display the number of questions answered correctly
# Feel free to change up the code for submitButton and results to make
# the test prettier and individualized!
results = Label(root, textvariable=result)
results.pack()

root.mainloop()
