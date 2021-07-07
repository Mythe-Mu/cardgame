# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2021/07/06 23:25:04
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   Test event
'''
import sys
import os
sys.path.append(os.path.abspath('./'))

from UI.gui import *


if __name__ == '__main__':
  w=base_window()
  w.run()
  