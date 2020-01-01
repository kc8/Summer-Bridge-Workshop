#creates a stack of Wool

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

def coloredTower():
    while True:
        woolColor = random.randrange(0,15)
        for a in range(60):
            mc.setBlock(pos.x+3, pos.y+a, pos.z, block.WOOL.id, woolColor)

coloredTower()