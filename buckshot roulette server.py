import socket
import time
import random
class main:
    def __init__(self) -> None:
        server = socket.socket()
        server.bind(("192.168.1.239",8067))
        
        self.all_items = ["cigarettes","pills"]
        self.chamber = []

        while True:
            time.sleep(1)
            self.lives = 2 + random.randint(0,2)
            self.p1_lives = self.lives
            self.p2_lives = self.lives
            self.turn = 0
            self.p1_items = []
            self.p2_items = []
            try:
                print("opening socket for connections")
                server.listen(2)
                self.con1, address = server.accept()
                print("connection 1 found")
                self.con2,address = server.accept()
                print("connection 2 found")
                time.sleep(1)
                self.con1.sendall(b"_")
                self.con2.sendall(b"_")
            except Exception as problem:
                print(problem)
                try:
                    self.con1.shutdown(socket.SHUT_RDWR)
                    self.con2.shutdown(socket.SHUT_RDWR)
                except:
                    print("socket could not be shut down")
            self.mainloop()
            try:
                self.con1.shutdown(socket.SHUT_RDWR)
                self.con2.shutdown(socket.SHUT_RDWR)
                print("closed the sockets")
            except Exception as problem:
                print(problem,"when trying to exit")
    def mainloop(self):
        self.reload()
        while True:
            print("start of turn")
            self.turn += 1
            self.update_players()
            time.sleep(5)
    def update_players(self):#seperation with a comma
        self.con1.sendall(("lives,"+str(self.p1_lives)+","+str(self.p2_lives)).encode()) #i should be better but 1st is p1 lives then p2 lives
        self.con1.recv(1024)
        self.con2.sendall(("lives,"+str(self.p1_lives)+","+str(self.p2_lives)).encode())
        self.con2.recv(1024)
        p1itemstring = ""
        for i in self.p1_items:
            p1itemstring = p1itemstring + i + "~" #to make it easier to reconstruct on the client side
        p1itemstring = p1itemstring.rstrip("~")
        p2itemstring = ""
        for i in self.p2_items:
            p2itemstring = p2itemstring + i + "~"
        p2itemstring = p2itemstring.rstrip("~")
        self.con1.sendall(("p1 items"+","+p1itemstring).encode())
        self.con1.recv(1024)
        self.con2.sendall(("p1 items"+","+p1itemstring).encode())
        self.con2.recv(1024)
        self.con1.sendall(("p2 items"+","+p2itemstring).encode())
        self.con1.recv(1024)
        self.con2.sendall(("p2 items"+","+p2itemstring).encode())
        self.con2.recv(1024)
    def reload(self):
        for i in range(self.lives):
            self.p1_items.append(self.all_items[random.randint(0,len(self.all_items)-1)])
            self.p2_items.append(self.all_items[random.randint(0,len(self.all_items)-1)])
            if len(self.p1_items) > 8:
                self.p1_items = self.p1_items[:9]
            if len(self.p2_items) > 8:
                self.p2_items = self.p2_items[:9]
        self.chamber = ["blank","live"]
        for i in range(6):
            if random.randint(0,1) == 1:
                match random.randint(0,1):
                    case 0:
                        self.chamber.append("blank")
                    case 1:
                        self.chamber.append("live")
        random.shuffle(self.chamber)   
        print(self.chamber)       # the contents of the chamber stay with the server for safekeeping
main()
