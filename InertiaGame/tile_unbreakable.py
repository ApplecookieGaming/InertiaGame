from scene import *
from tile import *

TILE_UNBREAKABLE = Texture('assets/textures/tile_unbreakable.png')

class TileUnbreakable (Tile):
	def setup(self):
		self.texture = TILE_UNBREAKABLE
		self.bounce = -0.3
		self.friction = 0.96
		self.health = -1
