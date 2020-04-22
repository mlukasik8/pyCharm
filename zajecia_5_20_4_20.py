import random

"""found= False
number = 0
while not found:
    number = random.randint(1, 10000)
    found = number%13 ==0
    print(number)


numbers_list = [1, 3, 5, 9, 15, 17, 90]
numbers_squared_list = []
for n in numbers_list:

    if n%3==0:
        numbers_squared_list.append(n**2)


numbers_squared_by_lc = [n**2 for n in numbers_list if n % 3 == 0]  # list comprehension
print(numbers_squared_by_lc)
"""

# Zadanie 1
"""
laws_of_robotics = [
    'A robot may not injure a human being or, through inaction, allow a human being to come to harm.',
    'A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.',
    'A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.',
]
new_first_law = 'No machine may harm humanity; or, through inaction, allow humanity to come to harm.'
zeroth_law = 'A robot may not injure humanity, or, by inaction, allow humanity to come to harm.'

laws_of_robotics[0] = new_first_law
laws_of_robotics.insert(0, zeroth_law)
print('Four Laws Of Robotics: ')

for i, law in enumerate(laws_of_robotics):
    print(f'{i}. {law}')
"""

# Zadanie 2
places = {
    'Aurora': {
        'age': 20_000,
        'description': 'Originally named New Earth, in later millennia the planet would be renamed "Aurora", which means "dawn", to signify the dawning of a new age for the Spacer culture.'
    },
    'Dahl': {
        'age': 1000,
        'description': 'Dahl is a district of Trantor. It is a small and rather down-trodden sector, which does not necessarily seem politically ambitious.'
    },
    'Cinna': {
        'age': 2000,
        'description': 'Cinna is the native planet of Dors Venabili.'
    },
    'Helicon': {
        'age': 10_000,
        'description': 'Helicon is the native planet of Hari Seldon. As the character says, Helicon is characterized by her Fight Abilities.'
    }
}

oldest_place= None
max_age =  0

for place, place_detail_dict in places.items():
    if place_detail_dict['age'] >max_age:
        max_age= place_detail_dict['age']
        oldest_place=place
print(f" the oldest place is {oldest_place}"
      f" description {places[oldest_place]['description']}")


# Zadanie 3
heroes = [
    {
        'name': 'Hari Seldon',
        'robot': True,
        'math': 10,
        'history': 4,
        'origin': 'Helicon'
    },
    {
        'name': 'Yugo Amaryl',
        'robot': False,
        'math': 10,
        'history': 1,
        'origin': 'Dahl'
    },
    {
        'name': 'Dors Venabili',
        'robot': True,
        'math': 3,
        'history': 9,
        'origin': 'Cinna'
    },
    {
        'name': 'R. Daneel Olivaw',
        'robot': True,
        'math': 8,
        'history': 10,
        'origin': 'Aurora'
    },
    {
        'name': 'Raych Seldon',
        'robot': False,
        'math': 3,
        'history': 5,
        'origin': 'Dahl'
    },
]

origin_count_dict = {}

for hero in heroes:
    if hero['origin'] in origin_count_dict.keys():
        origin_count_dict[hero['origin']] +=1
    else:
        origin_count_dict[hero['origin']]= 1

print(origin_count_dict)
sorted_origins_count= sorted(origin_count_dict, key=origin_count_dict.get, reverse=True)
print(sorted_origins_count[0])








