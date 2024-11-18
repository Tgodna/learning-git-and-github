import random
from functools import reduce


prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']


def capitalize_suffix(name):
    return name.capitalize()


capitalized_suffixes = list(map(capitalize_suffix, suffixes))


def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)


fantasy_names = []
for i in range(10):
    fantasy_name = create_fantasy_name(prefixes, capitalized_suffixes)
    fantasy_names.append(fantasy_name)


print('Fantasy Names:')
for name in fantasy_names:
    print(name)


print()  

def pure_fire_in_name(name):
    return 'fire' in name.lower()  


fire_in_name = list(filter(pure_fire_in_name, fantasy_names))


print(f"Filtered names with 'Fire': {fire_in_name}")


def pure_concatenate_names(name1, name2):
    return name1 + ' ' + name2


concatenated_name = reduce(pure_concatenate_names, fantasy_names)


print(f"Concatenated names: {concatenated_name}")
