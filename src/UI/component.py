# -*- encoding: utf-8 -*-
'''
@File    :   component.py
@Time    :   2021/07/06 01:46:05
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   componets of the pygame
'''
import sys
import os
sys.path.append(os.path.abspath('./'))

import pygame
import time
from config.config_reader import Configer

class Input_box(object):
  def __init__(self,x,y,width,height,surface) -> None:
      super().__init__()
      self.surface=surface
      self.x=self.surface.get_width()*x-width*0.5
      self.y=self.surface.get_height()*y-height*0.5
      self.box=pygame.Rect(self.x,self.y,width,height)
      self.color_inactive=pygame.Color('lightskyblue3')
      self.color_active=pygame.Color('dodgerblue2')
      self.color=self.color_inactive
      self.active=False
      self.done=False
      self.text=''
      self.font=pygame.font.Font(None,50)
      


  def action(self,event):

    if event.type==pygame.QUIT:
      self.done=True
    if event.type==pygame.MOUSEBUTTONDOWN:
      if self.box.collidepoint(event.pos):
        self.active=True
        self.color=self.color_active
      else:
        self.active = False
        self.color=self.color_inactive
    if event.type==pygame.KEYDOWN:
      if self.active:
        if event.key == pygame.K_RETURN:
          print(self.text)
        elif event.key == pygame.K_BACKSPACE:
          self.text=self.text[:-1]
        else:
          self.text+=event.unicode

  def render(self):
    txt_surface=self.font.render(self.text,True,self.color)
    self.surface.blit(txt_surface,(self.box.x+5,self.box.y+5))
    pygame.draw.rect(self.surface,self.color,self.box,2)
