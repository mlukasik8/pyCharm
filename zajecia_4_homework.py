import random
import datetime


# Listy zawierające dane do losowania
female_fnames = ['Kate', 'Agnieszka', 'Anna', 'Maria', 'Joss', 'Eryka']
male_fnames = ['James', 'Bob', 'Jan', 'Hans', 'Orestes', 'Saturnin']
surnames = ['Smith', 'Kowalski', 'Yu', 'Bona', 'Muster', 'Skinner', 'Cox', 'Brick', 'Malina']
countries = ['Poland', 'United Kingdom', 'Germany', 'France', 'Other']

current_year_ = datetime.datetime.now().strftime("%Y")
random_user_list=[]

print(current_year_)
for i in range(0,10):

     firstname = random.choice(female_fnames) if i<5 else random.choice(male_fnames)

     lastname = random.choice(surnames)
     age = random.randint(5, 45)
     email = f'{firstname}.{lastname}@example.com'
     country = random.choice(countries)
     adult = True if age>=18 else False

     random_user_list.append({
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'age': age,
        'country': country,
        'adult': adult


})


for user in random_user_list:
    print(f"Hi! I'm {user['firstname']} {user['lastname']}. "
          f"I come from {user['country']} and I was born "
          f"in {int(current_year_) - user['age']}")
