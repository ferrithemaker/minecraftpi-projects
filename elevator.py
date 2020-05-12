# Script By Ferran Fabregas (ferri.fc@gmail.com)

from mcpi import minecraft,block
import time

# Init Minecraft World
mc=minecraft.Minecraft.create()
mc.postToChat("Welcome to Minecraft 'elevator' demo")

distance = 10
zDistanceFromPlayer = 10

# Get original player tile position
playerTile = mc.player.getTilePos()
xInitPos = playerTile.x
zInitPos = playerTile.z - zDistanceFromPlayer
yInitPos = playerTile.y - 1

while True:
    # go up
    for elevation in range(distance):
        mc.setBlock(xInitPos,yInitPos + elevation,zInitPos,block.GOLD_BLOCK.id)
        mc.setBlock(xInitPos,yInitPos + elevation,zInitPos + 1,block.GOLD_BLOCK.id)
        mc.setBlock(xInitPos + 1,yInitPos + elevation,zInitPos,block.GOLD_BLOCK.id)
        mc.setBlock(xInitPos + 1,yInitPos + elevation,zInitPos + 1,block.GOLD_BLOCK.id)
        # restore the air blocks under the elevator
        mc.setBlock(xInitPos,yInitPos + elevation -1,zInitPos,block.AIR.id)
        mc.setBlock(xInitPos,yInitPos + elevation -1,zInitPos + 1,block.AIR.id)
        mc.setBlock(xInitPos + 1,yInitPos + elevation -1,zInitPos,block.AIR.id)
        mc.setBlock(xInitPos + 1,yInitPos + elevation -1,zInitPos + 1,block.AIR.id)
        time.sleep(0.3)
    #go down
    for elevation in range(distance -1 , -1, -1):
        mc.setBlock(xInitPos,yInitPos + elevation,zInitPos,block.GOLD_BLOCK.id)
        mc.setBlock(xInitPos,yInitPos + elevation,zInitPos + 1,block.GOLD_BLOCK.id)
        mc.setBlock(xInitPos + 1,yInitPos + elevation,zInitPos,block.GOLD_BLOCK.id)
        mc.setBlock(xInitPos + 1,yInitPos + elevation,zInitPos + 1,block.GOLD_BLOCK.id)
        # restore the air blocks over the elevator
        mc.setBlock(xInitPos,yInitPos + elevation +1,zInitPos,block.AIR.id)
        mc.setBlock(xInitPos,yInitPos + elevation +1,zInitPos + 1,block.AIR.id)
        mc.setBlock(xInitPos + 1,yInitPos + elevation +1,zInitPos,block.AIR.id)
        mc.setBlock(xInitPos + 1,yInitPos + elevation +1,zInitPos + 1,block.AIR.id)
        time.sleep(0.3)