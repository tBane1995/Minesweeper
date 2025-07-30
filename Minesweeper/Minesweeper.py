
import os
import sys
import sdl2
import sdl2.ext
import sdl2.sdlttf
import sdl2.sdlimage

import time

sdl2.ext.init()

import Window
import Theme
import Button
import Text

import Game
import Themes
import Instructions
import Credits
import Menu

def exit():
    sdl2.ext.quit()
    sys.exit(0)

Window.create()
Theme.load(0)
Window.pages.append(Menu.Menu())

while True:
    
    import ctypes

    mx = ctypes.c_int(0)
    my = ctypes.c_int(0)
    sdl2.SDL_GetMouseState(ctypes.byref(mx), ctypes.byref(my))
    mouse_x, mouse_y = mx.value, my.value
    
    Window.pages[-1].cursor_hover(mouse_x, mouse_y)
    
    # handle events
    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            exit()
    
        if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
            Window.pages[-1].handle_events(event, mouse_x, mouse_y)
    
        if event.type == sdl2.SDL_MOUSEBUTTONUP:
            Window.pages[-1].handle_events(event, mouse_x, mouse_y)
                  
    # update
    Window.pages[-1].update()
    
    # render
    Window.renderer.color = Window.color
    Window.renderer.clear()
    Window.pages[-1].draw()
    Window.renderer.present()
    
    time.sleep(1/60)

sdl2.ext.quit()
sys.exit(0)