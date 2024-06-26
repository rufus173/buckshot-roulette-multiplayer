import tkinter
import socket
from tkinter import font
import threading
from tkinter import messagebox

#place the ip i give you into the string
ip = "86.160.112.140"

class gui():
    def __init__(self) -> None:#just gonna initialise the entire gui
        bg_1 = "#7d4e2d"
        bg_2 = "#426646"
        fg_1 = "grey"

        self.root = tkinter.Tk()
        self.root.title("buckshot roulette")
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
            self.player_1_items[i].grid(row=i+1,column=0,sticky=tkinter.NSEW,columnspan=1,rowspan=1)
        self.player_1_frame.columnconfigure(0,weight=1)
        for i in range(4):
            self.player_1_items[i+4].grid(row=i+1,column=1,sticky=tkinter.NSEW,columnspan=1,rowspan=1)
        self.player_1_frame.columnconfigure(1,weight=1)

        #creating player 2s item window
        self.player_2_frame = tkinter.LabelFrame(self.root,text="player 2",bg=bg_1)
        self.player_2_frame.grid(row=0,column=0,columnspan=1,rowspan=1,sticky=tkinter.NSEW)
        self.root.columnconfigure(0,weight=1)
        self.player_2_items = {}
        for i in range(8):
            self.player_2_items[i] = tkinter.Button(self.player_2_frame,fg=fg_1,bg=bg_2)
        for i in range(4):
            self.player_2_items[i].grid(row=i+1,column=0,sticky=tkinter.NSEW,columnspan=1,rowspan=1)
        self.player_2_frame.columnconfigure(0,weight=1)
        for i in range(4):
            self.player_2_items[i+4].grid(row=i+1,column=1,sticky=tkinter.NSEW,columnspan=1,rowspan=1)
        self.player_2_frame.columnconfigure(1,weight=1)

        #creating the shotgun window
        self.shotgun_frame = tkinter.LabelFrame(self.root,text="shotgun",bg=bg_1)
        self.shotgun_frame.grid(row=0,column=1,columnspan=1,rowspan=1,sticky=tkinter.NSEW)
        self.player_2_select = tkinter.Button(self.shotgun_frame,text="player 2",bg=bg_1)
        self.player_2_select.grid(row=0,column=0,columnspan=1,rowspan=1,sticky=tkinter.NSEW)
        self.player_1_select = tkinter.Button(self.shotgun_frame,text="yourself",bg=bg_1)
        self.player_1_select.grid(row=1,column=0,columnspan=1,rowspan=1,sticky=tkinter.NSEW)
        self.shotgun_frame.columnconfigure(0,weight=1)
        self.shotgun_frame.rowconfigure(0,weight=1)
        self.shotgun_frame.rowconfigure(1,weight=1)

        #creating the defibrilator charges
        self.player_2_defib = tkinter.Label(self.player_2_frame,text="⚡",bg="grey")
        self.player_2_defib.grid(row=0,column=0,columnspan=2,sticky=tkinter.NSEW)
        self.player_1_defib = tkinter.Label(self.player_1_frame,text="⚡",bg="grey")
        self.player_1_defib.grid(row=0,column=0,columnspan=2,sticky=tkinter.NSEW)

        #this is threading the socket connection
        self.root.mainloop()
    def item_selected(self,item):
        pass
class connection(gui):
    def __init__(self,ip) -> None:
        threading.Thread(target=super().__init__).start()
        self.server = socket.socket()
        self.server.connect((ip,8067))
        self.server.recv(1024)

        self.p1_lives = 0
        self.p2_lives = 0
        self.p1_item_list = []
        self.p2_item_list = []
        self.mainloop()
    def notify(self,msg):
        messagebox.showinfo(message=msg,title="info")
    def mainloop(self):
        while True:
            receive_buffer = self.server.recv(4096).decode()
            receive_buffer = receive_buffer.split(",")
            match receive_buffer[0]:
                case "lives": #p1[1] then p2[2]
                    self.p1_lives = int(receive_buffer[1])
                    print(receive_buffer)
                    self.p2_lives = int(receive_buffer[2])
                    print("updating lives",self.p1_lives,self.p2_lives)
                    self.player_1_defib["text"] = "⚡"*self.p1_lives
                    self.player_2_defib["text"] = "⚡"*self.p2_lives
                    self.server.sendall(b"_")
                case "p1 items":
                    self.p1_item_list = receive_buffer[1].split("~") #trust me this is easier
                    counter = 0
                    for i in self.p1_item_list:
                        self.player_1_items[counter]["text"] = i
                        counter += 1
                    self.server.sendall(b"_")
                case "p2 items":
                    self.p2_item_list = receive_buffer[1].split("~")
                    counter = 0
                    for i in self.p2_item_list:
                        self.player_2_items[counter]["text"] = i
                        counter += 1
                    self.server.sendall(b"_")
                case "notificaiton":
                    threading.Thread(target=lambda arg=receive_buffer[1]:self.notify(arg))
                    self.server.sendall((b"_"))
connection(ip)