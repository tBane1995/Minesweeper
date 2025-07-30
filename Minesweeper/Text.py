import sys
import os
import sdl2
import sdl2.ext
import sdl2.ext.ttf

import Window
import Theme

def text_width(text: str, font_manager: sdl2.ext.FontManager, character_size: int) -> int:

    if text == "":
        return 0

    surface = font_manager.render(text, size=character_size, color=sdl2.ext.Color(255, 255, 255))
    texture = sdl2.SDL_CreateTextureFromSurface(Window.renderer.sdlrenderer, surface)
    
    w = sdl2.c_int()
    h = sdl2.c_int()
    sdl2.SDL_QueryTexture(texture, None, None, w, h)
    
    sdl2.SDL_DestroyTexture(texture)
    sdl2.SDL_FreeSurface(surface)

    return w.value

def wrap_text(font_manager: sdl2.ext.FontManager, character_size: int, line_width: int, text : str) -> []:
    
    wrapped_text = []
    
    line = ""
    word = ""

    for character in text:
        if text_width(word+character, font_manager, character_size) > line_width:
            if(line != ""):
                wrapped_text.append(line)
                line = ""
            
            # word longer than line
            l = ""
            word = word + character
            
            for c in word:
                if text_width(l+c, font_manager, character_size) > line_width:
                    wrapped_text.append(l)
                    l = c
                else:
                    l = l + c

            wrapped_text.append(l)
            word = ""

        elif text_width(line+word+character, font_manager, character_size) > line_width:
            wrapped_text.append(line)
            line = ""
            word = word + character
        elif character == '\n':
            if text_width(line+word, font_manager, character_size) > line_width:
                wrapped_text.append(line)
                wrapped_text.append(word)
                line = ""
                word = ""
            else:
                wrapped_text.append(line+word)
                line = ""
                word = ""
        elif character == ' ' or character == '\t':
            if text_width(line+word, font_manager, character_size) > line_width:
                wrapped_text.append(line)
                line = ""
            else:
                if character == '\t':
                    line = line + word + "    ";
                else:
                    line = line + word + character;

            word = "";
        elif character != '\n':
            word = word + character;

    if line != "" or word != "":
        wrapped_text.append(line + word)

    return wrapped_text
    
    
def draw_text(x: int, y: int, text:  list[str]):
    
    for i in range(len(text)):
        
        if text[i] == "" or text[i]=="\n":
            continue
        
        surface = Theme.font.render(text[i], size=Theme.font_size, color=Theme.text_color)
        texture = sdl2.SDL_CreateTextureFromSurface(Window.renderer.sdlrenderer, surface)
        w = sdl2.c_int()
        h = sdl2.c_int()
        sdl2.SDL_QueryTexture(texture, None, None, w, h)
            
        yy = y + i*Theme.font_size
        
        dstrect = sdl2.SDL_Rect(x, yy , w.value, h.value)
    
        sdl2.SDL_RenderCopy(Window.renderer.sdlrenderer, texture, None, dstrect)
        sdl2.SDL_DestroyTexture(texture)
        sdl2.SDL_FreeSurface(surface)


def draw_text_centered(x: int, y: int, text:  str):
    
    if text == "" or text=="\n":
        return
        
    surface = Theme.font.render(text, size=Theme.font_size, color=Theme.text_color)
    texture = sdl2.SDL_CreateTextureFromSurface(Window.renderer.sdlrenderer, surface)
    w = sdl2.c_int()
    h = sdl2.c_int()
    sdl2.SDL_QueryTexture(texture, None, None, w, h)
                    
    dstrect = sdl2.SDL_Rect(x - w.value//2, y -h.value//2 , w.value, h.value)
    
    sdl2.SDL_RenderCopy(Window.renderer.sdlrenderer, texture, None, dstrect)
    sdl2.SDL_DestroyTexture(texture)
    sdl2.SDL_FreeSurface(surface)