# -*- encoding: utf-8 -*-
'''
@File    :   shape.py
@Time    :   2021/07/07 15:34:19
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   All base shapes
'''

import sys
import os
sys.path.append(os.path.abspath('./'))

import pygame

class base_shape(object):
  def __init__(self,surface) -> None:
    super().__init__()
    self.surface=surface
    
