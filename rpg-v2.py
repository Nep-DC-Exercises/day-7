"""
HERO Game: Part 2

Exercise is to expand on the previous days RPG game. More characters, adding Items, etc.

"""
import random
import time

# Parent class of both User Characters and Enemies


class Character(object):

    def __init__(self, health, power):

        self.health = health
        self.power = power
        self.evade_points = 0
        self.coins = 0
        self.inventory = []
        self.armor_points = 0

    def attack(self, enemy):

        # The max points a character can have is 6
        evade_lookup = {
            2: 0.10,
            4: 0.20,
            6: 0.30
        }
        evade_chance = random.random()

        # Check to see if we can avoid the attack entirely because of evade points present
        try:
            if enemy.evade_points > 0:

                user_chance_of_evasion = evade_lookup[enemy.evade_points]

                if evade_chance <= user_chance_of_evasion:
                    print("The enemy missed thanks to your evade points.")
                    return

            # If there's no evade points, check to see if there's any armor
            elif enemy.armor_points > 0:
                reduced_damage = self.power - enemy.armor_points
                enemy.health -= reduced_damage
                print("That armor helps.")
                print(
                    f"You lose {reduced_damage} health instead of {self.power} health.")

            # If there's no armor or evade points, it's just a normal attack
            else:
                enemy.health -= self.power
        # if the enemy doesn't have any evade points, which are all the monsters, treat it like a regular attack
        except AttributeError:
            enemy.health -= self.power

    def alive(self):

        if self.health > 0:
            return True

    def print_status(self):
        i = 0
        user_characters = ['Hero', 'Medic', 'Shadow', 'Knight', 'Comedian']
        # if the class is a user character
        if self.__class__.__name__ in user_characters:

            print(f"You have {self.health} health and {self.power} power.")

            for i in range(len(self.inventory)):
                print(
                    f"You have: {self.inventory[i].__class__.__name__} in your inventory.")

            print(f"You have {self.coins} coins.")

        else:
            print(
                f"The {self.__class__.__name__} has {self.health} health and {self.power} power.")

    def buy_item(self, item):

        if self.coins >= item.cost:
            self.inventory.append(item)
            self.coins -= item.cost
            return True
        else:
            return False

# User Classes: Hero, Medic, Shadow, Knight, Comedian


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

    def medic_power(self):
        # Medics have a 20% chance of gaining health at the end of each turn
        medic_chance = random.random()
        if medic_chance <= 0.20:
            self.health += 2
            print("Your medic special ability kicked in. You gained 2 health.")


class Shadow(Character):
    pass


class Knight(Character):

    def attack(self, enemy):
        knight_chance = random.random()
        # Knights will miss their attack 60% of the time
        if knight_chance <= 0.60:
            print("Swing and a miss. Better luck next time.")
        else:
            print(
                f"You got him! {enemy.__class__.__name__} loses {self.power} health.")
            enemy.health -= self.power


class Comedian(Character):

    def attack(self, enemy):
        laugh_chance = random.random()
        # lol this is my favorite character
        jokes = [
            "I made a pencil with two erasers. It was pointless.",
            "How do you make a Kleenex dance? Put a little boogie in it!",
            "What do you get from a pampered cow? Spoiled Milk.",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "How do you get a squirrel to like you? Act like a nut.",
            "My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right!",
            "Did you hear the rumor about butter? Well, I'm not going to spread it!",
            "Why can't a nose be 12 inches long? Because then it would be a foot.",
            "Did you hear about the circus fire? It was in tents.",
            "What’s an astronaut’s favorite part of a computer? The space bar.",
            "Spring is here! I got so excited I wet my plants.",
            "Don't trust atoms. They make up everything!"
        ]
        print(
            f"You come up with a joke to tell the {enemy.__class__.__name__}.")

        print(random.choice(jokes))

        print("Was it funny?")

        time.sleep(5)

        if laugh_chance <= 0.50:
            print(
                f"It worked! The {enemy.__class__.__name__} laughs really hard and loses {self.power} health!")
            enemy.health -= self.power
        else:
            print(
                f"The {enemy.__class__.__name__} groans. The joke wasn't very funny unfortunately.")


# Enemy Classes: Goblin, Wizard, Zombie

class Goblin(Character):

    def __init__(self, health, power, bounty):
        self.health = health
        self.power = power
        self.bounty = bounty


class Wizard(Character):

    def __init__(self, health, power, bounty):
        self.health = health
        self.power = power
        self.bounty = bounty


class Zombie(Character):

    def __init__(self, health, power, bounty):
        self.health = health
        self.power = power
        self.bounty = bounty

    def never_die(self, enemy):
        if self.health <= 6:
            self.health = 6
            print("The Zombie immediately regenerates health.")

# Item Classes: Supertonic, Armor, Evade, Poison, Swap


class Supertonic:

    def __init__(self):
        self.cost = 5
        self.health_boost = 10

    def use(self, user):
        user.health += self.health_boost
        user.inventory.remove(self)
        print(
            f"You feel a nice buzz. Your health increased by {self.health_boost}.")


class Armor:

    def __init__(self):
        self.cost = 8
        self.points = 2

    def use(self, user):
        user.armor_points += self.points
        print("You now have armor. That should take the sting off some attacks.")
        user.inventory.remove(self)


class Evade:

    def __init__(self):
        self.cost = 9
        self.points = 2

    def use(self, user):

        if user.evade_points >= 6:
            print("You cannot have more than 6 evade points. Don't buy any more.")
            user.evade_points = 6

        else:
            user.evade_points += self.points
            print("You feel a little lighter on your feet. Might avoid some attacks.")

        user.inventory.remove(self)


class Poison:

    def __init__(self):
        self.cost = 10

    def use(self, user, enemy):

        if enemy.__class__.__name__ != "Zombie":
            print("You poisoned the enemy.")
            enemy.health = 0
            print(f"Their health is now {enemy.health}.")
            print("You'll attack them once more anyway to make sure.")

            user.inventory.remove(self)

        else:
            print("You can't poison an undead creature. Sorry.")


class Swap:

    def __init__(self):
        self.cost = 8

    def use(self, user, enemy):
        # using temporary variables to help with the switcharoo
        a = user.power
        b = enemy.power
        user.power = b
        enemy.power = a
        print(f"You now have {user.power} power.")
        print(f"Your opponent now has {enemy.power} power.")
        user.inventory.remove(self)


# Character Stats
hero_health = 10
hero_power = 4

medic_health = 8
medic_power = 3

shadow_health = 1
shadow_power = 2

knight_health = 15
knight_power = 5

comedian_health = 10
comedian_power = 2

# Character Objects
hero = Hero(hero_health, hero_power)
medic = Medic(medic_health, medic_power)
shadow = Shadow(shadow_health, shadow_power)
knight = Knight(knight_health, knight_power)
comedian = Comedian(comedian_health, comedian_power)

# Enemy Stats
goblin_health = 6
goblin_power = 2
goblin_bounty = 5

wizard_health = 8
wizard_power = 4
wizard_bounty = 6

zombie_health = 6
zombie_power = 3
# Actually irrelevant for a zombie since they can't die
zombie_bounty = 100


# Dictionary of Initialized Characters
character_dict = {
    1: hero,
    2: medic,
    3: shadow,
    4: knight,
    5: comedian
}


# MAIN GAMEPLAY

def main():
    # Enemy Objects
    goblin = Goblin(goblin_health, goblin_power, goblin_bounty)
    zombie = Zombie(zombie_health, zombie_power, zombie_bounty)
    wizard = Wizard(wizard_health, wizard_power, wizard_bounty)

    # List of enemies
    enemy_list = [goblin, zombie, wizard]

    print(f"""
    Welcome to Nep's RPG Game.
    You get to play as a Hero, Medic, Shadow, Knight, or Comedian.
    You'll fight monsters and get money on this quest.
    Here's some information on each character.

    A Hero has {hero.health} health and {hero.power} power.
    \t The hero can sometimes deal double damage points.\n
    A Medic has {medic.health} health and {medic.power} power.
    \t Medics can sometimes regenerate 2 health when they're attacked.\n
    A Shadow has {shadow.health} health and {shadow.power} power.
    \t Shadows only take damage 10% of the time.\n
    A Knight has {knight.health} health and {knight.power} power.
    \t Knights are strong but sometimes they miss.\n
    A Comedian has {comedian.health} health and {comedian.power} power.
    \t Comedians don't fight. They tell jokes.\n
    """)

    # If the user types in something thats not 1 - 5, they're stuck in a loop until they do.
    while True:
        character_choice = int(
            input("Type 1 for Hero. 2 for Medic. 3 for Shadow. 4 for Knight. 5 for Comedian. >> "))
        print("\n")
        try:
            user_character = character_dict[character_choice]
            print(f"You chose {user_character.__class__.__name__}.")
            break
        except:
            print("Please just type a single number between 1 - 5.")

    print()

    # Choose a monster at random
    random_monster = random.choice(enemy_list)
    print(f"A {random_monster.__class__.__name__} appears.")

    # The main fighting loop
    while random_monster.alive() and user_character.alive():

        user_character.print_status()
        random_monster.print_status()
        time.sleep(3)
        print()
        print("What do you want to do?")
        print("1. buy an item from the store")
        print(f"2. fight {random_monster.__class__.__name__}")
        print("3. do nothing")
        print("4. flee")
        print("> ",)
        user_input = input()

        if user_input == "1":
            # initialize item objects
            supertonic = Supertonic()
            armor = Armor()
            evade = Evade()
            poison = Poison()
            swap = Swap()

            # storing the item objects in a dictionary
            store_shelves = {
                "supertonic": supertonic,
                "armor": armor,
                "evade": evade,
                "poison": poison,
                "swap": swap,
            }
            print("===========    Welcome to the Store   ===========")
            print("The following are items in stock.")
            time.sleep(2)
            # Display the items available for purchase and how much they cost
            for i in store_shelves:
                print(i + " which costs " +
                      str(store_shelves[i].cost) + " coins.")
            time.sleep(2)
            # kick the user out of the store if they don't have cash money
            if user_character.coins == 0:
                print("You have no money. Go out there and fight.")
                print("===========   Exiting the Store   ===============\n")
                user_input = "2"
            else:
                print("\n")
                print("Would you like to purchase anything?")
                print("You can only buy one item at a time.")

                try:
                    item_purchase = input("Input the items name. >> ")
                    item_retrieval = store_shelves[item_purchase]
                    purchase_completion = user_character.buy_item(
                        item_retrieval)
                    if purchase_completion:
                        print("Purchase complete.")
                        print(f"You now have {user_character.coins} coins.")
                        print("===========   Exiting the Store   ===============\n")
                    else:
                        print("Sorry. It looks like you don't have enough coins.")
                        print("===========   Exiting the Store   ===============\n")
                    user_input = "2"
                except:
                    print("We don't have that in the store.")
                    print("You've overstayed your welcome. Get out.")
                    print("===========   Exiting the Store   ===============\n")

        if user_input == "2":

            if len(user_character.inventory) > 0:
                use_item = input(
                    "Would you like to use an item in your inventory? yes or no? >> ")
                if use_item == 'no':
                    pass
                elif 'yes':
                    try:
                        print("Here are all the items in your inventory.")
                        for i in range(len(user_character.inventory)):
                            print(
                                user_character.inventory[i].__class__.__name__ + " is in Location Number: " + str(i))

                        user_item_selection = int(
                            input("Input the location number of the item you want to use >> "))
                        selected_item = user_character.inventory[user_item_selection]

                        selected_item_class = selected_item.__class__.__name__
                        # Making sure that we are using the right arguments when calling the .use method.
                        if selected_item_class in ["Supertonic", "Armor", "Evade"]:
                            selected_item.use(user_character)

                        elif selected_item_class in ["Swap", "Poison"]:
                            selected_item.use(user_character, random_monster)

                        else:
                            print("Something went terribly wrong.")
                    except:
                        print("That item is not in your inventory.")
                else:
                    print("Invalid input.")

            print("You attack the monster.")
            user_character.attack(random_monster)

            if random_monster.__class__.__name__ == "Zombie":
                zombie.never_die(user_character)

            if random_monster.alive():
                pass

            else:
                user_character.coins += random_monster.bounty
                print(
                    f"You gained {random_monster.bounty} coins for defeating the enemy. You have {user_character.coins} coins now.")

                # New enemy objects need to be generated because if you defeat a goblin/wizard, and another goblin/wizard appears, their health persists and does not reset.
                goblin = Goblin(goblin_health, goblin_power, goblin_bounty)
                zombie = Zombie(zombie_health, zombie_power, zombie_bounty)
                wizard = Wizard(wizard_health, wizard_power, wizard_bounty)
                enemy_list = [goblin, wizard]
                random_monster = random.choice(enemy_list)
                time.sleep(4)
                print("\n\n")
                print(
                    f"But wait. A wild {random_monster.__class__.__name__} appears.")

        elif user_input == "3":
            pass

        elif user_input == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid input %r" % user_input)

        # Monster attack sequence
        if random_monster.alive():

            # Shadow special ability
            if user_character.__class__.__name__ == "Shadow":
                shadow_chance = random.random()
                if shadow_chance <= 0.10:
                    random_monster.attack(user_character)
                    print(
                        f"The enemy does {random_monster.power} damage to you.")

                else:
                    print(
                        "The enemy tried attacking you but missed and attacked your shadow.")

            else:
                print(f"The {random_monster.__class__.__name__} attacks you.")
                random_monster.attack(user_character)

            # Medic special ability
            if user_character.__class__.__name__ == "Medic":
                medic.medic_power()

            if not user_character.alive():
                print("You are dead.")

            user_input = "1"


main()
