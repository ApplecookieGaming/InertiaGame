from scene import Scene, run
from map_loader import MapLoader

class Main (Scene):
	def setup(self):
		MapLoader.store_maps(self)
		MapLoader.load_map(self, 'map0')
		
		self.player = MapLoader.get_player(self)
	
	def update(self):
		self.player.update()

if __name__ == '__main__':
	run(Main(), show_fps=True)
