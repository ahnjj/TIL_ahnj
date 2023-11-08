import socket


class Server:
    def __init__(self, port, req_size):
        self.__port = port
        self.__req_size = req_size

    def start_server(self):

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to a public host, and a well-known port
        serversocket.bind(('localhost', 9898))
        # become a server socket
        serversocket.listen(5)

        while True:
            (clientsocket, address) = serversocket.accept()
            print(address)
            req_msg = clientsocket.recv(self.__req_size)
            print(req_msg)
            req_msg = str(req_msg, encoding='utf-8')

            req_msg_lines = req_msg.splitlines()
            req_start_line = req_msg_lines[0]
            req_header = req_msg_lines[1:req_msg_lines.index('')]

            url = req_start_line[1]
            print(url)
            urls = {'/'         : self.index()
                    ,'/qr'      : QR.generate('https://www.naver.com')
                    ,'/favicon.ico' : ''.encode('utf-8')
                    }
            clientsocket.send('HTTP/1.1 200 ok \n\n'.encode('utf-8'))

            if clientsocket.sendall(urls.get(url)) is None:
                clientsocket.close()

    def index(self):
        return 'Hi! Index Page!'.encode('utf-8')

