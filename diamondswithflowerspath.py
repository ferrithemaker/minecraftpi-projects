# Script By Ferran Fabregas (ferri.fc@gmail.com)

from mcpi import minecraft,block

# Init Minecraft World
mc=minecraft.Minecraft.create()
mc.postToChat("Welcome to Minecraft 'diamond with flowers path' demo")

while True:
    # Get player tile position
    playerTile = mc.player.getTilePos()
    # Transform player tile floor to DIAMOND_BLOCK with FLOWER_YELLOW over
    mc.setBlock(playerTile.x,playerTile.y-1,playerTile.z,block.DIAMOND_BLOCK.id)
    mc.setBlock(playerTile.x,playerTile.y,playerTile.z,block.FLOWER_YELLOW.id)