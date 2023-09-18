from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character=load_image('character.png')
while(1):
    i=0
    while(i<390):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(i+400,90)
        i=i+2

        delay(0.001)

    i=0
    while(i<500):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(790,90+i)
        i=i+2

        delay(0.001)

    i=0
    while(i<790):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(790-i,590)
        i=i+2

    delay(0.001)
    i=0
    while(i<500):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,590-i)
        i=i+2

        delay(0.001)
    i=0
    while(i<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(i,90)
        i=i+2

        delay(0.001)

    i=270
    while(i<360+270):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+200 * math.cos(2 * math.pi * i/360),300 + 200 * math.sin(2 * math.pi * i/360))
        i=i+1
        delay(0.001)

close_canvas()
