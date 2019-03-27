birds = [
    {'common_name': 'Grey Heron', 'latin_name': 'Ardea cinerea', 'size': 'large', 'main_colour': 'grey', 'secondary_colour_1': 'white', 'secondary_colour_2': 'black'},
    {'common_name': 'Sparrowhawk', 'latin_name': 'Accipiter nisus', 'size': 'medium', 'main_colour': 'brown', 'secondary_colour_1': 'beige', 'secondary_colour_2': 'white'},
    {'common_name': 'Ring-necked Parakeet', 'latin_name': 'Psittacula krameri', 'size': 'medium', 'main_colour': 'green', 'secondary_colour_1': 'orange', 'secondary_colour_2': 'none'},
    {'common_name': 'Woodpigeon', 'latin_name': 'Columba palumbus', 'size': 'medium', 'main_colour': 'grey', 'secondary_colour_1': 'white', 'secondary_colour_2': 'black'},
    {'common_name': 'Green Woodpecker', 'latin_name': 'Picus viridis', 'size': 'medium', 'main_colour': 'green', 'secondary_colour_1': 'red', 'secondary_colour_2': 'black'},
    {'common_name': 'Wren', 'latin_name': 'Troglodytes troglodytes', 'size': 'very small', 'main_colour': 'brown', 'secondary_colour_1': 'white', 'secondary_colour_2': 'none'},
    {'common_name': 'Robin', 'latin_name': 'Erithacus rubecula', 'size': 'small', 'main_colour': 'brown', 'secondary_colour_1': 'orange', 'secondary_colour_2': 'red'},
    {'common_name': 'Moorhen', 'latin_name': 'Gallinula chloropus', 'size': 'medium', 'main_colour': 'black', 'secondary_colour_1': 'red', 'secondary_colour_2': 'white'},
    {'common_name': 'Goldcrest', 'latin_name': 'Regulus regulus', 'size': 'very small', 'main_colour': 'brown', 'secondary_colour_1': 'yellow', 'secondary_colour_2': 'black'},
    {'common_name': 'Blue Tit', 'latin_name': 'Cyanistes caeruleus', 'size': 'very small', 'main_colour': 'yellow', 'secondary_colour_1': 'blue', 'secondary_colour_2': 'white'},
]

app.run(debug=True)

colour = input('What is the main colour of the bird? ')

if colour == 'main_colour':
    for bird in birds:
        print(bird['common_name'])
        print(bird['latin_name'])
        print(bird['size'])

        (k for k,v in for_patient_type.iteritems() if v == 'Real')
