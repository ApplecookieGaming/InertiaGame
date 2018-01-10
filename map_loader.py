from entity_player import EntityPlayer
from tile_unbreakable import TileUnbreakable
import pickle

# Save locations of maps
MAP0_FILE = 'data/maps/map0.data'
MAP1_FILE = 'data/maps/map1.data'

class MapLoader ():
	"""Class loads and stores maps"""
	
	def get_player(self):
		return self.player
	
	def load_map(self, map):
		"""
		Loads required map, defaults to map0
		
		Map data is stored in a list and pickled. When the map is unpickled, this code searches all the text and places the required tile/entity at the location. Tiles are stored in a list that is used to check for collisions.
		"""
		tiles = []
		
		# load the required map
		if map == 'map1':
			with open(MAP1_FILE, 'rb') as file:
				self.map = pickle.load(file)
		else:
			with open(MAP0_FILE, 'rb') as file:
				self.map = pickle.load(file)
		
		map_width = len(self.map[0])
		map_height = len(self.map)
		
		self.tile_size = (self.size.x / map_width, self.size.y / map_height)
		
		for y in range(len(self.map)):
			for x in range(len(self.map[y])):
				if self.map[y][x] == '@':
					self.player = EntityPlayer(self, (x, len(self.map)-1-y), self.tile_size)
				elif self.map[y][x] == '0':
					tile = TileUnbreakable(self, (x, len(self.map)-1-y), self.tile_size)
					tiles.append(tile)
		
		for t in tiles:
			self.player.tiles_append(t)
			
	def store_maps(self):
		"""Stores maps by pickling them"""
		
		map0 = ['00000000000000000000000000000000',
					  '0               @              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0             000000           0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '0                              0',
					  '00000000000000000000000000000000']
		
		with open(MAP0_FILE, 'wb') as file:
			pickle.dump(map0, file)
		
		map1 = ['                ',
					  '                ',
					  '                ',
					  '                ',
					  '                ',
					  '                ',
					  '        @       ',
					  '                ',
					  '                ',
					  '                ',
					  '      00000     ',
					  '                ']
		
		with open(MAP1_FILE, 'wb') as file:
			pickle.dump(map1, file)
