from asyncio.windows_utils import BUFSIZE
import socket
from os import error
import threading
from unittest import result
from urllib import request
import json

from matplotlib.pyplot import close


HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    SERVER.bind((HOST,PORT))
    print(f'* Running on http://{HOST}:{PORT}')
except socket.error as e:
    print(f'socket error: {e}')
    print('socket error: %s' %(e))


def _start():
    SERVER.listen()
    while True:
        conn, addr = SERVER.accept()
        thread = threading.Thread(target=_handle, args=(conn, addr))
        thread.start()

def _handle(conn,addr):
    global request
    while conn:
        request = conn.recv(BUFSIZE).decode()
        if not request: conn.close()
        # conn.send(get_request('connect'))
        # print(get_request('connection'))
        conn.send(get_request('connection'))
        
        break

def get_request(key = None):
    request_without_body = request.split('\r\n\r\n')[0]
    body = request.split('\r\n\r\n')[1]
    request_array = []
    for x  in request_without_body.split('\r\n'):
        if x.strip():
            request_array.append(x)
            
    # print(request_array)
    print(request_without_body)

    # request_line = []
    # for x in request_array[0].split():
    #     request_line.append(x)
    # request_dict = dict(Method = request_line[0], Url = request_line[1], Protocol = request_line[2])
    # for x in request_array[1:]:
    #     data = x.split(':',1) 
    #     # request_dict.update({data[0]:data[1]})
    #     print(data)
    # if key is None: 
    #     result = request_dict
    # else:
    #     ket_value = (key.lower()).title()
    #     result = request_dict[ket_value]
    return b'aaaaa'

if __name__ == '__main__':
    _start()