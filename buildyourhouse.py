# Script By Ferran Fabregas (ferri.fc@gmail.com)

from mcpi import minecraft,block

# Init Minecraft World
mc=minecraft.Minecraft.create()
mc.postToChat("Welcome to Minecraft 'gold house' demo")

size = 10
distanceFromPlayer = 10

# Get player tile position
playerTile = mc.player.getTilePos()
xInitPos = playerTile.x
zInitPos = playerTile.z - distanceFromPlayer
yInitPos = playerTile.y - 1
# create a cube
for houseX in range(size):
    for houseY in range(size):
        for houseZ in range(size):
            mc.setBlock(xInitPos + houseX,yInitPos + houseY,zInitPos - houseZ,block.GOLD_BLOCK.id)
# empty the cube
for houseX in range(size-2):
    for houseY in range(size-2):
        for houseZ in range(size-2):
            mc.setBlock(xInitPos + houseX+1,yInitPos + houseY+1,zInitPos - houseZ-1,block.AIR.id)
# create the door
mc.setBlock(xInitPos,yInitPos + 1 ,zInitPos-int(size/2),block.AIR.id)
mc.setBlock(xInitPos,yInitPos + 1,zInitPos-int(size/2) + 1,block.AIR.id)
mc.setBlock(xInitPos,yInitPos + 2,zInitPos-int(size/2),block.AIR.id)
mc.setBlock(xInitPos,yInitPos + 2,zInitPos-int(size/2) + 1,block.AIR.id)
mc.setBlock(xInitPos,yInitPos + 3,zInitPos-int(size/2),block.AIR.id)
mc.setBlock(xInitPos,yInitPos + 3,zInitPos-int(size/2) + 1,block.AIR.id)