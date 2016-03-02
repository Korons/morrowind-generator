#eggplant
#aubergine
from random import choice
from random import randint
from random import shuffle
attributenum = randint(0,7)
skillnum = randint(0,26)

# Birth signs
signs = ["tower", "shadow", "lover", "ritual", "atronach", "apprentice", "lord", "steed", "lady", "serpent", "thief", "mage",
 "warrior"]

 # Skills
skills = ["heavy armour", "medium armour", "spear", "acrobatics", "armourer", "axe", "blunt", "long blade",
"block", "light armour", "marksman", "sneak", "athletics", "hand-to-hand", "short blade", "unarmoured", "illusion",
"mercantile", "speechcraft", "alchemy", "conjuration", "enchant", "security", "alteration", "destruction", "mysticism", "restoration"]

# Races
races = ["altmer", "argonian", "bosmer", "breton", "dunmer", "imperial", "khajiit", "nord", "orc", "redguard"]

# Attributes
attributes = ["agility", "endurance", "intelligence", "luck", "personality", "speed", "strength", "willpower"]
print("Your race is " + choice(races))
print("\nYour birthsign is " + choice(signs))

# These are for the skill loops below
skillcalc = 0
attributecalc = 0

# These randomize the skills and attributes lists
skill_order = skills[:]
shuffle(skill_order)
attribute_order = attributes[:]

# We use .pop() so we don't print the same item twice
print("\nYour major skills are as follows:")
for skillcalc in range(0,5):
	print(skill_order.pop())
	skillcalc + 1
print("\nYour minor skills are as follows:")
skillcalc = 0
for skillcalc in range(0,5):
	print(skill_order.pop())
	skillcalc + 1
print("\nYour primary attributes are as follows:")
for attributecalc in range(0,2):
	print(attribute_order.pop())
	attributecalc + 1
