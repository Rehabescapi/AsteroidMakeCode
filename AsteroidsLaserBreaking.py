# #Setup Code.
# #When the user presses A Shoot the Laser

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 8 8 8 8 . . . . . . 
                    . . . . . . 8 8 8 8 . . . . . . 
                    . . . . . . 8 8 8 8 . . . . . . 
                    . . . . . . 8 8 8 8 . . . . . . 
                    . . . . . . 8 8 8 8 . . . . . . 
                    . . . . . . 8 8 8 8 . . . . . . 
                    . . . . . . 8 8 8 8 . . . . . . 
                    . . . . . . 8 8 8 8 . . . . . . 
                    . . . . . . 8 8 8 8 . . . . . . 
                    . . . . . . 8 8 8 8 . . . . . .
        """),
        ship,
        0,
        -100)
    projectile.start_effect(effects.cool_radial, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

projectile: Sprite = None
ship: Sprite = None
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

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile_from_side(asteroids[randint(0, len(asteroids) - 1)], 0, 50)
    projectile.x = randint(10, 150)
    projectile.set_kind(SpriteKind.enemy)
game.on_update_interval(2000, on_update_interval)
