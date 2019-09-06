"""
HERO Game: Part 2

Exercise is to expand on the previous days RPG game. More characters, adding Items, etc.

"""
import random


class Character(object):

    def __init__(self, health, power):

        self.health = health
        self.power = power

    def attack(self, enemy):

        enemy.health -= self.power

    def alive(self):

        if self.health > 0:
            return True

    def print_status(self):

        if self.__class__.__name__ == 'Hero':
            print(f"You have {self.health} health and {self.power} power.")
        elif self.__class__.__name__ == 'Zombie':
            print(
                f"The Zombie has {self.health} health and {self.power} power.")


class Hero(Character):

    # The hero can generate double damage during an attack with a probability of 20%
    def attack(self, enemy):
        hero_attack_chance = random.random()
        if hero_attack_chance <= 0.20:
            double_damage = self.power * 2
            enemy.health -= double_damage
            print(
                f"You do {double_damage} damage to the {enemy.__class__.__name__}.")
        else:
            enemy.health -= self.power
            print(
                f"You do {self.power} damage to the {enemy.__class__.__name__}.")


class Zombie(Character):
    def never_die(self, enemy):
        if self.health <= 6:
            self.health = 6


# Character Stats
hero_health = 10
hero_power = 5
zombie_health = 6
zombie_power = 3

# Character Objects
our_hero = Hero(hero_health, hero_power)
zombie = Zombie(zombie_health, zombie_power)


def main():
    while zombie.alive() and our_hero.alive():
        our_hero.print_status()
        zombie.print_status()

        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()

        if user_input == "1":
            our_hero.attack(zombie)
            zombie.never_die(our_hero)
            print(f"The Zombie immediately regenerates health.")

        elif user_input == "2":
            pass

        elif user_input == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid input %r" % user_input)

        if zombie.alive():

            zombie.attack(our_hero)
            print("The Zombie does %d damage to you." % zombie.power)
            if not our_hero.alive():
                print("You are dead.")


main()
