import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.items = []

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

class Room:
    def __init__(self, name, description, enemies):
        self.name = name
        self.description = description
        self.enemies = enemies

class Game:
    def __init__(self, player):
        self.player = player
        self.rooms = [
            Room("Entrance", "You are standing at the entrance to the dungeon.", []),
            Room("Cavern", "You find yourself in a dark cavern.", [Enemy("Goblin", 50, 10)]),
            Room("Treasure Chamber", "You have found the treasure chamber!", [])
        ]
        self.current_room_index = 0

    def move_to_next_room(self):
        self.current_room_index += 1

    def get_current_room(self):
        return self.rooms[self.current_room_index]

    def is_battle_over(self, enemy):
        return enemy.hp <= 0 or self.player.hp <= 0

    def attack_enemy(self, enemy):
        damage = random.randint(5, 20)
        enemy.hp -= damage
        return f"You attack the {enemy.name} for {damage} damage."

    def get_enemy_attack_message(self, enemy):
        damage = enemy.damage
        self.player.hp -= damage
        return f"The {enemy.name} attacks you for {damage} damage."

    def is_game_over(self):
        return self.current_room_index == len(self.rooms) - 1 or self.player.hp <= 0

    def get_game_over_message(self):
        if self.player.hp <= 0:
            return "You died! Game over."
        else:
            return "Congratulations! You found the treasure and won the game."
