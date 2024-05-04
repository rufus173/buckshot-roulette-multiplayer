import tkinter
import socket
from tkinter import font
class gui():
    def __init__(self) -> None:#just gonna initialise the entire gui
        bg_1 = "#7d4e2d"
        bg_2 = "#426646"
        fg_1 = "grey"

        self.root = tkinter.Tk()
        self.defaultFont = font.nametofont("TkDefaultFont") 
        self.defaultFont.configure(size=19,weight=font.BOLD) 
        self.player_1_frame = tkinter.LabelFrame(self.root,text="you",bg=bg_1) #for all intents and purposes you are always player 1
        self.player_1_frame.grid(row=0,column=2,columnspan=1,rowspan=1,sticky=tkinter.NSEW)
        self.root.columnconfigure(2,weight=1)

        #creating your item window
        self.player_1_items = {}
        for i in range(8):
            self.player_1_items[i] = tkinter.Button(self.player_1_frame,fg=fg_1,bg=bg_2)
        for i in range(4):
            self.player_1_items[i].grid(row=i,column=0,sticky=tkinter.NSEW,columnspan=1,rowspan=1)
        self.player_1_frame.columnconfigure(0,weight=1)
        for i in range(4):
            self.player_1_items[i+4].grid(row=i,column=1,sticky=tkinter.NSEW,columnspan=1,rowspan=1)
        self.player_1_frame.columnconfigure(1,weight=1)

        #creating player 2s item window
        self.player_2_frame = tkinter.LabelFrame(self.root,text="player 2",bg=bg_1)
        self.player_2_frame.grid(row=0,column=0,columnspan=1,rowspan=1,sticky=tkinter.NSEW)
        self.root.columnconfigure(0,weight=1)
        self.player_2_items = {}
        for i in range(8):
            self.player_2_items[i] = tkinter.Button(self.player_2_frame,fg=fg_1,bg=bg_2)
        for i in range(4):
            self.player_2_items[i].grid(row=i,column=0,sticky=tkinter.NSEW,columnspan=1,rowspan=1)
        self.player_2_frame.columnconfigure(0,weight=1)
        for i in range(4):
            self.player_2_items[i+4].grid(row=i,column=1,sticky=tkinter.NSEW,columnspan=1,rowspan=1)
        self.player_2_frame.columnconfigure(1,weight=1)

        #creating the shotgun window
        self.shotgun_frame = tkinter.LabelFrame(self.root,text="shotgun",bg=bg_1)
        self.shotgun_frame.grid(row=0,column=1,columnspan=1,rowspan=1,sticky=tkinter.NSEW)
        self.player_2_select = tkinter.Button(self.shotgun_frame,text="player 2",fg="grey")
        self.player_2_select.grid(row=0,column=0,columnspan=1,rowspan=1,sticky=tkinter.NSEW)
        self.player_1_select = tkinter.Button(self.shotgun_frame,text="yourself",fg="grey")
        self.player_1_select.grid(row=1,column=0,columnspan=1,rowspan=1,sticky=tkinter.NSEW)
        self.shotgun_frame.columnconfigure(0,weight=1)
        self.shotgun_frame.rowconfigure(0,weight=1)
        self.shotgun_frame.rowconfigure(1,weight=1)

        self.root.mainloop()
    def item_selected(self,item):
        pass
gui()
