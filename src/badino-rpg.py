import random

player = input("enter player name:")
print(f"Welcome, {player}, good luck!")

player_hp = 200
player_damage = random.randint(1, 100)
import random

Weapon = [

   { "name" : "wood sword",
    "wood sworddamage" : player_damage * 0.1,
    "drop_chance" : 0.5
   },
   { "name" : "wood large sword",
    "wood large sword damage" : player_damage * 0.3,
    "drop_chance" : 0.3
   },
   { "name" : "giant axe",
    "giant axe damage" : player_damage * 0.5,
    "drop_chance" : 0.12
    },

]


monsters = ["goblin", "troll", "baby dragon", "orc", "baboon"]
goblin_hp = 250
goblin_damage = random.randint(1, 40)

troll_hp = 300
troll_damage = random.randint(1, 60)

baby_dragon_hp = 332
baby_dragon_damage = random.randint(1, 50)

orc_hp = 400
orc_damage = random.randint(1, 70)

baboon_hp = 150
baboon_damage = random.randint(1, 30)

firstmonster = random.choice(monsters)

print(f"A {firstmonster} apperared in frot of you!!")
if firstmonster == "goblin":
    monster_hp = goblin_hp
    monster_damage = goblin_damage
elif firstmonster == "troll":
    monster_hp = troll_hp
    monster_damage = troll_damage
elif firstmonster == "baby_dragon":
    monster_hp = baby_dragon_hp
    monster_damage = baby_dragon_damage
elif firstmonster == "orc":
    monster_hp = orc_hp
    monster_damage = orc_damage
elif firstmonster == "baboon": 
    monster_hp = baboon_hp
    monster_damage = baboon_damage
    
while  monster_hp > 0 and player_hp > 0:
    surprise_answer = input("wanna a surprise? (yes/no): ")
    if surprise_answer == "yes":
        Weapon_drop = random.choices(Weapon, weights=[weapon["drop_chance"] for weapon in Weapon], k=1)
        dropped_weapon = Weapon_drop[0]
        print(f"you found a {dropped_weapon['name']}")
        weapon_damage = list(dropped_weapon.values())[1]   
        print(f"your weapon does {weapon_damage} damage")
        break  # Exit the surpribrse weapon loop
    else:
        if surprise_answer == "no":
            weapon_damage = 0
            print("you choose no weapon")
            break  # Exit the surprise weapon loop
    if surprise_answer != "yes" and surprise_answer != "no":
        print("invalid answer, please enter yes or no")
        continue  # Prompt the user again for a valid answer
    


while monster_hp > 0 and player_hp > 0:
    ready = input(f"are you ready to fight {player}? (yes/no): ")
    if ready == "yes":
        print("fight started!")
    while monster_hp > 0 and player_hp > 0:
        input("press enter to attack:")
        monster_hp -= player_damage + weapon_damage
        print(f"you dealt {player_damage + weapon_damage} damage to the {firstmonster}")
        player_hp -= monster_damage
        print(f"the {firstmonster} dealt {monster_damage} damage to you")
        if monster_hp <= 0:
            print(f"you defeated the {firstmonster}!")
            break
        elif player_hp <= 0:
            print("you have been defeated!")
            break
    if ready == "no":
        print("you fled the battle!")
        break
        if ready != "yes" and ready != "no":
            print("invalid answer, please enter yes or no")
            continue  # Prompt the user again for a valid answer   
        else:
            continue # Prompt the user again for a valid answer