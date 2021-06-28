# next wip 
import random

mediumType = ['script',
              'short story',
              'novella',
              'poem']
genresMovies = ['romance', 'horror', 'science fiction', 'action', 'adventure', 'drama']
songs = ['365', 'one way', 'let me in', 'around you', 'where you at?', 'Sonatine', 'Universe', 'Fall Again',
         'Twilight', 'Love Letter', 'Crystal Ballad', '51db(Rain 51db)', 'A Different Night']
locations = ['South Korea', 'France', 'Japan', 'Iceland', 'UK', 'USA', 'Taiwan',
             'Hungary', 'Hong Kong', 'New Zealand', 'Czech Republic']
generate = True
isGenerated = True
while generate:
    try:
        changeGeneration = (input("Do you want this to be randomly generated?  ")).lower()
        if changeGeneration == 'no':
            isGenerated = False
        else:
            print("It will be randomly generated")
    except NameError:
        print('Please choose either yes or no.')
    characterNumbers = (input("How many characters do you want?  "))
    try:
        val = int(characterNumbers)
    except ValueError:
        print("That's not an int!")
    if not isGenerated:
        print('Pick a medium.\n')
        print(mediumType, '\n')
        medium = input('\n')
        while medium in mediumType:
            print('Pick a genre.\n')
            print(genresMovies, '\n')
            genre = input('\n')
            while genre in genresMovies:
                print('Pick a song,\n')
                print(songs, '\n')
                song = input('\n')
                while song in songs:
                    print('Pick a location.\n')
                    print(locations, '\n')
                    location = input('\n')
                    while location in locations:
                        print('\n')
                    else:
                        print('Pick a location from the list of locations')
                else:
                    print('Pick a song from the list of songs.')
            else:
                print('Pick a genre from the list of genres.')
        else:
            print('Pick a medium from the list of mediums')
    else:
        medium = (random.choice(mediumType))
        genre = (random.choice(genresMovies))
        song = (random.choice(songs))
        location = (random.choice(locations))
    print(f"You will write a {genre} {medium} with {characterNumbers} characters set in {location}.")
    wantContinue = (input("Do you want to continue? ")).lower()
    if wantContinue == "yes":
        wantContinue = True
    else:
        generate = False
