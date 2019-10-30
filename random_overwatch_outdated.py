#! python3
# random_Overwatch.py - picks a random hero, gamemode, role or shows info about a hero among other things

import random
import json

heroes_tank = ['D.Va', 'Orisa', 'Reinhardt', 'Roadhog', 'Sigma', 'Winston', 'Wrecking Ball', 'Zarya']
heroes_dps = ['Ashe', 'Bastion', 'Doomfist', 'Genji', 'Hanzo', 'Junkrat', 'Mccree', 'Mei', 'Pharah', 'Reaper', 'Soldier: 76', 'Sombra', 'Symmetra', 'Torbjörn', 'Tracer', 'Widowmaker']
heroes_support = ['Ana', 'Baptiste', 'Brigitte', 'Lúcio', 'Mercy', 'Moira', 'Zenyatta']
heroes_all = heroes_tank + heroes_dps + heroes_support

gamemodes_arcade = ['1V1 Mystery Duel', '1V1 Limited Duel', '3V3 Elimination', '6V6 Elimination', '3V3 Lockout Elimination', '6V6 Lockout Elimination', '6V6 Mystery Heroes', '6V6 No limits', '6V6 Total Mayhem', '6V6 Low Gravity', '6V6 Capture The Flag', '8P Deathmatch', '4V4 Team Deathmatch', '8P Mystery Deathmatch', '8P Château Deathmatch', '8P Petra Deathmatch', '8P Mirrored Deathmatch', '6V6 Quick Play Classic']
gamemodes_normal = ['Quick Play Role Queue', 'Competitive']
gamemodes_all = gamemodes_arcade + gamemodes_normal

role_all = ['Tank', 'Damage', 'Support']

try:
    # loads/reads json file
    with open('hero_info_overwatch.json', encoding='utf-8') as f:
        info_json = f.read()
    # saves data from json file to a variable
    heroes_info = json.loads(info_json)
    file_found = True 
except:
    # print a notice if the json file can't be accessed or found, and therefor sets "file_found" to False
    print('\nCan\'t find a file named "hero_info_overwatch.json')
    print('Can\'t use "info" when "hero_info_overwatch.json" not found\n')
    file_found = False # used so an error doesn't come when the user tries to see info about a hero in "get_hero_info" and the file is not found

def hero_picker(role): # returns a random hero depending on what "role" is equal to
    if role.lower() in ('all', 'a'):
        return random.choice(heroes_all)
    elif role.lower() in ('tank', 't'):
        return random.choice(heroes_tank)
    elif role.lower() in ('dps', 'damage', 'd'):
        return random.choice(heroes_dps)
    elif role.lower() in ('support', 'healer', 's'):
        return random.choice(heroes_support)
    else:
        return 'Please select a role'

def gamemode_picker(mode): # returns a random gamemode depending on what "mode" is equal to
    if mode.lower() in ('all'):
        return random.choice(gamemodes_all)
    elif mode.lower() in ('arcade'):
        return random.choice(gamemodes_arcade)
    elif mode.lower() in ('normal'):
        return random.choice(gamemodes_normal)
    else:
        return 'Please select a gamemode'

def role_picker(): # returns a random role
    return random.choice(role_all)

def get_hero_info(hero): # prints info about a hero on multiple lines
    hero = hero.lower()
    if hero in heroes_info:
        print('\nInfo about {0}:'.format(hero.upper()))
        print('Name: {0}'.format(heroes_info[hero]['name']))
        if not hero.lower() == 'orisa':
            print('Age: {0} years'.format(heroes_info[hero]['age']))
        else:
            print('Age: {0}'.format(heroes_info[hero]['age']))
        if not heroes_info[hero]['height'] == 'Unknown':
            print('Height: {0} meters'.format(heroes_info[hero]['height']))
        else:
            print('Height: {0}'.format(heroes_info[hero]['height']))
        print('Nationality: {0}'.format(heroes_info[hero]['nationality']))
        print('Occupation: {0}'.format(heroes_info[hero]['occupation']))
        print('Affiliation: {0}\n'.format(heroes_info[hero]['affiliation']))
    else:
        get_hero_info(input('Choose again: '))

def help(): # prints what commands the user can use with some explanation
    print('\nhero: choose a role and the program picks a random hero inside that role')
    print('gamemode: choose a category and the program picks a random gamemode inside that category')
    print('role: the program returns a random role, e.g. "tank"')
    print('info: choose a hero to show information about')
    print('height: prints the height of each hero')
    print('age: prints the age of each hero')
    print('help: explains what you can with this program\n')

def heroes_height(): # prints the height of each hero
    print()
    for hero in heroes_info:
        if not heroes_info[hero]['height'] == 'Unknown':
            print('Height of {0}{1} \t{2} meters'.format(hero.upper(), " "*5, heroes_info[hero]['height']).expandtabs(10))
        else:
            if hero in ('ana', 'mei', 'moira', 'orisa', 'sombra'): # add extra spaces depending on the hero
                print('Height of {0}{1} \tUnknown'.format(hero.upper(), " "*7).expandtabs(10))
            else:
                print('Height of {0}{1} \tUnknown'.format(hero.upper(), " "*1).expandtabs(10))
    print()

def heroes_age(): # prints the age of each hero
    print()
    for hero in heroes_info:
        if not hero == 'orisa': # add extra spaces depending on the hero
            if hero in ('ana', 'ashe', 'd.va', 'genji', 'hanzo', 'lúcio', 'mccree', 'mei', 'mercy', 'moira', 'pharah', 'reaper', 'sigma', 'sombra', 'tracer', 'zarya'):
                print('Age of {0}{1} \t{2} years'.format(hero.upper(), " "*10, heroes_info[hero]['age']).expandtabs(10))
            else:
                print('Age of {0}{1} \t{2} years'.format(hero.upper(), " "*5, heroes_info[hero]['age']).expandtabs(10))
        else:
            print('Age of {0}{1} \t{2}'.format(hero.upper(), " "*7, heroes_info[hero]['age']).expandtabs(10))
    print()

try:
    while True: # loops the code, so the user can keep selecting
        start_input = input('Choose what to pick (hero, gamemode, role, info, height, age, help): ').lower()
        if start_input == 'hero':
            while True:
                role_input = input('Choose a role (all, tank, dps, support): ')
                if role_input == '':
                    break
                if not hero_picker(role_input) == 'Please select a role':
                    print('Picked hero: {0}\n'.format(hero_picker(role_input)))
                else:
                    print('{0}\n'.format(hero_picker(role_input)))
        elif start_input == 'gamemode':
            while True:
                gamemode_input = input('Choose a category (all, normal, arcade): ')
                if gamemode_input == '':
                    break
                print('Picked gamemode: {0}\n'.format(gamemode_picker(gamemode_input)))
        elif start_input == 'info':
            while True:
                if file_found:
                    info_input = input('Choose a hero: ')
                    if info_input == '':
                        break
                    get_hero_info(info_input)
                else:
                    print('Can\'t access json file "hero_info_overwatch.json"\n')
                    break
        elif start_input == 'role':
            print('Picked role: {}\n'.format(role_picker()))
        elif start_input == 'help':
            help()
        elif start_input == 'height':
            if file_found:
                heroes_height()
            else:
                print('Can\'t access json file "hero_info_overwatch.json"\n')
        elif start_input == 'age':
            if file_found:
                heroes_age()
            else:
                print('Can\'t access json file "hero_info_overwatch.json"\n')
        elif start_input not in ('hero', 'gamemode', 'role', 'info', 'help', 'height', 'age'):
            print('Try again\n')
except KeyboardInterrupt:
    print('\nProgram closed by user')
