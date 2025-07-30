import os
import sys
import sdl2
import sdl2.ext
import sdl2.sdlttf
import sdl2.sdlimage
import time

import Window
import Theme

ButtonStates = ["idle", "hover", "press"]

class Button:
    
    def __init__(self, text: str, texture: sdl2.ext.Texture, texture_hover: sdl2.ext.Texture, x: int, y: int , w: int, h: int):
        
        self.text = text
        self.font = Theme.font
        self.font_size = Theme.font_size
        self.texture = texture
        self.texture_hover = texture_hover
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.state = 0 # 0-idle, 1-hover, 2-press
        
        self.text_color = [255, 255, 255]

        self.onclick_func = None
        
        self.click_time = time.time()
    
    def set_text(self, text:str):
        self.text = text
    
    def set_text_color(self, color: list[int]):
        self.text_color = color
    def set_font_size(self, size: int):
        self.font_size = size

    def click(self):
        if(self.onclick_func):
                self.onclick_func()
                        
    def cursor_hover(self, mouse_x: int, mouse_y: int):
        if self.state != 2:
            if mouse_x >= self.x-self.w//2 and mouse_x <= self.x+self.w//2 and mouse_y >= self.y-self.h//2 and mouse_y <= self.y+self.h//2:
                self.state = 1
            else:
                self.state = 0
            
    def handle_events(self, event: sdl2.ext.events,  mouse_x: int, mouse_y: int):
        if event.type == sdl2.SDL_MOUSEBUTTONUP:
            if mouse_x >= self.x-self.w//2 and mouse_x <= self.x+self.w//2 and mouse_y >= self.y-self.h//2 and mouse_y <= self.y+self.h//2:
                self.state = 2
                self.click_time = time.time()
            
    def update(self):
        if self.state == 2:
            if time.time() - self.click_time > 0.25:
                self.state = 0
                self.click()
        
    def draw(self):
        
        dstrect = sdl2.SDL_Rect(
            self.x - self.w // 2,
            self.y - self.h// 2,
            self.w, self.h
        )

        if self.state == 0:
            sdl2.SDL_RenderCopy(Window.renderer.sdlrenderer, self.texture, None, dstrect)
        else: 
            sdl2.SDL_RenderCopy(Window.renderer.sdlrenderer, self.texture_hover, None, dstrect)
        
        if( self.text != ""):
            surface = self.font.render(self.text, size=self.font_size, color=self.text_color)
            text = sdl2.SDL_CreateTextureFromSurface(Window.renderer.sdlrenderer, surface)
            w = sdl2.c_int()
            h = sdl2.c_int()
            sdl2.SDL_QueryTexture(text, None, None, w, h)

            dstrect = sdl2.SDL_Rect(
                self.x - w.value // 2,
                self.y - h.value // 2,
                w.value, h.value
            )

            sdl2.SDL_RenderCopy(Window.renderer.sdlrenderer, text, None, dstrect)
            sdl2.SDL_DestroyTexture(text)
            sdl2.SDL_FreeSurface(surface)
