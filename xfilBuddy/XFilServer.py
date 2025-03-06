class XFilServer():
    def __init__(self, address, port):
        self.address = address
        self.port = port

    def sayHello(self):
        print("Hello, I am XFilServer!")