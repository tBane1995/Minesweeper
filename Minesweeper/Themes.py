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

class Themes:
    def __init__(self):
        self.load()
        
    def load(self):
        
        self.left_back_btn = Button.Button("<", Theme.small_button, Theme.small_button_hover, 32, 32, 64, 64)
        self.left_back_btn.onclick_func = lambda: Window.pages.pop()
               
        self.right_back_btn = Button.Button(">", Theme.small_button, Theme.small_button_hover,416, 32, 64, 64)
        self.right_back_btn.onclick_func = lambda: Window.pages.pop()
        
        self.themes_buttons = self.create_theme_buttons()
    
    def create_theme_buttons(self) -> []:
        buttons_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        
        buttons = []
        buttons_count = len(buttons_names)
        margin = 16
        btn_w = 256
        btn_h = 48
        
        whole_y= buttons_count*( btn_h + margin) - margin
        
        start_y = Window.size[1]//2 + self.left_back_btn.h//2 - whole_y//2 + btn_h//2
        
        def set_theme(id: int):
            Theme.load(id)
            for page in Window.pages:
                page.load()
            
        for i in range(buttons_count):
            x = Window.size[0]//2
            y = start_y +  i * (btn_h+ margin)
            btn = Button.Button(buttons_names[i], Theme.large_button, Theme.large_button_hover, x, y, btn_w, btn_h)
            btn.onclick_func = lambda id=i: set_theme(id)
            buttons.append(btn)
            
            
        return buttons
        
    def cursor_hover(self, mouse_x: int, mouse_y: int):
        self.left_back_btn.cursor_hover(mouse_x, mouse_y)
        self.right_back_btn.cursor_hover(mouse_x, mouse_y)
        
        for btn in self.themes_buttons:
            btn.cursor_hover(mouse_x, mouse_y)
        
        
    def update(self):
        self.left_back_btn.update()
        self.right_back_btn.update()
        
        for btn in self.themes_buttons:
            btn.update()
    
    def handle_events(self, event: sdl2.ext.events, mouse_x: int, mouse_y: int):
        self.left_back_btn.handle_events(event, mouse_x, mouse_y)
        self.right_back_btn.handle_events(event, mouse_x, mouse_y)
        
        for btn in self.themes_buttons:
            btn.handle_events(event, mouse_x, mouse_y)
        
    def draw(self):
        
        Window.draw_frame(0, self.left_back_btn.h, Window.size[0], Window.size[1] - self.left_back_btn.h)
        
        Window.draw_frame(64,0,320,64)
        Text.draw_text_centered(Window.size[0]//2, 32, "Themes")

        self.left_back_btn.draw()
        self.right_back_btn.draw()

        for btn in self.themes_buttons:
            btn.draw()