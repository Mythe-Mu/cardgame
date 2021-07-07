# -*- encoding: utf-8 -*-
'''
@File    :   register.py
@Time    :   2021/07/05 16:59:45
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   A register file
'''

import sys
import os
sys.path.append(os.path.abspath('./'))
from message.message_creator import register_message

from database.db import DB
import hashlib

def create_player(msg,db=None):
    if db==None:
        db=DB()
    pwd=msg['password']
    
    sql="INSERT INTO users(user_id,user_name,user_password,timestamp) VALUES (NULL,'%s','%s',current_timestamp())"%(msg['name'],pwd)
    try:
        db.e(sql)
        db.db.commit()
        print("Registed successful!")
    except:
        print("Regist failed!")
    

if __name__ == '__main__':
    msg=register_message('tester3','hello')
    create_player(msg)