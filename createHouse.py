#Creates a house within the minecraft enviorment

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()



def createHouse(size, amount):
    # Modify Current position to build house in front of you:
    x = pos.x+2
    y = pos.y
    z = pos.z
    while True:
            # Calculate midpoint of house in order to make windows, doors etc:
            midx = x + size/2
            midy = y + size/2
            # Build the outside of the house as a shell:
            woolColor = random.randrange(0,15)
            mc.setBlocks(x, y, z, x+size, y+size, z+size, block.WOOL.id, woolColor)
            # Clear inside of the house by turning it into air
            mc.setBlocks(x+1, y, z+1, x+size-2, y+size-1, z+size-2,block.AIR.id)
            # Clear space of the door:
            mc.setBlocks(midx-1, y+1, z, midx+1, y+4, z, block.AIR.id)
            # Create the windows:
            mc.setBlocks(x+3, y+size-3,z, midx-3, midy+3,z,block.GLASS.id)
            mc.setBlocks(midx+3, y+size-3, z, x+size-3, midy+3,z,block.GLASS.id)
            # Time for a carpet!:
            mc.setBlocks(x+1, y, z+1, x+size-2, y, z+size-2, block.WOOL.id,1)

createHouse(10, 30)