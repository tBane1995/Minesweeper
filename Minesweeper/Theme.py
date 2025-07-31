import sys
import sdl2
import sdl2.ext
import sdl2.ext.ttf
import sdl2.sdlimage

import Window

current_theme: int

font: sdl2.ext.FontManager
font_size: int
text_font_size: int
text_color: list[int] = []
game_text_font_size: int
game_text_color: list[int] = []

background: sdl2.ext.Texture
frame: list[sdl2.SDL_Texture] = []
center: sdl2.ext.Texture

large_button: sdl2.ext.Texture
large_button_hover: sdl2.ext.Texture
small_button: sdl2.ext.Texture
small_button_hover: sdl2.ext.Texture
small_panel: sdl2.ext.Texture
large_panel: sdl2.ext.Texture
end_panel: sdl2.ext.Texture

values: list[sdl2.SDL_Texture]
mine: sdl2.ext.Texture
close: sdl2.ext.Texture
close_hover: sdl2.ext.Texture
flag: sdl2.ext.Texture
bad: sdl2.ext.Texture
explosion: sdl2.ext.Texture

def load_texture(path: str) -> sdl2.ext.Texture:
    surface = sdl2.sdlimage.IMG_Load(path)
    texture = sdl2.SDL_CreateTextureFromSurface(Window.renderer.sdlrenderer, surface)
    sdl2.SDL_FreeSurface(surface)
    return texture

def load(id: int):
    global current_theme
    global font
    global font_size
    
    global text_font_size
    global text_color
    global game_text_font_size
    global game_text_color

    global background
    global frame
    global center

    global large_button
    global large_button_hover
    global small_button
    global small_button_hover
    global small_panel
    global large_panel
    global end_panel

    global values
    global mine
    global close
    global close_hover
    global flag
    global bad
    global explosion
    
    current_theme = id
    
    font = sdl2.ext.FontManager(b"Themes/FiraCode-Medium.ttf")
    font_size = 24
    
    # Game End Text
    text_font_size = 48
    if id == 5:
        text_color = [0, 0, 0]
    else:
        text_color = [255, 255, 255]
        
    # Game Text
    game_text_font_size = 32
    if id == 8:
        game_text_color = [255, 255, 255]
    else:
        game_text_color = [255, 48, 48]

    # Background
    background = load_texture("Themes/{}/Background.png".format(current_theme).encode("utf-8"))

    # Frame 
    frame = []
    for i in range(8):
        texture = load_texture("Themes/{}/frame_{}.png".format(current_theme, i).encode("utf-8"))
        frame.append(texture)

    center = load_texture("Themes/{}/frame_center.png".format(current_theme).encode("utf-8"))

    # Buttons
    large_button = load_texture("Themes/{}/ButtonLarge.png".format(current_theme).encode("utf-8"))
    large_button_hover = load_texture("Themes/{}/ButtonLarge_hover.png".format(current_theme).encode("utf-8"))
    small_button = load_texture("Themes/{}/ButtonSmall.png".format(current_theme).encode("utf-8"))
    small_button_hover = load_texture("Themes/{}/ButtonSmall_hover.png".format(current_theme).encode("utf-8"))
    
    # Panels
    small_panel = load_texture("Themes/{}/PanelSmall.png".format(current_theme).encode("utf-8"))
    large_panel = load_texture("Themes/{}/PanelLarge.png".format(current_theme).encode("utf-8"))
    end_panel = load_texture("Themes/{}/PanelEnd.png".format(current_theme).encode("utf-8"))

    # Tiles in Game
    values = []
    for i in range(8):
        texture = load_texture("Themes/{}/{}.png".format(current_theme, i).encode("utf-8"))
        values.append(texture)
    
    mine = load_texture("Themes/{}/Mine.png".format(current_theme).encode("utf-8"))
    close = load_texture("Themes/{}/Close.png".format(current_theme).encode("utf-8"))
    close_hover = load_texture("Themes/{}/Close_hover.png".format(current_theme).encode("utf-8"))
    flag = load_texture("Themes/{}/Flag.png".format(current_theme).encode("utf-8"))
    bad = load_texture("Themes/{}/Bad.png".format(current_theme).encode("utf-8"))
    explosion = load_texture("Themes/{}/Explosion.png".format(current_theme).encode("utf-8"))