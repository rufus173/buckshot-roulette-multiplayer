import socket
import time
import random
class main:
    def __init__(self) -> None:
        server = socket.socket()
        server.bind(("192.168.1.239",8067))
        while True:
            time.sleep(5)
            self.lives = 2 + random.randint(0,2)
            self.p1_lives,self.p2_lives = self.lives, self.lives
            self.turn = 0
            try:
                print("opening socket for connections")
                server.listen(2)
                self.con1, address = server.accept()
                print("connection 1 found")
                self.con2,address = server.accept()
                print("connection 2 found")
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
        while True:
            print("start of turn")
            self.turn += 1
            self.update_players()
            time.sleep(5)
    def update_players(self):#seperation with a comma
        self.con1.sendall("lives,"+str(self.p1_lives).encode())
main()
