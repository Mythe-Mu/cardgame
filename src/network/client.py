# -*- encoding: utf-8 -*-
'''
@File    :   client.py
@Time    :   2021/07/05 15:55:11
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   Client
'''


import socket,time,json,pickle
import os,sys
sys.path.append(os.path.abspath("./"))
print(sys.path)

from message.message_creator import create_message

class Client(object):
    def __init__(self,addr,port) -> None:
        super().__init__()
        self.addr=addr
        self.port=port
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def send(self,msg):
        self.s.connect((self.addr,self.port))
        self.s.send(msg)


if __name__ == '__main__':
    s=Client('localhost',55555)
    s.send('hello,world'.encode('utf-8'))

