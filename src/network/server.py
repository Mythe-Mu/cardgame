# -*- encoding: utf-8 -*-
'''
@File    :   server.py
@Time    :   2021/07/05 15:39:05
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   Server Module
'''

import socket,time,json,pickle
import os,sys
import threading
import multiprocessing

sys.path.append(os.path.abspath("./"))
print(sys.path)

from message.message_creator import create_message

class Server(object):
    def __init__(self,addr,port) -> None:
        super().__init__()
        self.addr=addr
        self.port=port
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind((self.addr,self.port))
        self.player_list=[]
        self.start=self.run

    def __len__(self):
        return len(self.player_list)

    def run(self):
        print("Server is running on : %s:%d"%(self.addr,self.port))
        self.s.listen(100)
        while True:
            conn=self.s.accept()
            print(conn)
            self.player_list.append(conn)

    


if __name__ == '__main__':
    s=Server('localhost',55555)
    s.run()

