from tkinter import *
from questions import *
from tkinter import messagebox
import random
from threading import Timer
import time
from PIL import ImageTk, Image
import pygame
import csv
import numpy

csv_name_sub = None
csv_name_ses = None

class Welcome(object):

    def __init__(self, master, csv_name_ses, csv_name_sub):

        self.master = master
        self.master.title('Task')
        self.master.wm_attributes('-fullscreen', True)
        #self.master.wm_attributes("-toolwindow", 1)  for WINDOWS, not MAC
        width, height = self.master.winfo_screenwidth(),self.master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (width, height))

        w = Canvas(self.master, width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        w.place(relx=0.5, rely=0.5, anchor=CENTER)

        buttonInst1=Button(self.master,text='NEXT', fg='black',bg="blue", command=self.gotoPage1, anchor=W)
        buttonInst1.configure(activebackground="#33B5E5", relief=FLAT)
        buttonInst1.pack()
        buttonInst1.place_configure(relx=0.49, rely=0.9, anchor=S)

        labelWelcome=Label(self.master, text ="WELCOME", fg='black', font="Helvetica 48 bold", anchor=CENTER)
        labelWelcome.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.labelSub=Label(self.master, text="Participant No.", fg='black', font="Helvetica 20 bold", justify = LEFT)
        self.labelSub.place(relx=0.40, rely=0.5, anchor=CENTER)
        #isCont=(self.master.register(self.val), '%d')
        self.entrySub=Entry(self.master,bg="grey")
        self.entrySub.place(relx=0.55, rely=0.5, anchor=CENTER)


        self.labelSes = Label(self.master, text="Session", fg='black', font="Helvetica 20 bold", justify = LEFT)
        self.labelSes.place(relx=0.40, rely=0.45, anchor=CENTER)
        #subInfo=StringVar() ####subjection information retrival###
        self.entrySes = Entry(self.master, bg="grey")
        self.entrySes.place(relx=0.55, rely=0.45, anchor=CENTER)


#/Users/kezhang/Desktop/Luck_LossAversion_v2/cues/
    def writeToFile(self):

        Welcome.csv_name_sub = str(self.entrySub.get())
        Welcome.csv_name_ses = str(self.entrySes.get())
        print(Welcome.csv_name_ses, 'session is first')
        print(Welcome.csv_name_sub, 'subject is first')

    def gotoPage1(self):
        self.writeToFile()
        self.root2=Toplevel(self.master)
        instPage1=instructionPage1(self.root2)


class instructionPage1(Toplevel):
    label_l1 = None
    label_l2 = None
    label_l3 = None
    buttonInst3 = None
    w = None

    def __init__(self, master):
        self.master = master
        self.master.title('Task')
        width, height = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (width, height))
        # self.master.overrideredirect(True)
        self.master.wm_attributes('-fullscreen', True)


        self.w = Canvas(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        self.w.pack()
        self.w.place(relx=0.5, rely=0.5, anchor=CENTER)

        canvas_width = master.winfo_screenwidth()
        canvas_height = master.winfo_screenheight()
        middleX = canvas_width / 2
        circleMX = middleX / 2
        middleY = canvas_height / 2
        circleMY = middleY
        radius = 100

        self.label_l1 = Label(self.master, text="Instruction", fg='black', font="Helvetica 30 bold",
                              anchor=N)
        self.label_l1.place(relx=0.5, rely=0.1, anchor=CENTER)

        buttonInst4 = Button(self.master, text='NEXT', fg='black', bg="blue", command=self.gotoPage2, anchor=W)
        buttonInst4.configure(activebackground="#33B5E5", relief=FLAT)
        buttonInst4.pack()
        buttonInst4.place_configure(relx=0.49, rely=0.9, anchor=S)

        self.instr1 = """In this experiment you will be asked to make a series of financial decisions. Each decision will either result in a win, a loss, or a zero outcome. Your goal is to maximize the amount of money you win.
"""
        self.instr2 = """For each decision, you will be presented with two options, one on the right and one on the left. 
"""
        self.instr3 = """To select the option on the left, press Z.
To select the option on the right, press M.
"""

        self.message1 = Message(self.master, text = self.instr1, width = canvas_width - 130,
                                font = 'calibri 24 bold')
        self.message1.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.message2 = Message(self.master, text=self.instr2, width = canvas_width - 130,
                                font='calibri 24 bold')
        self.message2.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.message3 = Message(self.master, text=self.instr3, width = canvas_width - 130,
                                font='calibri 24 bold')
        self.message3.place(relx=0.5, rely=0.6, anchor=CENTER)

    def gotoPage2(self):
        self.root3=Toplevel(self.master)
        self.instPage2=instructionPage2(self.root3)

class instructionPage2():

    label_l1 = None
    label_l2 = None
    w = None
    buttonInst2 = None
    button1 = None
    button2 = None

    def __init__(self, master):
        self.master = master
        self.master.title('Task')
        width, height = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (width, height))
        # self.master.overrideredirect(True)
        self.master.wm_attributes('-fullscreen', True)

        self.w = Canvas(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        self.w.pack()
        self.w.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.w1= Canvas(master, width=130, heigh=200)
        self.w1.pack()
        self.w1.place()

        canvas_width = master.winfo_screenwidth()
        canvas_height = master.winfo_screenheight()
        middleX = canvas_width / 2
        circleMX = middleX / 2
        middleY = canvas_height / 2
        circleMY = middleY
        radius = 100


        self.label_l1=Label(self.master, text = "Instruction", fg='black', font="Helvetica 30 bold",
                            anchor=N)
        self.label_l1.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.label_l2=Label(self.master,
                            text="In this example:",
                            font= "calibri 22 bold", anchor=CENTER)
        self.label_l2.place(relx=0.5, rely=0.2, anchor=CENTER)

        explanation1 = """\u25C6 Choosing the option on the left offers a 50-50 chance of winning $6 or losing $4."""
        explanation2 = """\u25C6 Choosing the option on the right will always lead to a zero outcome (no win or loss)."""
        explanation5="""We will record the outcome of the trials, but they will not be shown to you.
 """

        self.label_l3 = Label(self.master, text=explanation1, font="calibri 22 ", justify=LEFT)
        self.label_l3.place(relx=0.2, rely=0.27, anchor=W)

        self.label_l4 = Label(self.master, text=explanation2, font="calibri 22", justify=LEFT)
        self.label_l4.place(relx = 0.2, rely=0.32, anchor=W)

        self.label_l7 = Label(self.master, text=explanation5, font="calibri 22 italic")
        self.label_l7.place(relx=0.5, rely=0.80, anchor = CENTER)

        self.rec1 = self.w.create_rectangle(circleMX - radius - 40, middleY - 60, middleX - 50, middleY + radius * 2-40,
                                             outline = 'red', width = 3)
        self.rec2 = self.w.create_rectangle(middleX+50, middleY - 60, middleX+circleMX+radius+40, middleY + radius * 2 -40,
                                            outline='red', width=3)

        self.w.create_oval(circleMX - radius+150, circleMY - radius + 50, circleMX + radius+150, circleMY + radius+50)

        self.w.create_oval(circleMX - radius + middleX-150, circleMY - radius + 50, circleMX + radius + middleX-150, circleMY
                           + radius+50, fill='navajo white')
        self.w.create_line(circleMX+150, circleMY - radius +50, circleMX+150, circleMY + radius+50)


        self.w.create_text(middleX + circleMX -150 , circleMY+40, text="100%", font="Helvetica 18 bold", fill="brown3")
        self.w.create_text(middleX +circleMX-150, circleMY+65, text="$0", font="Helvetica 18" )

        #coloring: in pure gain, certainty uses navajo white, win=sky blue, loss=dodger blue#
        self.w.create_arc(circleMX - radius+150, circleMY - radius + 50, circleMX + radius+150, circleMY + radius+50,
                          start=90, extent=180, fill='sky blue')
        self.w.create_arc(circleMX - radius + 150, circleMY - radius + 50, circleMX + radius + 150,
                          circleMY + radius+50, start=270, extent=180, fill='dodger blue')
        self.w.create_text(circleMX + 100, circleMY +40, text="50%", font="Helvetica 18 bold", fill="brown3")
        self.w.create_text(circleMX + 100, circleMY + 65, text="$6", font="Helvetica 18" )
        self.w.create_text(middleX - 125, circleMY +40, text="50%", font="Helvetica 18 bold", fill="brown3")
        self.w.create_text(middleX - 125, circleMY + 65, text="$- 4", font="Helvetica 18")

        self.w.create_text(circleMX-50, circleMY+40, text = "LEFT", font = 'calibri 20 bold')
        self.w.create_text(circleMX+middleX + 50, circleMY+40, text="RIGHT", font='calibri 20 bold')

        self.w.create_text(circleMX - 50, circleMY + 75, text="(Press key Z)", font='calibri 20 bold')
        self.w.create_text(circleMX + middleX + 50, circleMY + 75, text="(Press key M)", font='calibri 20 bold')

        self.buttonInst2=Button(self.master, text="NEXT", fg='black', command=self.gotoPage3, anchor=W)
        self.buttonInst2.configure(activebackground="#33B5E5", relief=FLAT)
        self.buttonInst2.pack()
        self.buttonInst2.place_configure(relx=0.49, rely=0.9, anchor=S)


    def gotoPage3(self):
        self.root4 = Toplevel(self.master)
        self.instPage3 = instructionPage3(self.root4)


class instructionPage3():

    label_l1=None
    label_l2=None
    label_l3=None
    buttonInst3=None
    w=None

    def __init__(self, master):
        self.master = master
        self.master.title('Task')
        width, height = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (width, height))
        self.master.wm_attributes('-fullscreen', True)

        self.w = Canvas(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        self.w.pack()
        self.w.place(relx=0.5, rely=0.5, anchor=CENTER)

        canvas_width = master.winfo_screenwidth()
        canvas_height = master.winfo_screenheight()
        middleX = canvas_width / 2
        circleMX = middleX / 2
        middleY = canvas_height / 2
        circleMY = middleY
        radius = 100


        self.label_l1=Label(self.master, text = "Instruction", fg='black', font="Helvetica 30 bold",
                            anchor=N)
        self.label_l1.place(relx=0.5, rely=0.1, anchor=CENTER)

        # explanation1 = """There are no right or wrong answers, we are interested in your preferences."""
        #explanation2 = """Remuneration:"""

        explanation3 = """At the end of the task, three of your choices will be randomly selected, and you will receive the outcomes of these choices as a cash bonus, up to a maximum of $20. Therefore it is important you consider your choices carefully throughout the task, as some of your choices will have real financial consequences. 
"""
        explanation4 = """You will now have the opportunity to practice three choices. There are no right or wrong answers, we are interested in your preferences. If you have any questions during this practice, ask the experimenter for assistance.

"""

        self.message7 = Message(self.master, text=explanation4, width=canvas_width - 130,
                                font='calibri 24 bold', justify = LEFT)
        self.message7.place(relx=0.5, rely=0.3, anchor=CENTER)


        self.message6 = Message(self.master, text=explanation3, width=canvas_width - 130,
                                font='calibri 24 bold', justify = LEFT)
        self.message6.place(relx=0.5, rely=0.5, anchor=CENTER)


        #self.label_l6 = Label(self.master, text=explanation4, font="calibri 20 bold", anchor=CENTER)
        #self.label_l6.place(relx=0.1, rely=0.65)

        self.buttonInst3 = Button(self.master, text="NEXT", fg='black', command=self.gotoPage3, anchor=W)
        self.buttonInst3.configure(activebackground="#33B5E5", relief=FLAT)
        self.buttonInst3.pack()
        self.buttonInst3.place_configure(relx=0.49, rely=0.9, anchor=S)


    def gotoPage3(self):
        self.root5 = Toplevel(self.master)
        self.instPage4 = practisePage1(self.root5)


class practisePage1():

    questionCoverBlockEx = None
    w = None
    labelEx = None
    label_1 = None
    line_c1 = None
    button1Ex = None
    button2Ex = None
    lostState1 = None
    lostState2 = None
    width=None
    height=None
    image = None
    imDisplay=None
    middleX = None
    circleMX = None
    middleY = None
    circleMY = None
    radius = None
    loss_sound = None
    loss1_image = None
    leftClick = None
    rightClick = None
    choiceA = None
    choiceB = None

    def __init__(self, master):
        self.master = master
        self.master.title('Task')
        self.width, self.height = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (self.width, self.height))
        self.master.wm_attributes('-fullscreen', True)

        self.w = Canvas(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        self.w.pack()
        self.w.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.middleX = self.width / 2
        self.circleMX = self.middleX / 2
        self.middleY = self.height / 2
        self.circleMY = self.middleY
        self.radius = 200

        self.labelEx = self.w.create_text(0.5*self.width, 0.1*self.height, text='Practice 1',font="Helvetica 36")

        self.w.create_oval(self.circleMX - self.radius, self.circleMY - self.radius,
                           self.circleMX + self.radius, self.circleMY + self.radius)
        self.w.create_oval(self.circleMX - self.radius + self.middleX, self.circleMY - self.radius,
                           self.circleMX + self.radius + self.middleX, self.circleMY + self.radius, fill="navajo white")
        self.line_c1 = self.w.create_line(self.circleMX, self.circleMY - self.radius, self.circleMX, self.circleMY + self.radius)

        self.ins_100 = self.w.create_text(self.circleMX + self.middleX, self.circleMY, text='$-3', font="Helvetica 48")


        #coloring: in pure loss, certainty uses navajo white, small=deepSkyBlue3, large=firebrick3#
        self.w.create_arc(self.circleMX - self.radius, self.circleMY - self.radius, self.circleMX +
                          self.radius, self.circleMY + self.radius, start=90, extent=180, fill='deepSkyBlue3')
        self.w.create_arc(self.circleMX - self.radius, self.circleMY - self.radius, self.circleMX + self.radius,
                          self.circleMY + self.radius, start=270, extent=180, fill='firebrick3')
        self.ins_50_1 = self.w.create_text(self.circleMX - 110, self.circleMY, text='$-1', font="Helvetica 48")
        self.ins_50_2 = self.w.create_text(self.circleMX + 110, self.circleMY, text='$-5', font="Helvetica 48")

        self.choiceA = master.bind('z', self.showResultEx1)
        self.choiceB = master.bind('m', self.showResultEx2)

        self.confRec_c1 = self.w.create_rectangle(self.circleMX - self.radius - 30, self.circleMY - self.radius - 20,
                                                  self.circleMX + self.radius + 30, self.circleMY + self.radius + 20,
                                                  outline='red', width = 5, state = "hidden")
        self.confRec_c2 = self.w.create_rectangle(self.circleMX - self.radius + self.middleX - 30, self.circleMY - self.radius - 20,
                                                  self.circleMX + self.radius + self.middleX + 30, self.circleMY + self.radius + 20,
                                                  outline='red', width = 5, state = "hidden")


    def showResultEx1(self, event = None):
        self.w.itemconfigure(self.confRec_c1, state = 'normal')
        t = Timer(1, self.showButtonInst3)
        t.start()
        self.master.unbind("<z>", self.choiceA)
        self.master.unbind("<m>", self.choiceB)


    def showResultEx2(self, event=None):
        self.w.itemconfigure(self.confRec_c2, state = 'normal')
        t = Timer(1, self.showButtonInst3)
        t.start()
        self.master.unbind("<m>", self.choiceB)
        self.master.unbind("<z>", self.choiceA)


    def showButtonInst3(self):
        self.buttonInst3=Button(self.master, text="NEXT", fg='black', command=self.gotoPage4, anchor=W)
        self.buttonInst3.configure(activebackground="#33B5E5", relief=FLAT)
        self.buttonInst3.pack()
        self.buttonInst3.place_configure(relx=0.49, rely=0.9, anchor=S)

    def gotoPage4(self):
        self.root5=Toplevel(self.w)
        self.instPage4=practisePage2(self.root5)

class practisePage2():

    questionCoverBlockEx = None
    w = None
    labelEx = None
    label_1 = None
    line_c2 = None
    button1Ex = None
    button2Ex = None
    winState1=None
    winState2=None
    width = None
    height = None
    win5_image = None
    win_sound = None
    choiceA = None
    choiceB = None


    def __init__(self, master):
        self.master = master
        self.master.title('Task')
        self.width, self.height = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (self.width, self.height))
        self.master.wm_attributes('-fullscreen', True)

        self.w = Canvas(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        self.w.pack()
        self.w.place(relx=0.5, rely=0.5, anchor=CENTER)

        canvas_width = master.winfo_screenwidth()
        canvas_height = master.winfo_screenheight()
        middleX = canvas_width / 2
        circleMX = middleX / 2
        middleY = canvas_height / 2
        circleMY = middleY
        radius = 200


        self.labelEx = self.w.create_text(0.5 * self.width, 0.1 * self.height, text='Practice 2', font="Helvetica 36")

        self.w.create_oval(circleMX - radius, circleMY - radius, circleMX + radius, circleMY + radius)
        self.w.create_oval(circleMX - radius + middleX, circleMY - radius, circleMX + radius + middleX,
                           circleMY + radius, fill='navajo white')
        self.line_c1 = self.w.create_line(circleMX, circleMY - radius, circleMX, circleMY + radius)

        self.ins_100 = self.w.create_text(circleMX + middleX, circleMY, text='$21', font="Helvetica 48")
        self.confRec_c1 = self.w.create_rectangle(circleMX - radius - 30, circleMY - radius - 20,
                                                  circleMX + radius + 30, circleMY + radius + 20,
                                                  outline='red', state='hidden', width = 5)
        self.confRec_c2 = self.w.create_rectangle(circleMX - radius + middleX - 30, circleMY - radius - 20,
                                                  circleMX + radius + middleX + 30, circleMY + radius + 20,
                                                  outline='red', state='hidden', width = 5)

        #coloring: in pure gain, certainty uses navajo white, small=light sea green, large=tomato#
        self.w.create_arc(circleMX - radius, circleMY - radius, circleMX + radius, circleMY + radius, start=90,
                          extent=180, fill='light sea green')
        self.w.create_arc(circleMX - radius, circleMY - radius, circleMX + radius, circleMY + radius, start=270,
                          extent=180, fill='tomato')
        self.ins_50_1 = self.w.create_text(circleMX - 110, circleMY, text='$6', font="Helvetica 48")
        self.ins_50_2 = self.w.create_text(circleMX + 110, circleMY, text='$36', font="Helvetica 48")


        self.choiceA = master.bind('z', self.showResultEx1)
        self.choiceB = master.bind('m', self.showResultEx2)


    def showResultEx1(self, event = None):
        self.w.itemconfigure(self.confRec_c1, state = 'normal')
        t = Timer(1, self.showButtonInst3)
        t.start()
        self.master.unbind("<z>", self.choiceA)
        self.master.unbind("<m>", self.choiceB)



    def showResultEx2(self, event=None):
        self.w.itemconfigure(self.confRec_c2, state='normal')
        t = Timer(1, self.showButtonInst3)
        t.start()
        self.master.unbind("<m>", self.choiceB)
        self.master.unbind("<z>", self.choiceA)


    def showButtonInst3(self):
        self.buttonInst3=Button(self.master, text="NEXT", fg='black', command=self.gotoPage4, anchor=W)
        self.buttonInst3.configure(activebackground="#33B5E5", relief=FLAT)
        self.buttonInst3.pack()
        self.buttonInst3.place_configure(relx=0.49, rely=0.9, anchor=S)

    def gotoPage4(self):
        root6=Toplevel(self.w)
        self.instpage5=practisePage3(root6)

class practisePage3():

    questionCoverBlockEx = None
    w = None
    labelEx = None
    label_1 = None
    line_c2 = None
    button1Ex = None
    button2Ex = None
    winState1=None
    winState2=None
    win2_image = None
    win_sound = None
    choiceA = None
    choiceB = None

    def __init__(self, master):
        self.master = master
        self.master.title('Task')
        width, height = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (width, height))
        self.master.wm_attributes('-fullscreen', True)

        self.w = Canvas(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        self.w.pack()
        self.w.place(relx=0.5, rely=0.5, anchor=CENTER)

        canvas_width = master.winfo_screenwidth()
        canvas_height = master.winfo_screenheight()
        middleX = canvas_width / 2
        circleMX = middleX / 2
        middleY = canvas_height / 2
        circleMY = middleY
        radius = 200


        self.labelEx = self.w.create_text(0.5 * width, 0.1 * height, text='Practice 3', font="Helvetica 36")

        self.w.create_oval(circleMX - radius, circleMY - radius, circleMX + radius, circleMY + radius)
        self.w.create_oval(circleMX - radius + middleX, circleMY - radius, circleMX + radius + middleX,
                           circleMY + radius, fill='navajo white')
        self.line_c1 = self.w.create_line(circleMX, circleMY - radius, circleMX, circleMY + radius)

        self.ins_100 = self.w.create_text(circleMX + middleX, circleMY, text='$0', font="Helvetica 48")

        self.confRec_c1 = self.w.create_rectangle(circleMX - radius - 30, circleMY - radius - 20,
                                                  circleMX + radius + 30, circleMY + radius + 20,
                                                  outline='red', state='hidden', width = 5)
        self.confRec_c2 = self.w.create_rectangle(circleMX - radius + middleX - 30, circleMY - radius - 20,
                                                  circleMX + radius + middleX + 30, circleMY + radius + 20,
                                                  outline='red', state='hidden', width = 5)
        #coloring: in mixed, certainty uses navajo white, win=sky blue, loss=dodger blue#
        self.w.create_arc(circleMX - radius, circleMY - radius, circleMX + radius, circleMY + radius, start=90,
                          extent=180, fill='sky blue')
        self.w.create_arc(circleMX - radius, circleMY - radius, circleMX + radius, circleMY + radius, start=270,
                          extent=180, fill='dodger blue')
        self.ins_50_1 = self.w.create_text(circleMX - 110, circleMY, text='$6', font="Helvetica 48")
        self.ins_50_2 = self.w.create_text(circleMX + 110, circleMY, text='$-4', font="Helvetica 48")


        self.choiceA = master.bind('z', self.showResultEx1)
        self.choiceB = master.bind('m', self.showResultEx2)


    def showResultEx1(self, event=None):
        self.w.itemconfigure(self.confRec_c1, state="normal")
        t = Timer(1, self.showButtonInst3)
        t.start()
        self.master.unbind("<z>", self.choiceA)
        self.master.unbind("<m>", self.choiceB)


    def showResultEx2(self, event=None):
        self.w.itemconfigure(self.confRec_c2, state="normal")
        t = Timer(1, self.showButtonInst3)
        t.start()
        self.master.unbind("<m>", self.choiceB)
        self.master.unbind("<z>", self.choiceA)

    def showButtonInst3(self):
        self.buttonInst3=Button(self.master, text="START TASK", fg='black', command=self.gotoApp, anchor=W)
        self.buttonInst3.configure(activebackground="#33B5E5", relief=FLAT)
        self.buttonInst3.pack()
        self.buttonInst3.place_configure(relx=0.49, rely=0.9, anchor=S)

    def gotoApp(self):
        root7=Toplevel(self.w)
        self.instpage6=App(root7, csv_name_ses, csv_name_sub)

class App(Welcome):

    label_50_1_c1 = None
    label_50_2_c1 = None
    label_100_c1 = None
    label_50_1_c2 = None
    label_50_2_c2 = None
    label_100_c2 = None
    label_image = None
    msg = None
    line_c1 = None
    line_c2 = None
    cue_effect = None
    win1_image = None
    win2_image = None
    win3_image = None
    win4_image = None
    win5_image = None
    loss1_image = None
    loss2_image = None
    loss3_image = None
    loss4_image = None
    loss5_image = None
    loss_sound = None
    win_sound = None
    bindid = None
    rebind = None
    bind_id_a = None
    bind_id_l= None
    start_time = None
    end_time = None
    human_choice = None

    computer_choice_label = None
    is_c1 = True
    questionCoverBlock = None
    imDisplay = None
    image = None
    value = None
    w = None
    canvas_width=None
    canvas_height=None
    middleX = None
    circleMX = None
    middleY = None
    circleMY = middleY
    radius = None
    confRec_c1 = None
    confRec_c2 = None
    master = None
    radius = 200
    finishedQuestionQty = 1



    #q_index: there are 5 pairs of questions for each pure gains and pure losses, the q_index represents each pair. Each pair repeats for once#
    q = []
    q_index = None
    clicked = []
    computerChoice = []
    isPure = True
    isMixed1 = True
    isMixed2 = True
    shouldShowQuestion = True
    button1 = None
    button2 = None
    choiceA = None
    choiceB = None
    buttonNext=None
    ButtonQuit=None
    finishedQuestionQty = 1   #how many questions are finished currently#
    questionNumber = 1 ### number of initial x question. For each set of gambles(pure gain/loss, and mixed), there are 5 questions as initial question####
    fileResult = None
    elapsed_time = None
#for loop, repeat the equations#

    def __init__(self, master, csv_name_ses, csv_name_sub):
        Welcome.__init__(self, master, csv_name_ses, csv_name_sub)
        self.csv_name_sub = Welcome.csv_name_sub
        self.csv_name_ses = Welcome.csv_name_ses
        print('session is', Welcome.csv_name_ses)
        print("subject is", Welcome.csv_name_sub)
        self.resultFile = open(
            "/Users/kezhang/Desktop/Luck_LossAversion_v2/Results/results_staircase/without_outcome_staircase/" + self.csv_name_sub + '_' + self.csv_name_ses +
            '_outcome_staircase_results.csv', 'w')


        self.resultFileWrite = csv.writer(self.resultFile)
        self.resultFileWrite.writerow(
            ['trial','v_50_1', 'v_50_2', 'v_100', 'subject choice', 'computer choice', 'rt(ms)'])

        self.master = master
        self.master.title('Task')
        self.canvas_width, self.canvas_height = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (self.canvas_width, self.canvas_height))
        self.master.wm_attributes('-fullscreen', True)

        self.w = Canvas(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        self.w.pack()
        self.w.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.middleX = self.canvas_width / 2
        self.circleMX = self.middleX / 2
        self.middleY = self.canvas_height / 2
        self.circleMY = self.middleY
        radius = 200

        self.q_index = random.randrange(0, 2 * self.questionNumber, 1)

        i = 1
        while i < 4: # for different block of questions
            j = 0
            while j < self.questionNumber: # for different init x
                self.q.append(question(i, j))
                self.clicked.append([])
                self.computerChoice.append([])
                j += 1
            i += 1

        print('initialized questions: ')
        for index, q in enumerate(self.q):
            print("question ", index, " with values ", q.v_50_1, q.v_50_2, q.v_100)

        #graphs#
        self.c1 = self.w.create_oval(self.circleMX-radius, self.circleMY-radius, self.circleMX+radius, self.circleMY+radius)
        self.c2 = self.w.create_oval(self.circleMX - radius +  self.middleX, self.circleMY - radius,
                                     self.circleMX + radius + self.middleX, self.circleMY + radius)

        # coloring: in pure gain, certainty uses navajo white, small=light sea green, large=tomato#
        #Small is the half circle at the left#
        self.arc_c1_Small = self.w.create_arc(self.circleMX - radius, self.circleMY - radius, self.circleMX + radius,
                                                  self.circleMY + radius, start=90,
                                                  extent=180, state='hidden', outline='')
        self.arc_c1_Large = self.w.create_arc(self.circleMX - radius, self.circleMY - radius, self.circleMX + radius,
                                                  self.circleMY + radius, start=270,
                                                  extent=180, state='hidden', outline='')
        self.arc_c2_Small = self.w.create_arc(self.circleMX - radius + self.middleX, self.circleMY - radius,
                                                  self.circleMX + radius + self.middleX, self.circleMY + radius,
                                                  start=90, extent=180, state='hidden', outline='')
        self.arc_c2_Large = self.w.create_arc(self.circleMX - radius + self.middleX, self.circleMY - radius,
                                                  self.circleMX + radius + self.middleX, self.circleMY + radius,
                                                  start=270, extent=180, state='hidden', outline='')


        self.choiceA = self.master.bind('z', self.run1)
        self.choiceB = self.master.bind('m', self.run2)

#attach labels on windows, and labels' locations. _c2 means the second circle, _c1 means the first circle#

        self.label_50_1_c1 = self.w.create_text(self.circleMX - 110, self.circleMY, text="$" + str(self.q[self.q_index].v_50_1), font="Helvetica 48")
        self.label_50_2_c1 = self.w.create_text(self.circleMX+110, self.circleMY, text="$" + str(self.q[self.q_index].v_50_2), font="Helvetica 48")
        self.label_100_c2 = self.w.create_text(self.circleMX+self.middleX, self.circleMY, text="$" + str(self.q[self.q_index].v_100),
                                               font="Helvetica 48")

# randomize for labels' locations: _c2 means the second circle, _c1 means the first circle#
        self.label_50_1_c2 = self.w.create_text(self.middleX + self.circleMX - 110, self.circleMY,text="$" + str(self.q[self.q_index].v_50_1), font="Helvetica 48")
        self.label_50_2_c2 = self.w.create_text(self.middleX + self.circleMX + 110, self.circleMY,text="$" + str(self.q[self.q_index].v_50_2), font="Helvetica 48")
        self.label_100_c1 = self.w.create_text(self.circleMX, self.circleMY,text="$" + str(self.q[self.q_index].v_100), font="Helvetica 48")

        self.computer_choice_label = Label(self.w, text='', fg='black')
        self.computer_choice_label.pack()
        self.w.create_window(600, 50, window=self.computer_choice_label)

        self.line_c1 = self.w.create_line(self.circleMX, self.circleMY - radius, self.circleMX, self.circleMY + radius)
        self.line_c2 = self.w.create_line(self.middleX + self.circleMX, self.circleMY - self.radius, self.middleX + self.circleMX,
                                          self.circleMY + radius)
        self.questionCoverBlock = self.w.create_rectangle(0, self.canvas_height, self.canvas_width, 50, outline= "white", fill="")

        self.randomize()
        self.displayOneSide()
        self.displayColor()
        self.start_time = time.time()
        print('start time is at initial ', self.start_time)


    def rebind_a(self):
        self.choiceA = self.master.bind("<a>", self.run1)
        print("rebinding A on")

    def rebind_l(self):
        self.choiceB = self.master.bind("<l>", self.run2)
        print('rebinding L on')

    # button run1:how do numbers change#
    def run1(self, event=None):
        self.draw_confirmation_button1()
        t = Timer(1, self.run1_s2)
        t.start()
        self.master.unbind("<m>", self.choiceB)
        self.master.unbind("<z>", self.choiceA)
        self.master.after(3000, self.rebind_a)
        self.end_time = time.time()
        print( "end time in run 1 is ", self.end_time)
        self.elapsed_time = (self.end_time - self.start_time) * 1000
        print('reaction time in run 1 is ', self.elapsed_time)
        return


    def run1_s2(self):
    #Choice A is 50/50 gamble, Choice B is the certainty.#
        print('for index ', self.q_index, ' choice is false')
        self.clickPreProcess(False)
        self.q[self.q_index].get_question(False)
        self.clicked[self.q_index].append(False)
        self.clickPostProcess()



    # button run2: how do numbers change#
    def run2(self, event=None):
        self.draw_confirmation_button2()
        t = Timer(1, self.run2_s2)
        t.start()
        self.master.unbind("<m>", self.choiceB)
        self.master.unbind("<z>", self.choiceA)
        self.master.after(3000, self.rebind_l)
        self.end_time = time.time()
        print("end time in run 2 is ", self.end_time)
        self.elapsed_time = (self.end_time - self.start_time) * 1000
        print('reaction time in run 2 is ', self.elapsed_time)
        return


    def run2_s2(self):
        print('for index ', self.q_index, ' choice is true')
        self.clickPreProcess(True)
        self.q[self.q_index].get_question(True)
        self.clicked[self.q_index].append(True)
        self.clickPostProcess()


    def clickPreProcess(self, human_choice):
        print('ClickPreProcess ------  q_index is ', self.q_index)
        self.computerChoose(human_choice)
        self.showResult()

    def clickPostProcess(self):
        self.finishedQuestionQty += 1
        print("current finished question count is ", self.finishedQuestionQty)
        if self.finishedQuestionQty == 2 * self.questionNumber * self.q[0].limit and self.isPure:
            # if 5 questions for gain and 5 questions for loss completed, each question has 6 iteration completed.
            print("Pure questions done, start mixed block 1 now")
            self.isPure = False
            self.initMixQuestions()

        elif self.finishedQuestionQty == 3 * self.questionNumber * self.q[0].limit + 1:
            # a = messagebox.showinfo("You can take a break")
            t = Timer(2, self.breakTime())
            t.start()
            return

            # if 5 questions have repeated 5 times: 1 pure gain, 1 pure loss, 1 mixed staircase, 1 mixed staircase,
            # 1 mixed matrix. AND first 4 blocks have 6 iteration, and the matrix block has 7 iterations.



        else:
            self.q[0]


      # when one question is finished, need to select another question to start iteration
        while self.q[self.q_index].to_display is False:
            print("question ", self.q_index, " is finished")

            # display from questionNumber 0, to questionNumber 10, that is pure questions
            if self.isPure:
                self.q_index = random.randrange(0, 2 * self.questionNumber, 1) # 2x2

            else:
                self.q_index = random.randrange(2 * self.questionNumber, 3 * self.questionNumber, 1) #2

        t = Timer(2, self.clearResult)
        t.start()

    def breakTime(self):
        self.questionCoverBlock = self.w.create_rectangle(0, 0, self.canvas_width, 600, outline= "white", fill="white")
        self.computer_choice_label['text'] = ''
        explantion = """        You can take a break
        Press START to continue"""

        self.msg = Label(self.master, text=explantion,
                         fg='black', font="calibri 36 bold", anchor=CENTER, justify = CENTER)
        self.msg.place(relx = 0.26, rely = 0.3)

        buttonBreak = Button(self.master, text='START', fg='black', bg="blue", command=self.gotoMatrix, anchor=W)
        buttonBreak.configure(activebackground="#33B5E5", relief=FLAT)
        buttonBreak.pack()
        buttonBreak.place_configure(relx=0.49, rely=0.9, anchor=S)

    def gotoMatrix(self):
        self.root8=Toplevel(self.master)
        matrix = App1(self.root8, csv_name_ses, csv_name_sub, question.algorithmIndex, question.initX, question.mid_loss_list, question.mid_gain_list)


    def initMixQuestions(self):
        i = 0
        while i < self.questionNumber:
            mid = self.q[i].v_100_history_gain[-1]/2 + self.q[i].v_100_history_gain[-2]/2
            self.q[i + 2 * self.questionNumber].initMixQuestion(mid)
            print('gain list v_100 history ', self.q[i].v_100_history_gain)
            i += 1


    def displayQuestion(self):
        print("displaying question ", self.q_index, " with values ",
              self.q[self.q_index].v_50_1,self.q[self.q_index].v_50_2,self.q[self.q_index].v_100)


        self.w.itemconfigure(self.label_100_c1, text= "$" + str(round(self.q[self.q_index].v_100, 2)))
        self.w.itemconfigure(self.label_100_c2, text= "$" + str(round(self.q[self.q_index].v_100, 2)))
        self.w.itemconfigure(self.label_50_1_c1, text= "$" + str(round(self.q[self.q_index].v_50_1, 2)))
        self.w.itemconfigure(self.label_50_2_c1, text= "$" + str(round(self.q[self.q_index].v_50_2, 2)))
        self.w.itemconfigure(self.label_50_1_c2, text= "$" + str(round(self.q[self.q_index].v_50_1, 2)))
        self.w.itemconfigure(self.label_50_2_c2, text= "$" + str(round(self.q[self.q_index].v_50_2, 2)))

        self.randomize()
        self.displayOneSide()
        self.displayColor()

        #self.start_time = time.clock()
        self.start_time = time.time()
        print('start time is at displayQuestion', self.start_time)
        return



    # computer generates a win number#

    def computerChoose(self, human_choice):
        if human_choice is True: ## human choice is B, 100%##
            print('current question is ', self.q[self.q_index].v_50_1,self.q[self.q_index].v_50_2, self.q[self.q_index].v_100)
            print('human choose + Choice B')
            self.value = round(self.q[self.q_index].v_100, 2)

            self.resultFileWrite.writerow(
                [self.finishedQuestionQty, str(self.q[self.q_index].v_50_1), str(self.q[self.q_index].v_50_2), str(self.q[self.q_index].v_100),
                 str(human_choice), str(self.value), self.elapsed_time])
            self.resultFile.flush()

            print('results', str(self.q[self.q_index].v_50_1), str(self.q[self.q_index].v_50_2), str(self.q[self.q_index].v_100),
                 str(human_choice), str(self.value), self.elapsed_time)

            return

        ## following is human choice is A, 50/50
        index = random.randrange(0, 2, 1)
        print('human choose + Choice A')
        if index == 0:
            self.computerChoice[self.q_index].append(True)
            index2 = random.randrange(0, 2, 1)
            if index2 == 0:
                self.value = round(self.q[self.q_index].v_50_1, 2)
            else:
                self.value = round(self.q[self.q_index].v_50_2, 2)

            self.resultFileWrite.writerow(
                [str(self.finishedQuestionQty), str(self.q[self.q_index].v_50_1), str(self.q[self.q_index].v_50_2), str(self.q[self.q_index].v_100),
                 str(human_choice), str(self.value), self.elapsed_time])
            self.resultFile.flush()

        else:
            self.computerChoice[self.q_index].append(False)
            index2 = random.randrange(0, 2, 1)
            if index2 == 0:
                self.value = round(self.q[self.q_index].v_50_1, 2)
            else:
                self.value = round(self.q[self.q_index].v_50_2, 2)


            self.resultFileWrite.writerow(
                [str(self.finishedQuestionQty), str(self.q[self.q_index].v_50_1), str(self.q[self.q_index].v_50_2), str(self.q[self.q_index].v_100),
                 str(human_choice), str(self.value), self.elapsed_time])
            self.resultFile.flush()

    def randomize(self):
        num = random.random()
        if num < 0.4:
            self.is_c1 = not self.is_c1
        print('randomize ----', self.is_c1)


    def displayOneSide(self):
        if self.is_c1:
            self.w.itemconfigure(self.line_c2, state='hidden')
            self.w.itemconfigure(self.line_c1, state='normal')

            self.w.itemconfigure(self.label_50_1_c1, state='normal')
            self.w.itemconfigure(self.label_50_2_c1, state='normal')
            self.w.itemconfigure(self.label_100_c2, state='normal')

            self.w.itemconfigure(self.label_100_c1, state='hidden')
            self.w.itemconfigure(self.label_50_1_c2, state='hidden')
            self.w.itemconfigure(self.label_50_2_c2, state='hidden')

        else:
            self.w.itemconfigure(self.line_c1, state='hidden')
            self.w.itemconfigure(self.line_c2, state='normal')

            self.w.itemconfigure(self.label_50_1_c2, state='normal')
            self.w.itemconfigure(self.label_50_2_c2, state='normal')
            self.w.itemconfigure(self.label_100_c1, state='normal')

            self.w.itemconfigure(self.label_100_c2, state='hidden')
            self.w.itemconfigure(self.label_50_1_c1, state='hidden')
            self.w.itemconfigure(self.label_50_2_c1, state='hidden')


        self.buttonRandom()


    def buttonRandom(self):
        if self.is_c1:
            self.choiceA = self.master.bind('z', self.run1)
            self.choiceB = self.master.bind('m', self.run2)
        else:
            self.choiceA = self.master.bind('z', self.run2)
            self.choiceB = self.master.bind('m', self.run1)


    def draw_confirmation_button1(self):
        #true, reverse; false, not reverse)
        print('draw confirmation for button1----', self.is_c1)
        if self.is_c1:
            self.confRec_c2 = self.w.create_rectangle(self.circleMX - self.radius - 30,
                                                      self.circleMY - self.radius - 20,
                                                      self.circleMX + self.radius + 30,
                                                      self.circleMY + self.radius + 20,
                                                      outline='red', width = 5)

        else:
            self.confRec_c1 = self.w.create_rectangle(self.circleMX - self.radius + self.middleX - 30, self.circleMY -
                                    self.radius - 20, self.circleMX + self.radius + self.middleX + 30,
                                    self.circleMY + self.radius + 20, outline = 'red', width = 5)


    def draw_confirmation_button2(self):
        #true, reverse; false, not reverse
        print('draw confirmation for button2----', self.is_c1)
        if self.is_c1:
            self.confRec_c1 = self.w.create_rectangle(self.circleMX - self.radius + self.middleX - 30, self.circleMY -
                                                      self.radius - 20, self.circleMX + self.radius + self.middleX + 30,
                                                      self.circleMY + self.radius + 20, outline='red', width = 5)


        else:
            self.confRec_c2 = self.w.create_rectangle(self.circleMX - self.radius - 30,
                                                      self.circleMY - self.radius - 20,
                                                      self.circleMX + self.radius + 30,
                                                      self.circleMY + self.radius + 20,
                                                      outline='red', width = 5)


    def displayColor(self): ##c1 is when circle 1 is 50/50 gamble##
        if self.is_c1:

        # coloring: in pure gain, certainty uses navajo white, small=light sea green, large=tomato#
            if self.q[self.q_index].algorithmIndex is 1:

                self.w.itemconfigure(self.arc_c1_Small, state='normal', fill='light sea green')
                self.w.itemconfigure(self.arc_c1_Large, state='normal', fill='tomato')
                self.w.itemconfigure(self.arc_c2_Small, state='normal', fill='navajo white')
                self.w.itemconfigure(self.arc_c2_Large, state='normal', fill='navajo white')

        # coloring: in pure loss, certainty uses navajo white, small=deepSkyBlue3, large=firebrick3#
            elif self.q[self.q_index].algorithmIndex is 2:
                self.w.itemconfigure(self.arc_c1_Small, state='normal', fill='deepSkyBlue3')
                self.w.itemconfigure(self.arc_c1_Large, state='normal', fill='firebrick3')
                self.w.itemconfigure(self.arc_c2_Small, state='normal', fill='navajo white')
                self.w.itemconfigure(self.arc_c2_Large, state='normal', fill='navajo white')
        # coloring: in mixed, certainty uses navajo white, win=sky blue, loss=dodger blue#
            else:
                self.w.itemconfigure(self.arc_c1_Small, state='normal', fill='dodger blue')
                self.w.itemconfigure(self.arc_c1_Large, state='normal', fill='sky blue')
                self.w.itemconfigure(self.arc_c2_Small, state='normal', fill='navajo white')
                self.w.itemconfigure(self.arc_c2_Large, state='normal', fill='navajo white')


        else:
            if self.q[self.q_index].algorithmIndex is 1:
                self.w.itemconfigure(self.arc_c2_Small, state='normal', fill='light sea green')
                self.w.itemconfigure(self.arc_c2_Large, state='normal', fill='tomato')
                self.w.itemconfigure(self.arc_c1_Small, state='normal', fill='navajo white')
                self.w.itemconfigure(self.arc_c1_Large, state='normal', fill='navajo white')

        # coloring: in pure loss, certainty uses navajo white, small=deepSkyBlue3, large=firebrick3#
            elif self.q[self.q_index].algorithmIndex is 2:
                self.w.itemconfigure(self.arc_c2_Small, state='normal', fill='deepSkyBlue3')
                self.w.itemconfigure(self.arc_c2_Large, state='normal', fill='firebrick3')
                self.w.itemconfigure(self.arc_c1_Small, state='normal', fill='navajo white')
                self.w.itemconfigure(self.arc_c1_Large, state='normal', fill='navajo white')

        # coloring: in mixed, certainty uses navajo white, win=sky blue, loss=dodger blue#
            else:
                self.w.itemconfigure(self.arc_c2_Small, state='normal', fill='dodger blue')
                self.w.itemconfigure(self.arc_c2_Large, state='normal', fill='sky blue')
                self.w.itemconfigure(self.arc_c1_Small, state='normal', fill='navajo white')
                self.w.itemconfigure(self.arc_c1_Large, state='normal', fill='navajo white')


    # display pictures
    def showResult(self):
        self.w.itemconfigure(self.confRec_c1, state='hidden')
        self.w.itemconfigure(self.confRec_c2, state='hidden')
        self.w.itemconfigure(self.questionCoverBlock, fill='white')


    #hide pictures
    def clearResult(self):
        self.w.itemconfigure(self.questionCoverBlock, fill='')
        self.displayQuestion()


class App1(Welcome, question):

    label_50_1_c1 = None
    label_50_2_c1 = None
    label_100_c1 = None
    label_50_1_c2 = None
    label_50_2_c2 = None
    label_100_c2 = None
    label_image = None
    line_c1 = None
    line_c2 = None
    cue_effect = None
    win1_image = None
    win2_image = None
    win3_image = None
    win4_image = None
    win5_image = None
    loss1_image = None
    loss2_image = None
    loss3_image = None
    loss4_image = None
    loss5_image = None
    loss_sound = None
    win_sound = None
    bindid = None
    rebind = None
    bind_id_a = None
    bind_id_l= None
    start_time = None
    end_time = None
    human_choice = None

    computer_choice_label = None
    is_c1 = True
    questionCoverBlock = None
    imDisplay = None
    image = None
    value = None
    w = None
    canvas_width=None
    canvas_height=None
    middleX = None
    circleMX = None
    middleY = None
    circleMY = middleY
    radius = None
    confRec_c1 = None
    confRec_c2 = None
    master = None
    radius = 200

    csv_name_sub = None
    csv_name_ses = None


    #q_index: there are 5 pairs of questions for each pure gains and pure losses, the q_index represents each pair. Each pair repeats for once#
    q = []
    q_index = None
    clicked = []
    computerChoice = []
    isPure = True
    isMixed1 = True
    shouldShowQuestion = True
    button1 = None
    button2 = None
    choiceA = None
    choiceB = None
    buttonNext=None
    ButtonQuit=None
    questionNumber = 6
    limit = 6
    finishedQuestionQty = 1   #how many questions are finished currently#
    elapsed_time = None
    step = 2 # how many number in gain range/loss range for matrix
#for loop, repeat the equatio

    mid_gain_list = []
    mid_loss_list = []

    start_gain = None  # mixed matrix starting point
    start_loss = None
    end_gain = None  # mixed matrix end point
    end_loss = None
    matrixCount = None  # all cells in the matrix
    min_gain = None  # smallest gain in the median pure gain ls
    min_loss = None  # smallest loss in the median pure loss ls
    max_gain = None  # largest gain in the median pure gain ls
    max_loss = None  # largest loss in the median pure loss ls

    list_gain_matrix = []  # list of gain numbers in matrix
    list_loss_matrix = []
    v_50_1_matrix_history = []
    v_50_2_matrix_history = []
    matrix = []


    def __init__(self, master, csv_name_ses, csv_name_sub, algorithmIndex, initX, mid_loss_list, mid_gain_list):
        Welcome.__init__(self, master, csv_name_ses, csv_name_sub)
        self.csv_name_sub = Welcome.csv_name_sub
        self.csv_name_ses = Welcome.csv_name_ses
        print('session in matrix 1 is', self.csv_name_ses)
        print("subject in matrix 1 is", self.csv_name_sub)
        self.mid_gain_list = question.mid_gain_list
        self.mid_loss_list = question.mid_loss_list
        print('mid gain list in matrix is ', self.mid_gain_list, 'mid loss list in matrix is ', self.mid_loss_list)

        self.resultFile = open("/Users/kezhang/Desktop/Luck_LossAversion_v2/Results/results_matrix/without_outcome_matrix/" + self.csv_name_sub
                               + '_' + self.csv_name_ses + '_outcome_matrix_results.csv', 'w')
        self.resultFileWrite = csv.writer(self.resultFile)
        self.resultFileWrite.writerow(
            ['trial','v_50_1', 'v_50_2', 'v_100', 'subject choice', 'computer choice', 'rt(ms)'])

        self.master = master
        self.master.title('Task')
        self.canvas_width, self.canvas_height = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (self.canvas_width, self.canvas_height))
        self.master.wm_attributes('-fullscreen', True)

        self.w = Canvas(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        self.w.pack()
        self.w.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.middleX = self.canvas_width / 2
        self.circleMX = self.middleX / 2
        self.middleY = self.canvas_height / 2
        self.circleMY = self.middleY
        radius = 200

        print('initialize mixed question start ========================================')

        # init question is the medium, specify v_50_1 and v_50_2 at init
        # construct matrix list
        self.min_gain = min(self.mid_gain_list)
        self.max_gain = max(self.mid_gain_list)
        self.min_loss = min(self.mid_loss_list)
        self.max_loss = max(self.mid_loss_list)
        print('min gain is ', self.min_gain, 'max gain is ', self.max_gain, 'min loss is ', self.min_loss,
              'max loss is ', self.max_loss)

        if self.min_gain > 3:
            self.start_gain = self.min_gain - 3
        else:
            self.start_gain = self.min_gain

        if self.max_loss >= -3:
            self.start_loss = self.max_loss
        else:
            self.start_loss = self.max_loss + 3

        self.end_gain = self.max_gain + 3
        self.end_loss = self.min_loss - 3
        print('gain matrix starts at ', self.start_gain, 'gain matrix ends at ', self.end_gain,
              'loss matrix loss starts at ', self.start_loss, 'loss matrix ends at ', self.end_loss)

        self.list_gain_matrix = numpy.linspace(self.start_gain, self.end_gain, self.step).round(2)
        self.list_loss_matrix = numpy.linspace(self.start_loss, self.end_loss, self.step).round(2)
        print('full list gain before shuffle and select ', self.list_gain_matrix,
              'full list loss before shuffle and select ', self.list_loss_matrix)

        # create the matrix for each question
        for i in self.list_gain_matrix:
            for j in self.list_loss_matrix:
                self.matrix.append([i, j])
        random.shuffle(self.matrix)
        self.matrixCount = len(self.matrix)
        print('matrix list initial is ', self.matrix)
        print('how many pairs in matrix init ', self.matrixCount)

        self.v_100 = 0
        self.v_50_1 = self.matrix[0].pop(0)
        self.v_50_2 = self.matrix[0].pop(0)

        self.v_50_1_matrix_history.append(self.v_50_1)
        self.v_50_2_matrix_history.append(self.v_50_2)

        self.matrix.pop(0)
        self.matrixCount = len(self.matrix)

        print('init mixed matrix v_50_1 is ', self.v_50_1, 'init mixed matrix v_50_2 is ', self.v_50_2)
        print('matrix after pop is ', self.matrix)
        print('v_50_1 matrix history ', self.v_50_1_matrix_history,
              'v_50_2 matrix history', self.v_50_2_matrix_history)
        print('current pairs in matrix list ', self.matrixCount)

        #graphs#
        self.c1 = self.w.create_oval(self.circleMX-radius, self.circleMY-radius, self.circleMX+radius, self.circleMY+radius)
        self.c2 = self.w.create_oval(self.circleMX - radius +  self.middleX, self.circleMY - radius,
                                     self.circleMX + radius + self.middleX, self.circleMY + radius)

        # coloring: in pure gain, certainty uses navajo white, small=light sea green, large=tomato#
        #Small is the half circle at the left#
        self.arc_c1_Small = self.w.create_arc(self.circleMX - radius, self.circleMY - radius, self.circleMX + radius,
                                                  self.circleMY + radius, start=90,
                                                  extent=180, state='hidden', outline='')
        self.arc_c1_Large = self.w.create_arc(self.circleMX - radius, self.circleMY - radius, self.circleMX + radius,
                                                  self.circleMY + radius, start=270,
                                                  extent=180, state='hidden', outline='')
        self.arc_c2_Small = self.w.create_arc(self.circleMX - radius + self.middleX, self.circleMY - radius,
                                                  self.circleMX + radius + self.middleX, self.circleMY + radius,
                                                  start=90, extent=180, state='hidden', outline='')
        self.arc_c2_Large = self.w.create_arc(self.circleMX - radius + self.middleX, self.circleMY - radius,
                                                  self.circleMX + radius + self.middleX, self.circleMY + radius,
                                                  start=270, extent=180, state='hidden', outline='')


        self.choiceA = self.master.bind('z', self.run1)
        self.choiceB = self.master.bind('m', self.run2)

#attach labels on windows, and labels' locations. _c2 means the second circle, _c1 means the first circle#

        self.label_50_1_c1 = self.w.create_text(self.circleMX - 110, self.circleMY, text="$" + str(self.v_50_1), font="Helvetica 48")
        self.label_50_2_c1 = self.w.create_text(self.circleMX+110, self.circleMY, text="$" + str(self.v_50_2), font="Helvetica 48")
        self.label_100_c2 = self.w.create_text(self.circleMX+self.middleX, self.circleMY, text="$" + str(self.v_100),
                                               font="Helvetica 48")

# randomize for labels' locations: _c2 means the second circle, _c1 means the first circle#
        self.label_50_1_c2 = self.w.create_text(self.middleX + self.circleMX - 110, self.circleMY,text="$" + str(self.v_50_1), font="Helvetica 48")
        self.label_50_2_c2 = self.w.create_text(self.middleX + self.circleMX + 110, self.circleMY,text="$" + str(self.v_50_2), font="Helvetica 48")
        self.label_100_c1 = self.w.create_text(self.circleMX, self.circleMY, text="$" + str(self.v_100), font="Helvetica 48")

        self.computer_choice_label = Label(self.w, text='', fg='black')
        self.computer_choice_label.pack()
        self.w.create_window(600, 50, window=self.computer_choice_label)

        self.line_c1 = self.w.create_line(self.circleMX, self.circleMY - radius, self.circleMX, self.circleMY + radius)
        self.line_c2 = self.w.create_line(self.middleX + self.circleMX, self.circleMY - self.radius, self.middleX + self.circleMX,
                                          self.circleMY + radius)
        self.questionCoverBlock = self.w.create_rectangle(0, self.canvas_height, self.canvas_width, 50, outline= "white", fill="")

        self.randomize()
        self.displayOneSide()
        self.displayColor()
        self.start_time = time.time()
        print('start time is at initial ', self.start_time)


    def rebind_a(self):
        self.choiceA = self.master.bind("<a>", self.run1)
        print("rebinding A on")

    def rebind_l(self):
        self.choiceB = self.master.bind("<l>", self.run2)
        print('rebinding L on')

    # button run1:how do numbers change#
    def run1(self, event=None):
        self.draw_confirmation_button1()
        t = Timer(1, self.run1_s2)
        t.start()
        self.master.unbind("<m>", self.choiceB)
        self.master.unbind("<z>", self.choiceA)
        self.master.after(3000, self.rebind_a)
        #self.end_time = time.clock()
        self.end_time = time.time()
        print( "end time in run 1 is ", self.end_time)
        self.elapsed_time = (self.end_time - self.start_time) * 1000
        print('reaction time in run 1 is ', self.elapsed_time)
        return

    def run1_s2(self):
    #Choice A is 50/50 gamble, Choice B is the certainty.#
        self.clickPreProcess(False)
        self.get_question_mixedMatrix()
        self.clickPostProcess()

    # button run2: how do numbers change#
    def run2(self, event=None):
        self.draw_confirmation_button2()
        t = Timer(1, self.run2_s2)
        t.start()
        self.master.unbind("<m>", self.choiceB)
        self.master.unbind("<z>", self.choiceA)
        self.master.after(3000, self.rebind_l)
        #self.end_time = time.clock()
        self.end_time = time.time()
        print("end time in run 2 is ", self.end_time)
        self.elapsed_time = (self.end_time - self.start_time) * 1000
        print('reaction time in run 2 is ', self.elapsed_time)
        return


    def run2_s2(self):
        self.clickPreProcess(True) #show results
        self.get_question_mixedMatrix()
        self.clickPostProcess() #determine what is the next question


    def clickPreProcess(self, human_choice):
        self.computerChoose(human_choice)
        self.showResult()

    def clickPostProcess(self):
        self.finishedQuestionQty += 1
        print('now current question count is ', self.finishedQuestionQty)
        # if self.finishedQuestionQty == self.step*self.step:
        #     b = messagebox.showinfo('Task', 'Done.')
        t = Timer(2, self.clearResult)
        t.start()

    def get_question_mixedMatrix(self):

        print('matrix after init is ', self.matrix)
        self.v_50_1 = self.matrix[0].pop(0)
        self.v_50_2 = self.matrix[0].pop(0)

        self.v_50_1_matrix_history.append(self.v_50_1)
        self.v_50_2_matrix_history.append(self.v_50_2)

        self.matrix.pop(0)
        self.matrixCount = len(self.matrix)
        print('v_50_1 is ', self.v_50_1, 'v_50_2 is ', self.v_50_2)
        print('v_50_1 matrix history ', self.v_50_1_matrix_history,
               'v_50_2 matrix history ', self.v_50_2_matrix_history)
        print('how many questions left ', self.matrixCount)

        # if len(self.matrix) == 0:
        #     b = messagebox.showinfo('Task', 'Done.')
        #     # if messagebox.askyesno('Task', 'Done. Quit?'):
            #     print('msgbo')
            #     self.master.destroy()


    def displayQuestion(self):
        print("displaying question count ", self.finishedQuestionQty, " with values ",
              self.v_50_1,self.v_50_2,self.v_100)
        self.w.itemconfigure(self.label_100_c1, text= "$" + str(round(self.v_100, 2)))
        self.w.itemconfigure(self.label_100_c2, text= "$" + str(round(self.v_100, 2)))
        self.w.itemconfigure(self.label_50_1_c1, text= "$" + str(round(self.v_50_1, 2)))
        self.w.itemconfigure(self.label_50_2_c1, text= "$" + str(round(self.v_50_2, 2)))
        self.w.itemconfigure(self.label_50_1_c2, text= "$" + str(round(self.v_50_1, 2)))
        self.w.itemconfigure(self.label_50_2_c2, text= "$" + str(round(self.v_50_2, 2)))

        self.randomize()
        self.displayOneSide()
        self.displayColor()

        #self.start_time = time.clock()
        self.start_time = time.time()
        print('start time is at displayQuestion', self.start_time)
        return

    # computer generates a win number#

    def computerChoose(self, human_choice):
        if human_choice is True: ## human choice is B, 100%##
            print('current question is ', self.v_50_1, self.v_50_2, self.v_100)
            print('human choose + Choice B')
            self.value = round(self.v_100, 2)

            self.resultFileWrite.writerow(
                [self.finishedQuestionQty, str(self.v_50_1), str(self.v_50_2), str(self.v_100),
                 str(human_choice), str(self.value), self.elapsed_time])
            self.resultFile.flush()

            print('results', str(self.v_50_1), str(self.v_50_2), str(self.v_100),
                 str(human_choice), str(self.value), self.elapsed_time)

            return

        ## following is human choice is A, 50/50

        index = random.randrange(0, 2, 1)
        print('human choose + Choice A')
        if index == 0:
            #self.computerChoice[self.q_index].append(True)
            index2 = random.randrange(0, 2, 1)
            if index2 == 0:
                self.value = round(self.v_50_1, 2)
            else:
                self.value = round(self.v_50_2, 2)

            self.resultFileWrite.writerow(
                [str(self.finishedQuestionQty), str(self.v_50_1), str(self.v_50_2),
                 str(self.v_100),
                 str(human_choice), str(self.value), self.elapsed_time])
            self.resultFile.flush()

        else:
            #self.computerChoice[self.q_index].append(False)
            index2 = random.randrange(0, 2, 1)
            if index2 == 0:
                self.value = round(self.v_50_1, 2)
            else:
                self.value = round(self.v_50_2, 2)

            self.resultFileWrite.writerow(
                [str(self.finishedQuestionQty), str(self.v_50_1), str(self.v_50_2),
                 str(self.v_100),
                 str(human_choice), str(self.value), self.elapsed_time])
            self.resultFile.flush()

    def randomize(self):
        num = random.random()
        if num < 0.4:
            self.is_c1 = not self.is_c1
        print('randomize ----', self.is_c1)


    def displayOneSide(self):
        if self.is_c1:
            self.w.itemconfigure(self.line_c2, state='hidden')
            self.w.itemconfigure(self.line_c1, state='normal')

            self.w.itemconfigure(self.label_50_1_c1, state='normal')
            self.w.itemconfigure(self.label_50_2_c1, state='normal')
            self.w.itemconfigure(self.label_100_c2, state='normal')

            self.w.itemconfigure(self.label_100_c1, state='hidden')
            self.w.itemconfigure(self.label_50_1_c2, state='hidden')
            self.w.itemconfigure(self.label_50_2_c2, state='hidden')

        else:
            self.w.itemconfigure(self.line_c1, state='hidden')
            self.w.itemconfigure(self.line_c2, state='normal')

            self.w.itemconfigure(self.label_50_1_c2, state='normal')
            self.w.itemconfigure(self.label_50_2_c2, state='normal')
            self.w.itemconfigure(self.label_100_c1, state='normal')

            self.w.itemconfigure(self.label_100_c2, state='hidden')
            self.w.itemconfigure(self.label_50_1_c1, state='hidden')
            self.w.itemconfigure(self.label_50_2_c1, state='hidden')


        self.buttonRandom()


    def buttonRandom(self):
        if self.is_c1:
            self.choiceA = self.master.bind('z', self.run1)
            self.choiceB = self.master.bind('m', self.run2)
        else:
            self.choiceA = self.master.bind('z', self.run2)
            self.choiceB = self.master.bind('m', self.run1)


    def draw_confirmation_button1(self):
        #true, reverse; false, not reverse)
        print('draw confirmation for button1----', self.is_c1)
        if self.is_c1:
            self.confRec_c2 = self.w.create_rectangle(self.circleMX - self.radius - 30,
                                                      self.circleMY - self.radius - 20,
                                                      self.circleMX + self.radius + 30,
                                                      self.circleMY + self.radius + 20,
                                                      outline='red', width = 5)

        else:
            self.confRec_c1 = self.w.create_rectangle(self.circleMX - self.radius + self.middleX - 30, self.circleMY -
                                    self.radius - 20, self.circleMX + self.radius + self.middleX + 30,
                                    self.circleMY + self.radius + 20, outline = 'red', width = 5)


    def draw_confirmation_button2(self):
        #true, reverse; false, not reverse
        print('draw confirmation for button2----', self.is_c1)
        if self.is_c1:
            self.confRec_c1 = self.w.create_rectangle(self.circleMX - self.radius + self.middleX - 30, self.circleMY -
                                                      self.radius - 20, self.circleMX + self.radius + self.middleX + 30,
                                                      self.circleMY + self.radius + 20, outline='red', width = 5)


        else:
            self.confRec_c2 = self.w.create_rectangle(self.circleMX - self.radius - 30,
                                                      self.circleMY - self.radius - 20,
                                                      self.circleMX + self.radius + 30,
                                                      self.circleMY + self.radius + 20,
                                                      outline='red', width = 5)


    def displayColor(self): ##c1 is when circle 1 is 50/50 gamble##
        if self.is_c1:
                self.w.itemconfigure(self.arc_c1_Small, state='normal', fill='dodger blue')
                self.w.itemconfigure(self.arc_c1_Large, state='normal', fill='sky blue')
                self.w.itemconfigure(self.arc_c2_Small, state='normal', fill='navajo white')
                self.w.itemconfigure(self.arc_c2_Large, state='normal', fill='navajo white')


        else:
                self.w.itemconfigure(self.arc_c2_Small, state='normal', fill='dodger blue')
                self.w.itemconfigure(self.arc_c2_Large, state='normal', fill='sky blue')
                self.w.itemconfigure(self.arc_c1_Small, state='normal', fill='navajo white')
                self.w.itemconfigure(self.arc_c1_Large, state='normal', fill='navajo white')


    # display pictures
    def showResult(self):
        self.w.itemconfigure(self.confRec_c1, state='hidden')
        self.w.itemconfigure(self.confRec_c2, state='hidden')
        self.w.itemconfigure(self.questionCoverBlock, fill='white')



    #hide pictures
    def clearResult(self):
        self.w.itemconfigure(self.questionCoverBlock, fill='')
        self.displayQuestion()

def main():

    root = Tk()
    myApp = Welcome(root, csv_name_ses, csv_name_sub)
    root.mainloop()

if __name__ == '__main__':
    main()

