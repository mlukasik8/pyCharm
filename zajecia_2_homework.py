

#Zadanie 1
first_name = 'James'
last_name = 'Micheals'
email = 'jmichaels@example.com'
phone = '12343214433'
age = 44
print(f"My name is {first_name} {last_name}\nI'm {age} years old\nYou can contact me via email: {email} or phone: {phone}  ")

#Zadanie 2

pi = 3.1415
r= 20

circumference = 2*pi*r
area = pi *r**2

print(round(circumference,4), round(area,4))


#Zadanie 3

a=5
b = 13

c_2 =a**2+b**2

c=(a**2+b**2)**0.5
print(round(c,2))

p= a*b/2
o=a+b+c
print(f"Pole: {p}, Obwód: {round(o, 2)}")


#Zadanie 4



gender = 'female'
name='Marta'
age=22
can_use_promotion = gender = 'female' and age >65 or  age <=16 or age >=45
print(f'{name}, Can use promotion: {can_use_promotion} ')

gender = 'male'
name='Marian'
age=72
can_use_promotion = gender ='male' and age >= 65 or 20 <= age <= 40
print(f'{name}, Can use promotion: {can_use_promotion} ')

gender = 'female'
name='Ewa'
age=46
can_use_promotion = gender = 'female' and age >=65 or age <=16 or age >=45
print(f'{name}, Can use promotion: {can_use_promotion} ')

gender='male'
name='Tomek'
age=12
can_use_promotion = gender ='male' and age >= 65 or 20 <= age <= 40
print(f'{name}, Can use promotion: {can_use_promotion} ')

gender='male'
name='Janusz'
age=40
can_use_promotion = gender ='male' and age >= 65 or 20 <= age <= 40
print(f'{name}, Can use promotion: {can_use_promotion} ')




