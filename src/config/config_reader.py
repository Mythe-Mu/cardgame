# -*- encoding: utf-8 -*-
'''
@File    :   config_reader.py
@Time    :   2021/07/05 20:51:28
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   A reader of config file.
'''

import sys
import os
sys.path.append(os.path.abspath('./'))

import configparser

class Configer(object):
    def __init__(self,path="./config/config.ini") -> None:
        super().__init__()
        self.path=path
        self.config=configparser.ConfigParser()
        self.config.read(path)


    def save_config(self):
        self.config.write(open(self.path),'w')

    def set_config(self,section,option,value):
        self.config.set(section,option,value)
        self.save_config()

    def add_section(self,section):
        self.config.add_section(section)
        self.save_config()

    def get_option(self,section,option):
        return self.config.get(section,option)

    def get_window_size(self):
        width,height=map(int,self.get_option("sys_config","window_size").split('x'))
        return width,height
        

if __name__ == '__main__':
    c=Configer()
    c.get_window_size()


