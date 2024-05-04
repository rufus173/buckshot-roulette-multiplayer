import tkinter
import socket
class gui():
    def __init__(self) -> None:#just gonna initialise the entire gui
        self.root = tkinter.Tk()
        self.player_1_frame = tkinter.LabelFrame(self.root,text="you",bg="grey") #for all intents and purposes you are always player 1
        self.player_1_frame.grid(row=0,column=2,columnspan=1,rowspan=1,sticky=tkinter.NSEW)
        self.root.columnconfigure(2,weight=1)
        self.player_1_items = {}
        for i in range(8):
            self.player_1_items[i] = tkinter.Button(self.player_1_frame,fg="grey")
        for i in range(4):
            self.player_1_items[i].grid(row=i,column=0,sticky=tkinter.NSEW,columnspan=1,rowspan=1)
        self.player_1_frame.columnconfigure(0,weight=1)
        for i in range(4):
            self.player_1_items[i+4].grid(row=i,column=1,sticky=tkinter.NSEW,columnspan=1,rowspan=1)
        self.player_1_frame.columnconfigure(1,weight=1)
        self.root.mainloop()
    def item_selected(self,item):
        pass
gui()