# Problem 1
menu = {'lagman': 120, 'plov':120, 'borsh': 100}
menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']

print(menu)


# Problem 2
# users = {}

# for i in range(3):
#     name = input('login: ')
#     password = input('Password: ')
#     users[name] = password


# print(users)


# Problem 3
people = {'Argen': "engineer", "Adilet": "teacher", 'Albina' : 'artist', 'Nurgul': 'musician', 'Alisa': "designer"}

for k, v in people.items():
    print(f'Здравствуйте {k}. Прекрасная профессия {v}.')


# Problem 4
menu['besh_barmak'] = 130
menu['besh_barmak'] = 135

del menu['borsh']
print(menu)


# Problem 5
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuator',
'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
sacdic = {}

for i in range(len(south_american_countries)):
    sacdic[i+1] = south_american_countries[i]


print(sacdic)

