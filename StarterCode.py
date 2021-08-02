# #Setup Code.
# #When the user presses A Shoot the Laser

def on_a_pressed():
    pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

"""

Ship Player to spawn

"""
"""

Set Asteroid sprite.

"""
"""

Ship to stay on the screen.

"""
# # Setup Code
# 
# # When the Laser Hits the Asteroid.
# 
# # When an Asteroid hits the Ship.
asteroids = [sprites.space.space_small_asteroid1,
    sprites.space.space_small_asteroid0,
    sprites.space.space_asteroid0,
    sprites.space.space_asteroid1,
    sprites.space.space_asteroid4,
    sprites.space.space_asteroid3]
ship = sprites.create(img("""
        . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c b . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . c 2 . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . e 2 . . . . . . . 
            . . . . . . e e 4 e . . . . . . 
            . . . . . . e 2 4 e . . . . . . 
            . . . . . c c c e e e . . . . . 
            . . . . e e 2 2 2 4 e e . . . . 
            . . c f f f c c e e f f e e . . 
            . c c c c e e 2 2 2 2 4 2 e e . 
            c c c c c c e e 2 2 2 4 2 2 e e 
            c c c c c c e e 2 2 2 2 4 2 e e
    """),
    SpriteKind.player)
ship.set_stay_in_screen(True)
controller.move_sprite(ship, 100, 100)
effects.star_field.start_screen_effect()
# #Queues up asteroid state to process
# #projectile = sprites.create_projectile_from_side(asteroids[randint(0, len(asteroids) - 1)], 0, 75)
# projectile.set_kind(SpriteKind.enemy)
# projectile.x = randint(10, 150)
# When the user gets hit go invisible for three seconds

def on_update_interval():
    pass
game.on_update_interval(500, on_update_interval)

# #Updates Invulnerable State
# if Invulnerable >= 1 and Invulnerable < 5:
# ship.start_effect(effects.halo)
# Invulnerable += 1
# elif Invulnerable == 5:
# Invulnerable = 0
# effects.clear_particles(ship)
# else:
# pass
# #

def on_update_interval2():
    pass
game.on_update_interval(500, on_update_interval2)
