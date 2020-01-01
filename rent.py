import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
mc = minecraft.Minecraft.create()

X1 = 0
Z1 = 10
X2 = 40
Z2 = 40

HOME_X = X2 + 2
HOME_Y = 10
HOME_Z = Z2 + 2

rent = 0 #Holds told rent
inField = 0 #Hold the seconds they are in the area
wood = block.WOOD_PLANKS
mc.setBlock(30, 11, 1, block.DIAMOND_BLOCK.id)
diamond_pos = mc.player.getTilePos()

def checkHit():
    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        if pos.x == diamond_pos.x and pos.y == diamond_pos.y and pos.z == diamond_pos.z:
            mc.postToChat("HIT")

for z in range(0,40):
    for x in range(0,40):
        mc.setBlock(X1 + x, 10, Z1 - z, wood)
    
while True:
    checkHit()
    time.sleep(1)

    pos = mc.player.getTilePos()

    if pos.x>X1 and pos.x<X2 and pos.z<Z1 and pos.z<Z2:
            rent += 1
            mc.postToChat("You now owe: " + str(rent))
            inField = inField + 1
    else:
            inField = 0
    if inField>3:
        mc.postToChat("To Slow!!!")
        mc.player.setPos(HOME_X, HOME_Y, HOME_Z)