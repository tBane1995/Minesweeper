from dis import Instruction
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

import Game
import Themes
import Instructions
import Credits

class Menu:
    
    def __init__(self):
        self.load()
    
    def load(self):
        self.background = Theme.background
        self.buttons = self.create_buttons()
        
    def create_buttons(self) -> []:
        buttons_names = ["new game", "themes", "instructions", "credits", "exit"]
        
        buttons = []
        buttons_count = len(buttons_names)
        margin = 16
        btn_w = 256
        btn_h = 48
        
        start_y = Window.size[1]//2 - (buttons_count*( btn_h + margin) + margin)//2 + btn_h//2 + margin
        
        for i in range(buttons_count):
            x = Window.size[0]//2
            y = start_y +  i * (btn_h+ margin)
            btn = Button.Button(buttons_names[i], Theme.large_button, Theme.large_button_hover, x, y, btn_w, btn_h)
            buttons.append(btn)
            
        buttons[0].onclick_func = lambda:  Window.pages.append(Game.Game())
        #buttons[1].onclick_func = lambda:  Window.pages.append(Highscores())
        buttons[1].onclick_func = lambda:  Window.pages.append(Themes.Themes())
        buttons[2].onclick_func = lambda:  Window.pages.append(Instructions.Instructions())
        buttons[3].onclick_func = lambda:  Window.pages.append(Credits.Credits())
        buttons[4].onclick_func = lambda: exit()

        return buttons
        
    def cursor_hover(self, mouse_x: int, mouse_y: int):
        for btn in self.buttons:
            btn.cursor_hover(mouse_x, mouse_y)
            
    def handle_events(self, event: sdl2.ext.events, mouse_x: int, mouse_y: int):
        for btn in self.buttons:
            btn.handle_events(event, mouse_x, mouse_y)
            
    def update(self):
        for btn in self.buttons:
            btn.update()
    
    
        
    def draw(self):
        dstrect = sdl2.SDL_Rect(0,0,Window.size[0], Window.size[1])
        sdl2.SDL_RenderCopy(Window.renderer.sdlrenderer, self.background, None, dstrect)
        
        for btn in self.buttons:
            btn.draw()