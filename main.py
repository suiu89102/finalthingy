def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . 
                    . . . . . 1 . . 
                    . . 1 . 1 1 . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 1 . . 
                    . . 1 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        ship,
        0,
        -140)
    projectile.start_effect(effects.blizzard, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite2, otherSprite2):
    scene.camera_shake(4, 500)
    otherSprite2.destroy(effects.disintegrate)
    sprite2.start_effect(effects.fire, 200)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.disintegrate)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
ship: Sprite = None
asteroids = [sprites.space.space_small_asteroid1,
    sprites.space.space_small_asteroid0,
    sprites.space.space_asteroid0,
    sprites.space.space_asteroid1,
    sprites.space.space_asteroid4,
    sprites.space.space_asteroid3]
ship = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . 3 e e 3 . . . . . . 
            . . . . . . 3 3 3 3 . . . . . . 
            . . . . . . e e e e . . . . . . 
            . . . . . . e e e e . . . . . . 
            . . . . . . e e e 2 . . . . . . 
            . . . . . . e f e e . . . . . . 
            . . . . . . e e e e . . . . . . 
            . . . . . . e e 2 e . . . . . . 
            . . . . . . e e e e . . . . . . 
            . . . e e e e e e e e e e . . . 
            . . e f e 2 e e f e e f e e . . 
            . . e e e e e e e e e 2 e e . . 
            . . e f e 2 . . . . e e e e . . 
            . . . e e . . . . . . e f . . .
    """),
    SpriteKind.player)
info.set_life(4)
ship.set_stay_in_screen(True)
ship.bottom = 120
controller.move_sprite(ship, 100, 100)
effects.star_field.start_screen_effect()

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile_from_side(asteroids[randint(0, len(asteroids) - 1)], 0, 75)
    projectile.set_kind(SpriteKind.enemy)
    projectile.x = randint(10, 150)
game.on_update_interval(500, on_update_interval)
