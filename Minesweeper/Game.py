import os
import sys
import sdl2
import sdl2.ext
import sdl2.sdlttf
import sdl2.sdlimage

import numpy as np
import time

import Window
import Theme
import Button
import Text

class Game:
    def __init__(self):
        
        self.left_back_btn = Button.Button("<", Theme.small_button, Theme.small_button_hover, 32, 32, 64, 64)
        self.left_back_btn.onclick_func = lambda: Window.pages.pop()
        
        self.time_btn = Button.Button("", Theme.small_panel, Theme.small_panel, 128, 32, 128, 64)
        self.time_btn.set_font_size(Theme.game_text_font_size)
        self.time_btn.set_text_color(Theme.game_text_color)

        self.face_btn = Button.Button("", Theme.small_button, Theme.small_button, 224, 32, 64, 64)

        self.flags_btn = Button.Button("", Theme.small_panel, Theme.small_panel, 320, 32, 128, 64)
        self.flags_btn.set_text_color(Theme.game_text_color)
        self.flags_btn.set_font_size(Theme.game_text_font_size)

        self.right_back_btn = Button.Button(">", Theme.small_button, Theme.small_button_hover, 416, 32, 64, 64)
        self.right_back_btn.onclick_func = lambda: Window.pages.pop()

        self.width = 7
        self.height = 11

        self.start_game()
        
    def start_game(self):
        self.end_game = False
        self.win_game = True
        self.end_button = None
        
        self.create_tiles()
        self.add_mines()
        self.set_values()
        self.hide_tiles()

        self.setted_flags = 0
        self.time_start = time.time()
        self.time_end = time.time()
        
        self.time_btn.set_text(self.get_time())
        self.flags_btn.set_text(str(self.mines_count - self.setted_flags))

    def get_time(self) -> str:
        
        self.time_end = time.time()
        time_str= ""

        minutes = int((self.time_end-self.time_start) // 60)
        seconds = int((self.time_end-self.time_start) % 60)

        if(minutes < 10):
            time_str = "0" + str(minutes)
        else:
            time_str = str(minutes)

        time_str = time_str + ":"

        if(seconds < 10):
            time_str = time_str + "0" + str(seconds)
        else:
            time_str = time_str + str(seconds)

        return time_str

    def create_tiles(self):
        tiles: list[chr] = []
        
        for y in range(self.height):
            for x in range(self.width):
                tiles.append('0')
       
        self.tiles = tiles
    
    def add_mines(self):
        mines_count = int(len(self.tiles)*15/100)
        self.mines_count = mines_count

        while( mines_count > 0):
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            if self.tiles[y*self.width + x]!='*':
                self.tiles[y*self.width + x]='*'
                mines_count=mines_count-1
        
        

    def set_values(self):
        for y in range(self.height):
            for x in range(self.width):
                
                if self.tiles[y*self.width + x]=='*':
                    continue
                    
                val = 0
                # top left
                if y >0 and x>0 and self.tiles[(y-1)*self.width + x-1]=='*':
                    val = val+1
                # top
                if y >0 and self.tiles[(y-1)*self.width + x]=='*':
                    val = val+1
                # top right
                if y >0 and x<self.width-1 and self.tiles[(y-1)*self.width + x+1]=='*':
                    val = val+1
                # left
                if x >0 and self.tiles[y*self.width + x-1]=='*':
                    val = val+1
                # right
                if x <self.width-1 and self.tiles[y*self.width + x+1]=='*':
                    val = val+1
                
                # bottom left
                if y < self.height-1 and x>0 and self.tiles[(y+1)*self.width + x-1]=='*':
                    val = val+1
                # bottom 
                if y < self.height-1 and self.tiles[(y+1)*self.width + x]=='*':
                    val = val+1
                # bottom right
                if y < self.height-1 and x<self.width-1 and self.tiles[(y+1)*self.width + x+1]=='*':
                    val = val+1
                
                self.tiles[y*self.width+x] = str(val)
      
    def hide_tiles(self):
        tiles_status: list[chr] = []
        
        for y in range(self.height):
            for x in range(self.width):
                tiles_status.append('c')
       
        self.tiles_status = tiles_status
    
    def open_tile(self, x: int, y: int):
        if x < 0 or x >= self.width or y < 0 or y>= self.height:
            return
        
        if self.tiles_status[y*self.width + x]=='o':
            return
        
        self.tiles_status[y*self.width + x]='o'
        
        if self.tiles[y*self.width + x] =='*':
            self.end_game = True
            self.win_game = False
            self.create_end_button("game over")
        if self.tiles[y*self.width + x] == '0':
            for yy in range(y-1, y+2):
                for xx in range(x-1, x+2):
                    self.open_tile(xx,yy)
        
        self.win()
        if self.end_game == True and self.win_game== True:
            self.create_end_button("you win")


    def change_flag(self, x: int, y: int):

        if self.tiles_status[y*self.width+x] == 'f':
            
            self.tiles_status[y*self.width+x] = 'c'
            self.setted_flags = self.setted_flags - 1
            self.flags_btn.set_text(str(self.mines_count - self.setted_flags))

        elif self.tiles_status[y*self.width+x] == 'c' and self.setted_flags < self.mines_count:
            
            self.tiles_status[y*self.width+x] = 'f'
            self.setted_flags = self.setted_flags + 1
            self.flags_btn.set_text(str(self.mines_count - self.setted_flags))

    def click_tile(self, event: sdl2.ext.events, mouse_x: int, mouse_y: int):
        
        if mouse_y < 64:
            return
            
        x = mouse_x//64
        y = mouse_y//64 - 1
        
        if event.type == sdl2.SDL_MOUSEBUTTONUP:
            if event.button.button == sdl2.SDL_BUTTON_RIGHT:
                self.change_flag(x,y)
            elif event.button.button == sdl2.SDL_BUTTON_LEFT:
                if(self.tiles_status[y*self.width+x] == 'f'):
                    return
                self.open_tile(x,y)
    
    def draw_tiles(self):
        for y in range(self.height):
            for x in range(self.width):
                dstrect = sdl2.SDL_Rect(
                    x*64,
                    y*64 + 64,
                    64, 64
                )
                
                
                tex: sdl2.ext.Texture
                if self.end_game == True:

                    if self.tiles_status[y*self.width + x]=='f':
                        if self.tiles[y*self.width + x] != '*':
                            tex = Theme.bad
                        else:
                            tex = Theme.mine
                    elif self.tiles_status[y*self.width+x] =='o' and self.tiles[y*self.width+x] == '*':
                        tex = Theme.explosion
                    elif self.tiles[y*self.width + x] == '*':
                        tex = Theme.mine
                    else:
                        tex = Theme.values[int(self.tiles[y*self.width + x])]

                else:
                    if self.tiles_status[y*self.width + x]=='c':
                        tex = Theme.close
                    elif self.tiles_status[y*self.width + x] =='f':
                        tex = Theme.flag
                    else:
                        tex = Theme.values[int(self.tiles[y*self.width + x])]
                
                sdl2.SDL_RenderCopy(Window.renderer.sdlrenderer, tex, None, dstrect)
    
    def create_end_button(self, text: str):

        self.end_button = Button.Button(text, Theme.end_panel, Theme.end_panel, Window.size[0]//2, Window.size[1]*3//7, 256, 128)
        self.end_button.onclick_func = lambda: self.start_game()
    
    def win(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.tiles[y*self.width+x] != '*' and self.tiles_status[y*self.width+x]=='c':
                    return
        
        self.end_game = True
        
        
    def cursor_hover(self, mouse_x: int, mouse_y: int):
        self.left_back_btn.cursor_hover(mouse_x, mouse_y)
        self.right_back_btn.cursor_hover(mouse_x, mouse_y)
        
        if self.end_game == True:
            self.end_button.cursor_hover(mouse_x, mouse_y)
        
        
    def update(self):
        
        self.left_back_btn.update()
        self.right_back_btn.update()

        if self.end_game == False:
            self.time_btn.set_text(self.get_time())
        
        if self.end_game == True:
            self.end_button.update()
    
    def handle_events(self, event: sdl2.ext.events, mouse_x: int, mouse_y: int):
        self.left_back_btn.handle_events(event, mouse_x, mouse_y)
        self.right_back_btn.handle_events(event, mouse_x, mouse_y)
        
        if self.end_game == True:
            self.end_button.handle_events(event, mouse_x, mouse_y)
        
        elif event.type == sdl2.SDL_MOUSEBUTTONUP:
            self.click_tile(event, mouse_x, mouse_y)
            
        
    def draw(self):
     
        self.left_back_btn.draw()
        self.time_btn.draw()
        self.face_btn.draw()
        self.flags_btn.draw()
        self.right_back_btn.draw()


        self.draw_tiles()
        if self.end_game == True:
            self.end_button.draw()