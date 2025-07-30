import os
import sys
import sdl2
import sdl2.ext

import Theme

window = sdl2.ext.Window
renderer = sdl2.ext.Renderer

color = sdl2.ext.Color(48, 48, 48)
size = (448, 768)

pages = []

def create():
    global window
    global renderer
    global color
    global size
    global pages

    window = sdl2.ext.Window("Minesweeper", size)
    window.show()

    renderer = sdl2.ext.Renderer(window)
    
    pages = []

def draw_frame(x: int, y: int, width: int, height: int):

    # Center
    dstrect = sdl2.SDL_Rect(x,y,width,height)
    sdl2.SDL_RenderCopy(renderer.sdlrenderer, Theme.center, None, dstrect)

    # Top
    dstrect = sdl2.SDL_Rect(x,y,12,12)
    sdl2.SDL_RenderCopy(renderer.sdlrenderer, Theme.frame[0], None, dstrect)

    dstrect = sdl2.SDL_Rect(x+12,y,width-24,12)
    sdl2.SDL_RenderCopy(renderer.sdlrenderer, Theme.frame[1], None, dstrect)

    dstrect = sdl2.SDL_Rect(x+width-12,y,12,12)
    sdl2.SDL_RenderCopy(renderer.sdlrenderer, Theme.frame[2], None, dstrect)

    # Left & Right
    dstrect = sdl2.SDL_Rect(x,y+12,12,height-24)
    sdl2.SDL_RenderCopy(renderer.sdlrenderer, Theme.frame[3], None, dstrect)

    dstrect = sdl2.SDL_Rect(x+width-12,y+12,12,height-24)
    sdl2.SDL_RenderCopy(renderer.sdlrenderer, Theme.frame[4], None, dstrect)

    # Bottom
    dstrect = sdl2.SDL_Rect(x,y+height-12,12,12)
    sdl2.SDL_RenderCopy(renderer.sdlrenderer, Theme.frame[5], None, dstrect)

    dstrect = sdl2.SDL_Rect(x+12,y+height-12,width-24,12)
    sdl2.SDL_RenderCopy(renderer.sdlrenderer, Theme.frame[6], None, dstrect)

    dstrect = sdl2.SDL_Rect(x+width-12,y+height-12,12,12)
    sdl2.SDL_RenderCopy(renderer.sdlrenderer, Theme.frame[7], None, dstrect)

    