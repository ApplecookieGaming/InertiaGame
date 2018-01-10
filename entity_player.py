from scene import Texture, gravity
from entity import Entity

ACC = -1/80

ENTITY_PLAYER = Texture('assets/textures/entity_player.png')

class EntityPlayer (Entity):
	def setup(self):
		self.texture = ENTITY_PLAYER
		self.gravity = True
	
	def check_inputs(self):
		g = gravity()
		
		if abs(g.y) > 0.1:
			self.input = True
			self.acc.x += ACC * g.y
