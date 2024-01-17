#!/user/bin/env python3

# Created by: Marli Peters
# Created on: Jan 2024
# This program is the "Space Aliens" program on the PyBadge

import ugame
import stage
import time 
import random 

import constants

# function that holds the menu
def menu_scene():
    
    # images to import
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text 
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(4, 10)
    text1.text("Silly Goose Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(32, 110)
    text2.text("Press start!")
    text.append(text2)
    
    # set background to first image and set size
    background = stage.Grid(image_bank_mt_background, 10, 8)
  
    # create stage and set game to 60fps
    game = stage.Stage(ugame.display, 60)
    # set layers of all sprites
    game.layers = text + [background]
    # render all sprites
    game.render_block()
    
    # loop to refpeat forever
    while True:
        # get user input
        keys =  ugame.buttons.get_pressed()
        
        # button
        if keys & ugame.K_START != 0:
            game_scene()
        
        # redraw sprites
        game.tick()

# function that holds the spaslh screen
def splash_scene():

    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    
    # images to import
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # set background to first image and set size
    background = stage.Grid(image_bank_mt_background, 10, 8)

    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white
  
    # create stage and set game to 60fps
    game = stage.Stage(ugame.display, 60)
    # set layers of all sprites
    game.layers = [background]
    # render all sprites
    game.render_block()
    
    # wait for 2 seconds
    while True:
        time.sleep(2.0)
        menu_scene()

# function that holds the main game
def game_scene():

    
    # images to import
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # button info
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    # set background to first image and set size
    background = stage.Grid(image_bank_background, 10, 8)

    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
    
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    alien = stage.Sprite(image_bank_sprites, 9, int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)

    # create stage and set game to 60fps
    game = stage.Stage(ugame.display, 60)
    # set layers of all sprites
    game.layers = [ship] + [alien] + [background]
    # render all sprites
    game.render_block()
    
    # loop to refpeat forever
    while True:
        # get user input
        keys =  ugame.buttons.get_pressed()
        
        # a button fire
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        
        #b button
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
            
        if keys & ugame.K_RIGHT != 0:

            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
                
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0 , ship.y)
                
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # update game logic play sound if a is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
            
        # redraw sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    splash_scene()
