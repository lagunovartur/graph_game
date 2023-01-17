from game import Game
from labirinth import LabirinthFrame

if __name__ == '__main__':
    game = Game()
    game.current_frame = LabirinthFrame()
    game.start()