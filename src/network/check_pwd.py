# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2021/07/05 16:43:26
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   a module for login
'''

import sys
import os
sys.path.append(os.path.abspath('./'))

from database.db import DB
from message.message_creator import login_message
import hashlib

def check_user(msg,db=None):
    if db==None:
        db=DB()

    if '@' in msg['name']:
        db.e("SELECT user_email,user_password from users where user_email='%s'"%msg['name'])
    else:
        db.e("SELECT user_name,user_password from users where user_name='%s'"%msg['name'])
    u=db.cur.fetchone()
    pwd=msg['password']

    if u==None:
        print("Warning: User not exist! please try again!")
    else:
        if u[1]==pwd:
            print("Success: you are login~")
        else:
            print("Error: Wrong password")

if __name__ == '__main__':
    db=DB()
    msg=login_message('123@qq.com','1234567')
    check_user(msg,db)