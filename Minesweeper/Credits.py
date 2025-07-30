import os
import sys
import sdl2
import sdl2.ext
import sdl2.sdlttf
import sdl2.sdlimage

import Window
import Theme
import Button
import Text


class Credits:
    def __init__(self):
        self.left_back_btn = Button.Button("<", Theme.small_button, Theme.small_button_hover, 32, 32, 64, 64)
        self.left_back_btn.onclick_func = lambda: Window.pages.pop()
             
        self.right_back_btn = Button.Button(">", Theme.small_button, Theme.small_button_hover, 416, 32, 64, 64)
        self.right_back_btn.onclick_func = lambda: Window.pages.pop()

        c = "This program may be downloaded, copied, modified. \n\n\nProgram created by tBane.\n\n"
        self.credits = Text.wrap_text(Theme.font, Theme.font_size, Window.size[0]-2*8 - 2*8, c)
        
        
    def cursor_hover(self, mouse_x: int, mouse_y: int):
        self.left_back_btn.cursor_hover(mouse_x, mouse_y)
        self.right_back_btn.cursor_hover(mouse_x, mouse_y)
        
        
    def update(self):
        self.left_back_btn.update()
        self.right_back_btn.update()
    
    def handle_events(self, event: sdl2.ext.events, mouse_x: int, mouse_y: int):
        self.left_back_btn.handle_events(event, mouse_x, mouse_y)
        self.right_back_btn.handle_events(event, mouse_x, mouse_y)
        
    def draw(self):
       
        Window.draw_frame(0, self.left_back_btn.h, Window.size[0], Window.size[1] - self.left_back_btn.h)
        Text.draw_text(16, self.left_back_btn.h + 16, self.credits)


        Window.draw_frame(64,0,320,64)
        Text.draw_text_centered(Window.size[0]//2, 32, "Credits")

        self.left_back_btn.draw()
        self.right_back_btn.draw()