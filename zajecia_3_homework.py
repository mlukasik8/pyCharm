#1
primes= [2,3,5,7,11,13,17,19,23,29 ]
print(len(primes))
primes.append(31)
primes_four = primes[0:4]
print(primes_four[-1])
print(sum(primes)/sum(primes_four))

#2

list = [22, 3.3, -2, 5, 701, 42, -120, 35, 69.9, 123, -444, 0.0, 0]
sorted_list = sorted(list)
print(sorted_list[0],sorted_list[-1])

#3

favorite_band = {
    'name':'Wu-Tang Clan',
    'country':'Shaolin',
    'albums':['Enter the Wu-Tang 36 chambers', 'Forever','The W','Iron Flag'],
    'start_year': 1992,
    'albums_sold': 6_000_000,

}
favorite_band_2 = {
    'name':'Pearl Jam',
    'country':'Seattle',
    'albums':['Ten', 'Vs.','No Code','Yield'],
    'start_year': 1990,
    'albums_sold': 85_000_000,
}
favorite_band_3 = {
    'name':'Pearl Jam2',
    'country':'Seattle2',
    'albums':['Ten2', 'Vs.2','No Code2','Yield2'],
    'start_year': 1992,
    'albums_sold': 85_000_002,
}
favorite_band['active']=True
print(favorite_band)
favorite_band['albums'].append('Once Upon a Time in Shaolin')
print(favorite_band['albums'])
favorite_band['active']=False # to samo można zrobić tak: favorite_band['active'] = not favorite_band['active']

print(favorite_band)
favorite_band['albums_sold']+=1
print(favorite_band['albums_sold'])

#4
bands = [favorite_band,favorite_band_2,favorite_band_3]
print(bands[-1]['country'])
print(bands[1]['albums'][1])
print(bands[0]['active'])
