x, y = 10, -7

greater_number = max(x, y)
lesser_number = min(x, y)
print(lesser_number)

print(abs(121))

# Zadanie_1. Mając dane: a, b, c = 12.4, 3, -50
# oraz funkcje min(), abs(), print() wydrukuj wartość bezwzględną najmniejszej z nich.
# Czy potrafisz zrobić to w jednej linijce?

a, b, c = 12.4, 3, -50
print(abs(min(a, b, c)))

first_name = 'michał'
print(first_name.capitalize())
print(first_name.upper())
# 2. Używając zmiennych
# # # name, company = 'ricardo', 'fbi'
# # # oraz method upper() i capitalize()
# # # wydrukuj zdanie: "Officer Ricardo works for FBI"
name, company = 'rICARDO', 'fbi'
print(f'Officer {name.capitalize()} works for {company.upper()}')

# 3. Wykonaj poniższe:
#
# a. Stwórz listę swoich 5 ulubionych filmów
#
# b. Wydrukuj długość listy
#
# c. Wydrukuj 3 element tej listy
#
# d. Dodaj na koniec listy element “Joker”
#
# e. Wydrukuj ostatni element na liście
#
# # f. Wydrukuj dwa pierwsze elementy listy
my_favorite_movies = ['Pulp Fiction', 'Wolf of Wall Street', 'Star Wars', 'Moonlight', 'Inglorious Basterds', 'Miś', ]
print(len(my_favorite_movies))
print(f'Number 3 on my list is: {my_favorite_movies[2]}')
my_favorite_movies.append('Joker')
print(f'Last on my list is: {my_favorite_movies[-1]}')
# two_best =(*my_favorite_movies [0:2])
print(f'My two best movies are:{my_favorite_movies[0:2]}')

##Słowniki


# 4. Stwórz słownik opisujący Polskę, który będzie zawierał takie klucze:
#
# a. country_name
#
# b. language
#
# c. population
#
# d. capital
#
# e. famous_people
#
# {
#
# 'country_name': 'Italy', 'language': 'Italian', 'population': 60_360_000, 'capital': 'Rome', 'famous_people': ['Roberto Benigni', 'Leonardo da Vinci']
#
# }

my_country_poland = {
    'country_name': 'Poland',
    'language': 'Polish',
    'population': 38_000_000,
    'capital': 'Warszawa',
    'famous_people': ['Fryderyk Chopin', 'Lech Wałęsa']
}
my_country_france = {
    'country_name': 'France',
    'language': 'french',
    'population': 67_000_000,
    'capital': 'Paris',
    'famous_people': ['Voltaire', 'Maurice Ravel']
}
my_country_canada = {
    'country_name': 'Canada',
    'language': ['french','english'],
    'population': 36_700_000,
    'capital': 'Ottawa',
    'famous_people': ['Brian Addams', 'Lucy Maud Montgomery']
}
print(my_country_poland['country_name'])
my_country_poland['famous_people'].append('Andrzej Wajda')
print(my_country_france['famous_people'][-1])
country_list = [my_country_poland,my_country_france,my_country_canada]
print((country_list[-1]['capital'],country_list[0]['population']))

# 5. Utwórz listę 3 słowników zawierających opis krajów: Polska, Francja, Kanada. Następnie wydrukuj:
#
# a. Stolicę ostatniego kraju
#
# b. Populację pierwszego kraju