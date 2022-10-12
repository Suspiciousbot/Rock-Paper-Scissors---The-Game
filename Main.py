from PIL import ImageTk
import PIL.Image
import random
from tkinter import *
import sys

root = Tk()

root.title("RPS-The Game V4")
root.iconbitmap("logoinem.ico")

root.minsize(1366,780)
root.maxsize(1366,780)

tl = 10

def fs1():
    oldimg.destroy()
    newimg.place(x=0, y=0, anchor="nw")
    newimg.after(5000,fs2)

def fs2():
    newimg.destroy()
    otherimg.pack(anchor="center",fill= Y)
    otherimg.after(5000, g_main_m_func)

def startbym (event):
    sf.destroy()
    playgame()

def quitbykb (event):
    if event.char == "q":
        exit()

def startbykb (event):
    if event.char == "s":
        sf.destroy()
        playgame()

def g_main_m_func():
    otherimg.destroy()

    mml.place(x=0, y=0)

    global sf
    sf = Frame(root, bg= "black")
    sf.place(x=1010, y=350, anchor=CENTER)

    startbut = Button(sf, text= "Start", borderwidth=0, font=("Bahnschrift", 110, "bold"), bg= "green", fg= "yellow", activebackground="yellow", activeforeground= "green")
    startbut.bind("<Button-1>", startbym)
    startbut.bind("<Key>", startbykb)

    def close():
        exit()

    qbut = Button(sf, text= "Quit", borderwidth=0,command= close, font= ("Bahnschrift", 110, "bold"), bg="red" ,fg="orange", activebackground="orange", activeforeground= "red")
    qbut.bind("<Key>", quitbykb)

    startbut.grid(row= 0, column= 0, padx= 7, pady= 10)
    qbut.grid(row= 1, column= 0, padx= 7, pady= 10)

def playgame():

    mml2 = Label(root, image= mm2)
    mml2.place(x=0, y=0)

    def submit_N_R():
        un = user_name.get()

        try:
            nr = no_rounds.get()
            nr = int(nr)
            print (type(nr))
        except Exception as e:
            NR_E_La = Label(text= "Error: Please enter the number of ronuds in integer", fg= "red", bg= "black")
            NR_E_La.pack(side=BOTTOM, anchor= "sw")
            def dest_nr ():
                NR_E_La.destroy()
            NR_E_La.after(3000, dest_nr)

        if un == "":
            def dest_n ():
                Name_E_L.destroy()
            Name_E_L = Label(text="Error: Please enter the username", fg= "red", bg= "black")
            Name_E_L.pack(side=BOTTOM, anchor= "sw")
            Name_E_L.after(3000, dest_n)
        if nr == 0 or nr == None:
            def dest_r ():
                NR_E_l.destroy()
            NR_E_l = Label(text= "Error: Please entetr the number of ronuds in integer other than 0", fg= "red",bg= "black")
            NR_E_l.pack(side=BOTTOM, anchor= "sw")
            NR_E_l.after(3000, dest_r)
        if un != "" and un != None and nr != 0 and nr != None and type(nr) == int:
            print (un)
            print (nr)
            ent_meun_fr.destroy()
            Ent_N.destroy()
            userentry.destroy()
            Ent_Round.destroy()
            roundentry.destroy()
            mml2.destroy()

            M_g_Canva = Canvas(root, width= 1366, height= 780, bg= "black")
            M_g_Canva.pack()
            M_g_Canva.create_image(0,0, image= melo, anchor= "nw")
            M_g_Canva.create_text(733, 75, text="Chose one of these:", font= ("copperplategothic", 30, "bold"), fill= "blue")

            OptFrm = Frame(bg= "black")
            OptFrm.place(x= 400, y=130)
            
            M_g_Canva.create_line(0, 382, 1366, 382, fill= "green")

            ResultFrm = Frame(bg= "red")
            ResultFrm.place(x=683, y=542,anchor= CENTER)
            
            RoundnumL = Label(ResultFrm, fg= "blue", bg="red", font=("", 29, "normal"))
            RoundnumL.grid(row= 0, column= 0)
            YoChoiceL = Label(ResultFrm, fg= "blue", bg="red", font=("", 29, "normal"))
            YoChoiceL.grid(row= 1, column= 0)
            CompChoiceL = Label(ResultFrm, fg= "blue", bg="red", font=("", 29, "normal"))
            CompChoiceL.grid(row= 2, column= 0)
            RWinOrLossL = Label(ResultFrm, fg= "blue", bg="red", font=("", 29, "normal"))
            RWinOrLossL.grid(row= 3, column= 0)
            PlScoreL= Label(ResultFrm, fg= "blue", bg="red", font=("", 29, "normal"))
            PlScoreL.grid(row= 4, column= 0)
            CoScoreL= Label(ResultFrm, fg= "blue", bg="red", font=("", 29, "normal"))
            CoScoreL.grid(row= 5, column= 0)

            def gameResultDescition (you,compu):
                if you == "r":
                    if compu == "p":
                        a = False
                        return a
                    elif compu == "s":
                        a = True
                        return a
                elif you == "p":
                    if compu == "s":
                        a = False
                        return a
                    elif compu == "r":
                        a = True
                        return a
                elif you == "s":
                    if compu == "r":
                        a = False
                        return a
                    elif compu == "p":
                        a = True
                        return a
                else:
                    a = None
                    return a

            youu = StringVar()
            Comp_score = 0
            Your_score = 0

            def rocopt():
                youu.set("r")
            def papeopt():
                youu.set("p")
            def sicssopt():
                youu.set("s")
            
            RockOpt = Button(OptFrm, image= Roc, borderwidth=0, command= rocopt)
            PaperOpt = Button(OptFrm, image= pap, borderwidth=0, command=papeopt)
            SicssorOpt = Button(OptFrm, image= sic, borderwidth=0, command= sicssopt)


            for r in range(nr):
                RandomNo =  random.randint(1,3)

                if RandomNo == 1:
                    compu = "r"
                elif RandomNo == 2:
                    compu = "p"
                elif RandomNo == 3:
                    compu = "s"

                RockOpt.grid(column=0, row=0, padx= 15, pady= 10)
                PaperOpt.grid(column=1, row=0, padx= 15, pady= 10)
                SicssorOpt.grid(column=2, row=0, padx= 15, pady= 10)

                SicssorOpt.wait_variable(youu)

                a = gameResultDescition(youu.get(), compu)
                if a == True:
                    Your_score += 1
                    YoChoiceL.config(text= f"{un}'s choice: {youu.get()}")
                    CompChoiceL.config(text= f"Computer's choice: {compu}")
                    RWinOrLossL.config(text= f"{un} Won this round!")
                    PlScoreL.config(text= f"{un}'s score: {Your_score}")
                    CoScoreL.config(text= f"Computer's scoer: {Comp_score}")

                elif a == False:
                    Comp_score += 1
                    YoChoiceL.config(text= f"{un}'s choice: {youu.get()}")
                    CompChoiceL.config(text= f"Computer's choice: {compu}")
                    RWinOrLossL.config(text= "Computer won this round!")
                    PlScoreL.config(text= f"{un}'s score: {Your_score}")
                    CoScoreL.config(text= f"Computer's scoer: {Comp_score}")

                elif a == None:
                    RWinOrLossL.config(text= "This round tied!")
                    YoChoiceL.config(text= f"{un}'s choice: {youu.get()}")
                    CompChoiceL.config(text= f"Computer's choice: {compu}")
                    PlScoreL.config(text= f"{un}'s score: {Your_score}")
                    CoScoreL.config(text= f"Computer's scoer: {Comp_score}")

                RoundnumL.config(text=f"Result of round: {r+1}")
                if r+1 == nr:

                    RoundnumL.config(text=f"Result of round: {r+1} (The Last Round)")
                    tlf = Frame(bg= "black")
                    tlf.place(x=1255, y= 677, anchor= CENTER)
                    F_T_Le_La = Label(tlf, text= "", font= ("", 18, "bold"), fg= "red", bg= "black")
                    F_T_Le_La.pack()
                    def finalResult ():
                        def tlc ():
                            global tl
                            F_T_Le_La.config(text= f"Final result in {str(tl)}")
                            tl-=1
                            F_T_Le_La.after(1000, tlc)
                            if tl == -2:
                                final_result(Comp_score, Your_score, un)
                        tlc()
                        
                    def final_result (score1, score2, Player_Name):
                        tlf.destroy()
                        RockOpt.destroy()
                        PaperOpt.destroy()
                        SicssorOpt.destroy()
                        M_g_Canva.destroy()
                        ResultFrm.destroy()
                        OptFrm.destroy()
                        fr_canvas = Canvas(width=1366, height=780, bg="black")
                        fr_canvas.pack()

                        if score1 == score2:
                            fr_canvas.create_rectangle(50, 50, 1316, 540, fill= "blue")
                            fr_canvas.create_text (683, 120, text= f"Computer's Score = {Comp_score}", font= ("", 60, "bold"), fill= "black")
                            fr_canvas.create_text (683, 270,text= f"Your's Score = {Your_score}", font= ("", 60, "bold"), fill= "black")
                            fr_canvas.create_text (683, 420,text= "The game tied", font= ("", 60, "bold"), fill= "black")

                        elif score1 < score2:
                            fr_canvas.create_rectangle(50, 50, 1316, 540, fill= "green")
                            fr_canvas.create_text (683, 120, text= f"Computer's Score = {Comp_score}", font= ("", 60, "bold"), fill= "yellow")
                            fr_canvas.create_text (683, 270,text= f"Your's Score = {Your_score}", font= ("", 60, "bold"), fill= "yellow")
                            fr_canvas.create_text (683, 420,text= f"GG! {Player_Name} defated the computer!", font= ("", 50, "bold"), fill= "yellow")

                        elif score1 > score2:
                            fr_canvas.create_rectangle(50, 50, 1316, 540, fill= "orange")
                            fr_canvas.create_text (683, 120, text= f"Computer's Score = {Comp_score}", font= ("", 60, "bold"), fill= "red")
                            fr_canvas.create_text (683, 270,text= f"Your's Score = {Your_score}", font= ("", 60, "bold"), fill= "red")
                            fr_canvas.create_text (683, 420,text= f"Better Luck Next Time {Player_Name},\n Computer won the game!", font= ("", 40, "bold"), fill= "red")

                        def Show_creadits():
                            Credits = Tk()
                            Credits.geometry("600x350")
                            Credits.title("RPS-The Game V4 Creadits")
                            Credits.iconbitmap("logoinem.ico")
                            Cr_canvas = Canvas(Credits,width= 600, height= 350, bg= "black")
                            Cr_canvas.pack()
                            Cr_canvas.create_text(300, 40, text= "Creadits", font= ("", 30, "bold"), anchor= CENTER, fill= "green")
                            Cr_canvas.create_text(300, 175,text= "Developer  ---  SUSPICIOUSBOT\n\nDesigner  ---  SUSPICIOUSBOT\n\n\n\n  GitHub Id - Suspiciousbot",font= ("", 20, "bold"), anchor= CENTER, fill= "green")
                            Credits.mainloop()

                        def new_game(event):
                            global tl
                            tl= 10
                            playgame()
                            fr_canvas.destroy()

                        def next_buttons():
                            Final_opt_fr = Frame(bg= "black")
                            Final_opt_fr.place(x= 683, y= 620, anchor= CENTER)

                            rebut = Button(Final_opt_fr, text= "Restart", borderwidth= 0, font= ("Bahnschrift", 45, "bold"), bg="yellow" ,fg="gray", activebackground="gray", activeforeground= "yellow")
                            rebut.grid(row= 0, column= 0, padx= 90)
                            rebut.bind("<Button-1>", new_game)

                            cred = Button(Final_opt_fr, text= "Creadits", borderwidth= 0, command= Show_creadits, font= ("Bahnschrift", 45, "bold"), bg="blue" ,fg="green", activebackground="green", activeforeground= "blue")
                            cred.grid(row= 0,column= 2, padx= 90)

                            def close1():
                                sys.exit()

                            quitb = Button(Final_opt_fr, text= "Quit", borderwidth= 0, command= close1 , font= ("Bahnschrift", 45, "bold"), bg="red" ,fg="orange", activebackground="orange", activeforeground= "red")
                            quitb.grid(row= 0, column= 1, padx= 90)

                        fr_canvas.after(3000, next_buttons)

                    finalResult()

    ent_meun_fr = Frame(bg="black")
    ent_meun_fr.pack(side=RIGHT, padx= 30)

    Ent_N = Label(ent_meun_fr, text="Enter your name:", fg= "blue", bg="black", font= ("copperplategothic", 30, "bold"))
    Ent_N.pack(pady= 20, padx= 50, side= TOP)
    user_name = StringVar()
    userentry = Entry(ent_meun_fr, textvariable = user_name)
    userentry.pack(pady= 2, padx= 50)

    Ent_Round = Label(ent_meun_fr, text="Enter the number of rounds:", fg= "blue", bg="black", font= ("copperplate gothic", 30, "bold"))
    Ent_Round.pack(pady= 20, padx= 50)
    no_rounds = StringVar()
    roundentry = Entry(ent_meun_fr, textvariable = no_rounds)
    roundentry.pack(pady= 2, padx= 50)

    done1 = Button(ent_meun_fr, text= "Done", command= submit_N_R, borderwidth=0, font= ("", 50, "bold"), bg="green" ,fg="yellow", activebackground="yellow", activeforeground= "green")
    done1.pack(pady= 40, side= BOTTOM)

# Defining images
Sm2 = PIL.Image.open("main menu - Copy.png")
mm2 = ImageTk.PhotoImage(Sm2)

me = PIL.Image.open("logo in em.png")
melo = ImageTk.PhotoImage(me)

Rockimg= PIL.Image.open("Rock button.png")
Roc = ImageTk.PhotoImage(Rockimg)

Paperimg = PIL.Image.open("Paper button.png")
pap= ImageTk.PhotoImage(Paperimg)

Sicssorimg = PIL.Image.open("Sicssor button.png")
sic = ImageTk.PhotoImage(Sicssorimg)

Sm = PIL.Image.open("main menu.png")
mm = ImageTk.PhotoImage(Sm)
mml = Label(root, image= mm)

image1 = PIL.Image.open("Desclimer.png")
img1 = ImageTk.PhotoImage(image1)
oldimg = Label(root, image=img1)
oldimg.place(x=0, y=0, anchor="nw")

oldimg.after(5000,fs1)

image2 = PIL.Image.open("Studio.png")
img2 = ImageTk.PhotoImage(image2)
newimg = Label(root, image=img2)

image3 = PIL.Image.open("G Logo Gui.png")
img3 = ImageTk.PhotoImage(image3)
otherimg = Label(root, image=img3)

root.mainloop()
