import random
from pico2d import *
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

mx = []
my = []

def handle_events():
    global running
    global num
    global mx, my
    global hx, hy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mx.append(event.x)
            my.append(TUK_HEIGHT - 1 - event.y)
            num += 1
        elif event.type == SDL_MOUSEMOTION:
            hx, hy = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def move_character(hx, hy):
    global x, y


running = True
x, y = 400, 300
index = 0
num = 0
frame = 0
hide_cursor()
hx, hy = 0, 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(hx, hy)
    if num != index:
        for i in range(index, num):
            hand.draw(mx[i], my[i])
        x = x + math.cos(math.atan2(my[index] - y, mx[index] - x))
        y = y + math.sin(math.atan2(my[index] - y, mx[index] - x))
        if x < mx[index]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif x >= mx[index]:
            character.clip_composite_draw(frame * 100, 100 * 1, 100, 100,0, 'h', x, y, 100, 100)
        if mx[index] - 1 <= x and x <= mx[index] + 1 and my[index] - 1 <= y and y <= my[index] + 1:
            index += 1
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()