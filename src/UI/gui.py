# -*- encoding: utf-8 -*-
'''
@File    :   login.py
@Time    :   2021/07/05 16:08:02
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   UI for Login
'''

import sys
import os
sys.path.append(os.path.abspath('./'))

import pygame
import time
import random
from config.config_reader import Configer
from UI.component import Input_box

try:
  pygame.init()
except:
  pass


class Window(object):
  def __init__(self,color=(128,128,128)) -> None:
    super().__init__()
    self.configer=Configer()
    self.width,self.height=self.configer.get_window_size()
    self.layers=[]
    self.screen=pygame.display.set_mode((self.width,self.height))
    self.color=color
    self.componets=[]
    self.componets.append(Input_box(0.5,0.5,500,50,self.screen))
    self.clock=pygame.time.Clock()
  
  def run(self,play_time=2):
    start=time.time()
    speed=[2,2]

    while True:
      self.screen.fill(self.color)
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          sys.exit()
        for component in self.componets:
          component.action(event)
      for component in self.componets:
        component.render()
      pygame.display.flip()

class WindowPlayer(object):
  def __init__(self) -> None:
      super().__init__()
      self.windows=[]
      self.windows.append(Window(color=(128,0,0)))
      # self.windows.append(Window(color=(0,128,0)))
      # self.windows.append(Window(color=(0,0,128)))

  def run(self):
    while True:
      for w in self.windows:
        w.run()

class base_window(object):
  def __init__(self,capition="Hello,world!",default_color=(0,0,0),fps=25) -> None:
    super().__init__()
    pygame.display.set_caption(capition)
    self.configer=Configer()
    self.width,self.height=self.configer.get_window_size()
    self.screen=pygame.display.set_mode((self.width,self.height))
    self.layers=[]
    self.default_color=default_color
    self.clock=pygame.time.Clock()
    self.fps=fps
    self.events={}

  def add_layer(self,surface):
    self.layers.append(surface)

  def event_handler(self):
    for event in pygame.event.get():
      if event.type in self.events:
        for cb in self.events[event.type]:
          cb()
      print(event.type)

  def event_register(self,event,callback):
    if event.type in self.events:
      self.events[event.type]=[]
    self.events[event.type].append(callback)   

  def run(self):
    while True:
      self.screen.fill(self.default_color)
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          sys.exit()

        for layer in self.layers:
          layer.event_handler(event)

      for layer in self.layers:
        layer.update()
        self.screen.blit(layer.surface,(0,0))

      pygame.display.flip()
      self.clock.tick(self.fps)


class base_surface(object):
  def __init__(self,default_color=(50,0,0)) -> None:
      super().__init__()
      self.configer=Configer()
      self.window_width,self.window_height=self.configer.get_window_size()
      # self.surface=pygame.display.set_mode((self.window_width,self.window_height))
      self.surface=pygame.Surface((self.window_width,self.window_height))
      # self.surface.convert()
      self.default_color=default_color
      self.surface.fill(default_color)
      self.components=[]

  def event_handler(self,event):
    for component in self.components:
      component.event_handler(event)

  def add_component(self,*component):
    for c in component:
      self.components.append(c)
    self.blit_component()

  def add_components(self,component_list):
    for c in component_list:
      self.components.append(c)
    self.blit_component()

  def blit_component(self):
    self.surface.fill(self.default_color)
    for component in self.components:
      self.surface.blit(component.content,component.pos)

  def update(self):
    for component in self.components:
      component.update()
    self.blit_component()
     
class base_component(object):
  def __init__(self,surface,pos=(0,0)) -> None:
    super().__init__()
    self.surface=surface
    self.content=None
    self.pos=pos
    self.animations=[]

  def event_handler(self,event):
    pass

  def update(self):
    pass

  def random_pos(self):
    self.pos=(random.randint(0,self.surface_width),random.randint(0,self.surface_height))

  def move_around(self):
    self.pos=((self.pos[0]+random.randint(-2,2)),self.pos[1]+random.randint(-2,2))

class Text(base_component):
  def __init__(self,surface,text,pos=(100,200),family=None,size=36,color=(255,255,255)) -> None:
    super().__init__(surface,pos)
    # self.surface=surface
    self.text=text
    self.family=family
    self.surface_width,self.surface_height=self.surface.surface.get_width(),self.surface.surface.get_height()
    self.font=pygame.font.Font(family,size)
    self.content=self.font.render(self.text,1,color)
    # self.pos=self.content.get_rect()
    self.color=color
    self.size=size
    # self.pos.centerx=surface.surface.get_rect().centerx
    # self.animations=[]

  def update(self):
    for anim in self.animations:
      anim()

  def random_color(self):
    self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    self.content=self.font.render(self.text,1,self.color)

  def size_around(self):
    size=self.size+random.randint(-5,5)
    self.font=pygame.font.Font(self.family,size)
    self.content=self.font.render(self.text,1,self.color)

  def content_around(self):
    self.text=random.choice(["hello","world","great","lover"])
    self.content=self.font.render(self.text,random.randint(10,20),self.color)


class TextEntry(base_component):
  def __init__(self, surface, pos,width=500,height=60,family=None,size=36,bgcolor=(0,0,0),afcolor=(255,255,255),iafcolor=(210,210,210),iabcolor=(125,125,125),abcolor=(200,200,200)) -> None:
    super().__init__(surface, pos=pos)
    self.width=width
    self.height=height
    self.bgcolor=bgcolor
    self.iafcolor=iafcolor
    self.afcolor=afcolor
    self.fcolor=iafcolor
    self.iabcolor=iabcolor
    self.text="Default"
    self.abcolor=abcolor
    self.bcolor=self.iabcolor
    self.active=False
    self.family=family
    self.size=size
    self.box=pygame.Rect(self.pos[0],self.pos[1],self.width,self.height)
    self.update()

  def event_handler(self,event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      if self.box.collidepoint(event.pos):
        self.active=True
        self.bcolor=self.abcolor
        self.fcolor=self.afcolor
      else:
        self.active=False
        self.bcolor=self.iabcolor
        self.fcolor=self.iafcolor

    if event.type== pygame.KEYDOWN and self.active:
      if event.key==pygame.K_RETURN:
        print(self.text)
      elif event.key== pygame.K_BACKSPACE:
        self.text=self.text[:-1]
      else:
        self.text+=event.unicode

  def update(self):
    tx=Text(self.surface,self.text,self.pos,self.family,self.size,self.fcolor)
    self.content=tx.content

class Button(base_component):
  def __init__(self, surface, pos, width, height,text="Button",fcolor=(125,125,0),hcolor=(125,0,125),acolor=(0,125,125),func=lambda x:x) -> None:
    super().__init__(surface, pos=pos)
    self.func=func
    self.fcolor=fcolor
    self.hcolor=hcolor
    self.acolor=acolor
    self.width=width
    self.height=height
    self.text=text
    self.color=self.fcolor
    self.box=pygame.Rect(self.pos[0],self.pos[1],self.width,self.height)
    self.txt=Text(self.surface,self.text,self.pos)

  def event_handler(self, event):
    if event.type==pygame.MOUSEBUTTONDOWN:
      if self.box.collidepoint(event.pos):
        self.color=self.acolor
        self.func()
    elif event.type==pygame.MOUSEMOTION:
      if self.box.collidepoint(event.pos):
        self.color=self.hcolor
    else:
      self.color=self.fcolor

  def update(self):
    
    pass



        


if __name__ == '__main__':
  w=base_window()
  bg=base_surface()
  w.add_layer(bg)
  # tx=Text(bg,"Hello,world!")
  # tx2=Text(bg,"Great!",(500,600))
  # tx2.animations.append(tx2.random_color)
  # tx.animations.append(tx.move_around)
  # tx.animations.append(tx.random_color)
  # tx.animations.append(tx.size_around)
  # tx.animations.append(tx.content_around)
  te=TextEntry(bg,(100,100))
  te2=TextEntry(bg,(500,100))
  bg.add_component(te,te2)
  w.run()
