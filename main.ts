controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
        . . . . . . . . 
        . . . . . 1 . . 
        . . 1 . 1 1 . . 
        . . 1 1 1 . . . 
        . . . 1 1 1 . . 
        . . 1 1 1 . . . 
        . . . 1 1 . . . 
        . . . 1 1 . . . 
        `, ship, 0, -140)
    projectile.startEffect(effects.blizzard, 100)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    scene.cameraShake(4, 500)
    otherSprite2.destroy(effects.disintegrate)
    sprite2.startEffect(effects.fire, 200)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
    otherSprite.destroy(effects.disintegrate)
    info.changeScoreBy(1)
})
let projectile: Sprite = null
let ship: Sprite = null
let ememys = [sprites.food.smallIceCream, sprites.food.smallCake, sprites.food.bigDonut]
ship = sprites.create(img`
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
    `, SpriteKind.Player)
info.setLife(4)
ship.setStayInScreen(true)
ship.bottom = 120
controller.moveSprite(ship, 100, 100)
game.onUpdateInterval(500, function () {
    projectile = sprites.createProjectileFromSide(ememys[randint(0, ememys.length - 1)], 0, 75)
    projectile.setKind(SpriteKind.Enemy)
    projectile.x = randint(10, 150)
})
