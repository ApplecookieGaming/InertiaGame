from scene import SpriteNode, Texture

MISSING_TEXTURE = Texture('assets/textures/missing_texture.png')

class Tile (SpriteNode):
	"""Base class. Is not used by itself"""
	def __init__(self, game, pos, size):
		self.size = size
		self.anchor_point = (0, 0)
		self.texture = MISSING_TEXTURE
		self.set_position(pos)
		game.add_child(self)
		
		self.bounce = 0
		self.friction = 0 # Must be a float between 0 and 1 (lower value = higher friction)
		self.health = 0
		
		self.setup()
	
	def setup(self):
		pass
		
	def set_position(self, pos):
		self.position = pos * self.size
	
	def get_bounce(self):
		return self.bounce
	
	def get_friction(self):
		return self.friction
	
	def get_health(self):
		return self.health
