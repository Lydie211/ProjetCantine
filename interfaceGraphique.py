# coding: utf-8
 
from tkinter import * 
from controller import Controller
from interfaceVotes import InterfaceVotes
fenetre = Tk()
class ihm:

    def __init__(self):

        label = Label(fenetre, text='question')
        label.pack()    

        fenetre['bg']='white'

        # frame 1
        Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack(side=LEFT, padx=50, pady=30)
        Bouton = Button(Frame1, text="Beurk", height=4, width=9, background="red")
        Bouton.pack()

        Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack(side=LEFT, padx=50, pady=30)
        Bouton = Button(Frame1, text="Bof", height=4, width=9, background="orange")
        Bouton.pack()

        Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack(side=LEFT, padx=50, pady=30)
        Bouton = Button(Frame1, text="Bon", height=4, width=9, background="yellow")
        Bouton.pack()

        Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack(side=LEFT, padx=50, pady=30)
        Bouton = Button(Frame1, text="Délicieux", height=4, width=9, background="green")
        Bouton.pack()


        fenetre.mainloop()

fenetre = ihm()