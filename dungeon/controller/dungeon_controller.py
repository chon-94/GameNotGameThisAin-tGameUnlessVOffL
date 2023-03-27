from dungeon import Game
from dungeon_view import DungeonView

class DungeonController:
    def __init__(self):
        self.player_name = input("What is your name? ")
        self.game = Game(self.player_name)
        self.view = DungeonView(self.game)

    def run(self):
        while True:
            self.view.display_room()
            room = self.game.get_current_room()
            if room.enemies:
                for enemy in room.enemies:
                    self.view.display_enemy(enemy)
                    while True:
                        action = self.view.display_battle_options()
                        if action == "a":
                            self.view.display_attack_result(self.game.attack_enemy(enemy))
                            if self.game.is_battle_over(enemy):
                                break
                            self.view.display_enemy_attack
