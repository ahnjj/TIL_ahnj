from server import Server

if __name__ == '__main__':
    Server('localhost', 9898, 4096).start_server()