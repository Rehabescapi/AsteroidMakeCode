# #Setup Code.

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . . 
                    . . . 7 7 . . .
        """),
        ship,
        0,
        -140)
    projectile.start_effect(effects.cool_radial, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# #When  A Laser hits an Asteroid.

def on_on_overlap(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.disintegrate)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    global Invulnerable
    if Invulnerable == 0:
        scene.camera_shake(4, 500)
        Invulnerable += 1
        sprite.start_effect(effects.fire, 200)
        info.change_life_by(-1)
    else:
        pass
    otherSprite.destroy(effects.disintegrate)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

"""

# Setup Code

# When the Laser Hits the Asteroid.

# When an Asteroid hits the Ship.

"""
projectile: Sprite = None
Invulnerable = 0
ship: Sprite = None
asteroids = [sprites.space.space_small_asteroid1,
    sprites.space.space_small_asteroid0,
    sprites.space.space_asteroid0,
    sprites.space.space_asteroid1,
    sprites.space.space_asteroid4,
    sprites.space.space_asteroid3]
ship = sprites.create(sprites.space.space_red_ship, SpriteKind.player)
ship.set_stay_in_screen(True)
ship.bottom = 120
Invulnerable = 0
controller.move_sprite(ship, 100, 100)
info.set_life(3)
effects.star_field.start_screen_effect()

def on_update_interval():
    global projectile
    # #Queues up asteroid state to process
    projectile = sprites.create_projectile_from_side(asteroids[randint(0, len(asteroids) - 1)], 0, 75)
    projectile.set_kind(SpriteKind.enemy)
    projectile.x = randint(10, 150)
game.on_update_interval(500, on_update_interval)

def on_update_interval2():
    global Invulnerable
    # #Updates Invulnerable State
    if Invulnerable >= 1 and Invulnerable < 5:
        ship.start_effect(effects.halo)
        Invulnerable += 1
    elif Invulnerable == 5:
        Invulnerable = 0
        effects.clear_particles(ship)
    else:
        pass
game.on_update_interval(500, on_update_interval2)
