"""
HERO Game: Part 2

Exercise is to expand on the previous days RPG game. More characters, adding Items, etc.

"""
import random

# Parent class of both User Characters and Enemies


class Character(object):

    def __init__(self, health, power):

        self.health = health
        self.power = power

    def attack(self, enemy):
        medic_chance = random.random()
        # if the class you are attacking is a Medic
        if enemy.__class__.__name__ == 'Medic':
            if medic_chance <= 0.20:
                enemy.health -= self.power
                enemy.health += 2
                print("Your Medic special ability kicked in. You gained 2 health.")
        else:
            enemy.health -= self.power

    def alive(self):

        if self.health > 0:
            return True

    # Todo will need to expand this for other classes that are created

    def print_status(self):

        if self.__class__.__name__ == 'Hero':
            print(f"You have {self.health} health and {self.power} power.")
        elif self.__class__.__name__ == 'Zombie':
            print(
                f"The Zombie has {self.health} health and {self.power} power.")

# ! Below are the classes the user can choose to play as: Hero, Medic, Shadow


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


class Medic(Character):
    pass

# ! Below are the classes the user fights: Goblin, Zombie


class Zombie(Character):
    def never_die(self, enemy):
        if self.health <= 6:
            self.health = 6


# Todo
# Character Stats
hero_health = 10
hero_power = 5

medic_health = 10
medic_power = 3

# TODO Create all the character objects
# Character Objects
our_hero = Hero(hero_health, hero_power)
medic = Medic(medic_health, medic_power)

# Enemy Stats
zombie_health = 6
zombie_power = 3

# TODO Create all enemy objects
# Enemy Objects
zombie = Zombie(zombie_health, zombie_power)

# Dictionary of Initialized Characters
character_dict = {
    1: our_hero,
    2: medic
}

# TODO We can randomly select an enemy for our hero to face!
# TODO Store all of the Enemy Objects in an empty array.
enemy_list = []
enemy_list.append(zombie)


def main():
    # ! Make sure this text keeps up to date with how many User Character options there are
    print(f"""
    Welcome to Nep's RPG Game. Please choose to play as either a Hero or Medic.
    A Hero has {our_hero.health} health and {our_hero.power} power.
    A Medic has {medic.health} health and {medic.power} power. 
    Medic's can some times regenerate 2 health when they're attacked.
    """)

    character_choice = int(input("Type 1 for Hero. Type 2 for Medic >> "))

    user_character = character_dict[character_choice]
    print()
    while zombie.alive() and user_character.alive():
        user_character.print_status()
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
