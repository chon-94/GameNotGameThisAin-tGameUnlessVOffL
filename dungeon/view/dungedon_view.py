class DungeonView:
    def __init__(self, game):
        self.game = game

    def display_room(self):
        room = self.game.get_current_room()
        print(f"\n{room.name}\n{room.description}\n")

    def display_enemy(self, enemy):
        print(f"A {enemy.name} appears!")

    def display_battle_options(self):
        return input("Do you want to attack (a) or flee (f)? ")

    def display_attack_result(self, message):
        print(message)

    def display_enemy_attack(self, message):
        print(message)

    def display_game_over_message(self, message):
        print(message)
