
from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block

while True:
	x,y,z = mc.player.getPos()
	bb=mc.getBlock(x,y-1,z)
	if bb==stone:
		mc.setBlock(x,y,z, lava)
	else:
		mc.setBlock(x,y-1,z, stone)
