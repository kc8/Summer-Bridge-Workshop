#Below are different examples of how to use the Minecraft API
import mcpi.minecraft as minecraft
import mcpi.block as block


mc= minecraft.Minecraft.create()
pos = mc.player.getTilePos()

#Players position (It is included in the most defs making it easier to copy and paste
x = pos.x
y = pos.y
z = pos.z

def getYourCurrentPos():
	'''Returns current position of player'''
   x = pos.x
   y = pos.y
   z = pos.z
   return x,y,z


def teleport(x,y,z):
    '''Teleport any where in the world, takes cordinates x,y,z as parameter'''
    mc.player.setTilePos(x,y,z)
    return

def createHouse(size):
    '''Will create a house at player x position + 2.
    Takes the size of the house as a parameter (size 10 is a two story house)
    Builds a very simple house'''
    # Modify Current position to build house in front of you:
    x = pos.x+2
    y = pos.y
    z = pos.z
    # Calculate mid point of house in order to make windows, doors etc
    midx = x + size/2
    midy = y + size/2
    # Build the outside of the house as a shell
    mc.setBlocks(x, y, z, x+size, y+size, z+size, block.WOOD_PLANKS.id)
    # Clear inside of the house by turning it into air
    mc.setBlocks(x+1, y, z+1, x+size-1, y+size-1, z+size-1, block.AIR.id)
    # Clear space of the door
    mc.setBlocks(midx-1, y+1, z, midx+1, y+4, z, block.AIR.id)
    # Create the windows
    mc.setBlocks(x+3, y+size-3,z, midx-3, midy+3,z,block.GLASS.id)
    mc.setBlocks(midx+3, y+size-3, z, x+size-3, midy+3,z, block.GLASS.id)
    # Time for a carpet!
    mc.setBlocks(x+1, y, z+1, x+size-1, y, z+size-1, block.WOOL.id,1)

def hollowCube(size):
	'''Creates a cube with nothing inside''' 
    x = pos.x+2
    y = pos.y
    z = pos.z
    # Build the outside
    mc.setBlocks(x, y, z, x+size, y+size, z+size, block.WOOL.id, 2)
    # Clear inside
    mc.setBlocks(x+1, y+1, z+1, x+size-1, y+size-1, z+size-1, block.AIR.id)

def solidCube(size):
	'''creates a solid cube'''
    x = pos.x+2
    y = pos.y
    z = pos.z
    mc.setBlocks(x, y, z, x+size, y+size, z+size, block.WOOL.id, 4)


def drawSphere(x1, y1, z1, radius, blockType, blockData=0):
	'''Draw a sphere, takes: x pos, y pos, z pos, radius, block type, and id'''
    for x in range(radius*-1,radius):
        for y in range(radius*-1, radius):
            for z in range(radius*-1,radius):
                if x**2 + y**2 + z**2 < radius**2:
                    mc.setBlock(x1 + x, y1 + y, z1 + z, blockType, blockData)


def create_flower_path():
	'''Should add flower MAY NOTR BE WORKING!!!! It is old'''
    stop = 0
    while stop < 100:
        pos = mc.player.getPos()
        x = pos.x
        y = pos.y
        z = pos.z
        block = 38 #flow block 
        mc.setBlock(x,y,z,block)
        time.sleep(0.2)
        stop += 1

def wall(size):
	'''Creates a wall, add a z to make it a solid cube '''
   wood = block.WOOD_PLANKS
   for x in xrange(0, size):
      for y in xrange(0,size):
         mc.setBlock(pos.x - x, pos.y + y, pos.z +z, wood)
