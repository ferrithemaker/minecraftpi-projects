# Script By Ferran Fabregas (ferri.fc@gmail.com)

from mcpi import minecraft,block,event
import time

# Init Minecraft World
mc=minecraft.Minecraft.create()
mc.postToChat("Welcome to death blast demo")

maxDistance = 16

while True:
	hitEvents = mc.events.pollBlockHits()
	for hitEvent in hitEvents:
		playerPos = mc.player.getPos()
		for xdistance in range(maxDistance):
			for zdistance in range(maxDistance):
				# throw the "vaporizer" blast
				for ydistance in range(4):
					mc.setBlock(playerPos.x-int(maxDistance/2)+xdistance,playerPos.y+ydistance,playerPos.z-int(maxDistance/2)+zdistance,block.AIR.id)

