# -*- encoding: utf-8 -*-
'''
@File    :   glet_UI.py
@Time    :   2021/07/06 05:36:23
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   pyglet UI
'''

import sys
import os
sys.path.append(os.path.abspath('./'))

import pyglet
from config.config_reader import Configer

class Window(object):
  def __init__(self) -> None:
      super().__init__()
      self.configer=Configer()
      self.window=pyglet.window.Window()
      self.window_width,self.window_height=self.configer.get_window_size()
      self.components=[]
      self.label=pyglet.text.Label("Hello,World!",
            font_name="Times New Roman",
            font_size=36,
            x=self.window.width//2,y=self.window.height//2,
            anchor_x='center',anchor_y='center')
      self.components.append(self.label)
      @self.window.event
      def on_key_press(symbol,modifiers):
        print("A key was pressed!")
      
      @self.window.event 
      def on_draw():
        self.window.clear()
        for component in self.components:
          component.draw()

  def run(self):
    pyglet.app.run()



class Login(Window):
  def __init__(self) -> None:
      super().__init__()
      self.username=""
      self.password=""
      self.width=300
      self.height=60
      self.x=self.window_width//2-self.width//2
      self.y=self.window_height//2-self.height//2
      self.username_input=pyglet.gui.TextEntry("Input your Name",self.x,self.y)
      
      



# window=pyglet.window.Window()
# label=pyglet.text.Label("Hello,World!",
#             font_name="Times New Roman",
#             font_size=36,
#             x=window.width//2,y=window.height//2,
#             anchor_x='center',anchor_y='center')

# img=pyglet.resource.image('img/1p.png')
# print(img.width,img.height)

# @window.event
# def on_key_press(symbol,modifiers):
#   print("A key was pressed")


# @window.event 
# def on_draw():
#   window.clear()
#   label.draw()
#   img.blit(100,200)


# pyglet.app.run()
if __name__ == '__main__':
  w=Window()
  w.run()