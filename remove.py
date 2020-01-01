#Turns objects in a set location into 'air', effectivley removing them. 
#Can you do the following:
#Create a defenition for this? Maybe give it parameters and arguments? 
#Change the size, can you change the shape? 

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


mc.setBlocks(pos.x, pos.y, pos.z, pos.x - 80, pos.y + 30, pos.z-80, block.AIR.id)