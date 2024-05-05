import socket
import time
class main:
    def __init__(self) -> None:
        server = socket.socket()
        server.bind(("192.168.1.239",8067))
        while True:
            time.sleep(5)
            try:
                print("opening socket for connections")
                server.listen(2)
                con1, address = server.accept()
                print("connection 1 found")
                con2,address = server.accept()
                print("connection 2 found")
                con1.sendall(b"_")
                con2.sendall(b"_")
            except Exception as problem:
                print(problem)
                try:
                    con1.shutdown(socket.SHUT_RDWR)
                    con2.shutdown(socket.SHUT_RDWR)
                except:
                    print("socket could not be shut down")

                        
            
            try:
                con1.shutdown(socket.SHUT_RDWR)
                con2.shutdown(socket.SHUT_RDWR)
                print("closed the sockets")
            except Exception as problem:
                print(problem,"when trying to exit")

main()
