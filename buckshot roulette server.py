import socket
class main:
    def __init__(self) -> None:
        server = socket.socket()
        server.bind(("localhost",8067))