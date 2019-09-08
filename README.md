# More Practice

### Date: 9/6/19

### Summary

The `frequency_pattern` files are some algorithms practice. The `rpg-v2.py` is yesterdays RPG that includes expanded functionality. Part of the assignment was to add more characters, purchasing of items, and use of items before a battle. My favorite character is the Comedian. I'd consider this a working rough draft for now. Plenty of opportunity to refactor and make it more organized and re-examine the characters' attributes to make sure the game is somewhat balanced.

The requirements for the assignment are included below:

1. make the hero generate double damage points during an attack with a probability of 20%
2. make a new character called Medic that can sometimes recuperate 2 health points after being attacked with a probability of 20%
3. make a character called Shadow who has only 1 starting health but will only take damage about once out of every ten times he is attacked.
4. make a Zombie character that doesn't die even if his health is below zero
5. come up with at least two other characters with their individual characteristics, and implement them.
6. Give each enemy a bounty. For example, the prize for defeating the Goblin is 5 coins, for the Wizard it is 6 coins.

Items

1. make a SuperTonic item to the store, it will restore the hero back to 10 health points.
2. add an Armor item to the store. Buying an armor will add 2 armor points to the hero - you will add "armor" as a new attribute to hero. Every time the hero is attacked, the amount of hit points dealt to him will be reduced by the value of the armor attribute.
3. add an Evade item to the store. Buying an "evade" will add 2 evade points to the hero - another new attribute on the Hero object. The more evade he has, the more probable that he will evade an enemy attack unscathed. For example: 2 evade points: 10% probably of avoiding attack, 4 evade points: 15% probability of avoiding attack. It should never be possible to reach 100% evasion though.
4. come up with at least two other items with their unique characteristics and implement them. You can add more attributes to the hero or the characters.

Bonus

1. allow items to be used on the battle field. The hero can carry the items with him, and you have the option of choosing to use a tonic at any turn in a battle.
2. make a Swap item, which when used on a battle field, will swap the power values of the two characters for one turn.
