birds = [
    {'common_name': 'Grey Heron', 'latin_name': 'Ardea cinerea', 'size': 'large', 'main_colour': 'grey',
     'secondary_colour_1': 'white', 'secondary_colour_2': 'black'},
    {'common_name': 'Sparrowhawk', 'latin_name': 'Accipiter nisus', 'size': 'medium', 'main_colour': 'brown',
     'secondary_colour_1': 'beige', 'secondary_colour_2': 'white'},
    {'common_name': 'Ring-necked Parakeet', 'latin_name': 'Psittacula krameri', 'size': 'medium',
     'main_colour': 'green', 'secondary_colour_1': 'orange', 'secondary_colour_2': 'none'},
    {'common_name': 'Woodpigeon', 'latin_name': 'Columba palumbus', 'size': 'medium', 'main_colour': 'grey',
     'secondary_colour_1': 'white', 'secondary_colour_2': 'black'},
    {'common_name': 'Green Woodpecker', 'latin_name': 'Picus viridis', 'size': 'medium', 'main_colour': 'green',
     'secondary_colour_1': 'red', 'secondary_colour_2': 'black'},
    {'common_name': 'Wren', 'latin_name': 'Troglodytes troglodytes', 'size': 'very small', 'main_colour': 'brown',
     'secondary_colour_1': 'white', 'secondary_colour_2': 'none'},
    {'common_name': 'Robin', 'latin_name': 'Erithacus rubecula', 'size': 'small', 'main_colour': 'brown',
     'secondary_colour_1': 'orange', 'secondary_colour_2': 'red'},
    {'common_name': 'Moorhen', 'latin_name': 'Gallinula chloropus', 'size': 'medium', 'main_colour': 'black',
     'secondary_colour_1': 'red', 'secondary_colour_2': 'white'},
    {'common_name': 'Goldcrest', 'latin_name': 'Regulus regulus', 'size': 'very small', 'main_colour': 'brown',
     'secondary_colour_1': 'yellow', 'secondary_colour_2': 'black'},
    {'common_name': 'Blue Tit', 'latin_name': 'Cyanistes caeruleus', 'size': 'very small', 'main_colour': 'yellow',
     'secondary_colour_1': 'blue', 'secondary_colour_2': 'white'},
]

bird_colour = input('What is the main colour of the bird? ')

# bird_colour_2 = input('What is an other of the bird? ')

# bird_colour_3 = input('What is an other of the bird? ')

#bird_size = input('What is the size of the bird? ')

for bird in birds:
    if bird_colour == (bird['main_colour']) and bird_size == (bird['size']):
        print(bird['common_name'])


#    if (bird_colour == (bird['main_colour']) or 'I do not know') and (bird_size == (bird['size']) or 'I do not know'):
# if bird_colour == ((bird['main_colour']) or (bird['secondary_colour_1'])): #and bird_colour_2 == ((bird['secondary_colour_1']) or 'I do not know' or (bird['main_colour'])) and bird_size == ((bird['size']) or 'I do not know'):

# and bird_colour_2 == ((bird['secondary_colour_1']) or 'I do not know')

# for bird in birds:
#   if (bird['main_colour']) == bird_colour:
#       print(bird['common_name'])
#      print(bird['latin_name'])

# and (bird_colour_3 == (bird['secondary_colour_2']) or 'I do not know')

# know_color =  input('do you know the color?')

# if know-color == 'yes' then

# if ((bird['size']) == bird_size) or (bird_size == 'I do not know') and ((bird['main_colour']) == bird_colour) or (bird_colour == 'I do not know'):

