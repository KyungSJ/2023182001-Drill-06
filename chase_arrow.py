from os import closerange
from random import randint

from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def chase_arrow(i):
    global character_x, character_y, arrow_x, arrow_y, cycle

    t = i / 1000
    character_x = (1-t) * character_x + t * arrow_x
    character_y = (1-t) * character_y + t * arrow_y

    if character_x == arrow_x and character_y == arrow_y:
        arrow_x, arrow_y = randint(0, 1280), randint(0, 1024)
        cycle = 0
    pass

running = True
character_x, character_y = TUK_WIDTH // 2,TUK_HEIGHT // 2
arrow_x, arrow_y = randint(0, 1280), randint(0, 1024)
frame = 0
cycle = 0


while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
    arrow.draw(arrow_x, arrow_y, 50, 50)
    update_canvas()
    frame = (frame + 1) % 8
    cycle += 1
    chase_arrow(cycle)
    handle_events()

close_canvas()