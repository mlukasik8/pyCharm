# print('Today is Friday')
# is_day =False
# if is_day:
#     print('Good Morning')
# else:
#     print('Good night')
#
# temp_celsius=0
# pressure_hpa=1013
# if temp_celsius==0 and pressure_hpa ==1013:
#     print('In water freezing point')
# else:
#     print('Not in water freezing')
#
# price =100
# free_product=False
# cash_amount=101
# if free_product:
#     print('You get the product for free.')
# elif cash_amount>=price:
#     print('You can buy this product.')
#
# else:
#     print(f'You need {price-cash_amount} more cash to buy this product.')
#
# for i in range(100):
#     print(i)
# for i in range(101, 1, -1):
#         print(i**2)
# for i in range (11,28):
#     print(i**3)

names=['janek', 'monika', 'adam']
for name in names:
    print(name.capitalize())

numbers=[3, 12, 55, 178, 1300, 6789, 19200]

for i in numbers:
    print(i*3)

login = 'admin12344'
for c in login:
    if c.isdigit():
        print(c)
    else:
        print(c.upper())
# zadanie 6
for i  in numbers:
    if i %3==0:
        print(i)




