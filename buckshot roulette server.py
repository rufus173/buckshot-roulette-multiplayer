import socket
import time
class main:
    def __init__(self) -> None:
        while True:
            time.sleep(5)
            try:
                print("opening socket for connections")
                server = socket.socket()
                server.bind(("192.168.1.239",8067))
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
                    server.close()
                    server.shutdown()
                except:
                    print("socket could not be shut down")

                        
            
            try:
                server.close()
                server.shutdown(socket.SHUT_RDWR)
            except:
                pass

main()
