# -*- encoding: utf-8 -*-
'''
@File    :   message_creator.py
@Time    :   2021/07/05 15:43:58
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   Create Messages
'''
import hashlib,json,pickle

def create_message(msg=None):
    if msg==None:
        msg="hello,world!" 
    return {
        'type':'common',
        'content':msg
    }

def register_message(name,password,email,etype='md5',code='utf-8',encode=False):
    if etype=='md5':
        password=hashlib.md5(password.encode(code)).hexdigest()
    elif etype=='sha256':
        password=hashlib.sha256(password.encode(code)).hexdigest()
    msg={
        "type":"regist",
        "name":name,
        "password":password,
        "email":email
    }
    if encode==True:
        msg=pickle.dumps(msg,protocol=pickle.HIGHEST_PROTOCOL,fix_imports=True)
    return msg

def login_message(name,password,etype='md5',code='utf-8',encode=False):
    if etype=='md5':
        password=hashlib.md5(password.encode(code)).hexdigest()
    elif etype=='sha256':
        password=hashlib.sha256(password.encode(code)).hexdigest()
    msg={
        "type":"login",
        "name":name,
        "password":password
    }
    if encode==True:
        msg=pickle.dumps(msg,protocol=pickle.HIGHEST_PROTOCOL,fix_imports=True)
    return msg

if __name__ == '__main__':
    msg=login_message('hello','world',encode=True)
    print(pickle.loads(msg))