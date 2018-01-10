from scene import Scene, Texture, SpriteNode, Vector2

MISSING_TEXTURE = Texture('assets/textures/missing_texture.png')
GRAVITY = -9.8/1000 # Acceleration of gravity
RAM_VEL = 0.2 # Velocity required to break tiles

class Entity (SpriteNode):
	"""Base class. Is not used by itself"""
	def __init__(self, game, pos, size):
		self.game = game
		self.size = size
		self.anchor_point = (0, 0)
		self.texture = MISSING_TEXTURE
		self.set_position(pos)
		game.add_child(self)
		
		self.pos = pos
		self.vel = Vector2(0, 0)
		self.acc = Vector2(0, 0)
		self.gravity = False
		
		self.tiles = [] # Used to check tiles for collision
		
		self.setup()
	
	def setup(self):
		pass
	
	def update(self):
		self.acc = Vector2(0, 0)
		self.input = False
		
		self.check_inputs()
		self.entity_motion()
		self.check_collisions()
		
		self.pos += self.vel
		self.set_position(self.pos)
	
	def check_inputs(self):
		pass
	
	def entity_motion(self):
		if self.gravity:
			self.acc.y += GRAVITY
		
		self.vel += self.acc
		# self.vel *= self.game.dt
	
	def check_collisions(self):
		bottom_left = (self.bbox.min_x, self.bbox.min_y)
		bottom_right = (self.bbox.max_x, self.bbox.min_y)
		top_left = (self.bbox.min_x, self.bbox.max_y)
		top_right = (self.bbox.max_x, self.bbox.max_y)
		
		bottom_left_collide = False
		bottom_right_collide = False
		top_left_collide = False
		top_right_collide = False
		
		x_ram = False # Horizontal ram
		y_ram = False # Vertical ram
		
		if abs(self.vel.x) > RAM_VEL:
			x_ram = True
		if abs(self.vel.y) > RAM_VEL:
			y_ram = True
		
		# Check where collisions are occuring
		for t in self.tiles:
			if t.bbox.contains_point(bottom_left):
				bottom_left_collide = True
				bounce = t.get_bounce()
				friction = t.get_friction()
				tile_health = t.get_health()
				
			if t.bbox.contains_point(bottom_right):
				bottom_right_collide = True
			
			if t.bbox.contains_point(top_left):
				top_left_collide = True
			
			if t.bbox.contains_point(top_right):
				top_right_collide = True
				bounce = t.get_bounce()
				friction = t.get_friction()
				tile_health = t.get_health()
		
		## Rebound off block
		# If the collision is at the bottom of the tile
		if (bottom_left_collide and bottom_right_collide):
			if self.vel.y < 0:
				self.vel.y *= bounce
				
				# Friction
				self.vel.x *= friction/1
					
		# If the collision is at the top of the tile
		if (top_left_collide and top_right_collide):
			if self.vel.y > 0:
				self.vel.y *= bounce
		# If the collision is at the left of the tile
		if (bottom_left_collide and top_left_collide):
			if self.vel.x < 0:
				self.vel.x *= bounce
		# If the collision is at the right of the tile
		if (bottom_right_collide and top_right_collide):
			if self.vel.x > 0:
				self.vel.x *= bounce
		
	def set_position(self, pos):
		self.position = pos * self.size
	
	def tiles_append(self, tile):
		self.tiles.append(tile)
