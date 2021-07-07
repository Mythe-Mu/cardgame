# -*- encoding: utf-8 -*-
'''
@File    :   db.py
@Time    :   2021/07/05 16:13:22
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   DB Control
'''

import sys
import os
sys.path.append(os.path.abspath('./'))

import pymysql as psql


class DB(object):
    def __init__(self,db=None,host='localhost',user='root',password='',port=3306,db_name='player',charset='utf8mb4') -> None:
        super().__init__()
        if db==None:
            try:
                self.db=psql.connect(
                        host=host,
                        user=user,
                        port=port,
                        db=db_name,
                        charset=charset
                    )
            except:
                print("Database connect failed!")
                exit()
        else:
            self.db=db
        self.cur=self.db.cursor()
        self.e=self.cur.execute


if __name__ == '__main__':
    # test
    name='tester'
    b=DB()
    b.e("SELECT * from users where user_name='%s'"%name)
    data=b.cur.fetchall()
    for i in data:
        for k in i:
            print(k)