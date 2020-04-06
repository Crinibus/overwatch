#! python3
# random_overwatch.py - pick a random hero, gamemode, role, show info about a hero or play a quiz (singleplayer and multiplayer) among other things

import json
import requests
import random
import os
import platform
from PIL import Image
import webbrowser
from load_json import load_json_files, get_images


def hero_picker(role):
    """Returns a random hero depending on what "role" is equal to."""
    if role.lower() in ('all', 'a'):
        return random.choice(HEROES_ALL)
    elif role.lower() in ('tank', 't'):
        return random.choice(HEROES_TANK)
    elif role.lower() in ('dps', 'damage', 'd'):
        return random.choice(HEROES_DPS)
    elif role.lower() in ('support', 'healer', 's'):
        return random.choice(HEROES_SUPPORT)
    else:
        return None


def gamemode_picker(mode):
    """Returns a random gamemode depending on what "mode" is equal to."""
    if mode.lower() in ('all',):
        return random.choice(GAMEMODES_ALL)
    elif mode.lower() in ('arcade',):
        return random.choice(GAMEMODES_ARCADE)
    elif mode.lower() in ('normal',):
        return random.choice(GAMEMODES_NORMAL)
    else:
        return None


def role_picker():
    """Returns a random role."""
    return random.choice(ROLE_ALL)


def get_hero_info(hero):
    """Prints info about a hero on multiple lines."""
    hero = hero.lower()
    if hero in heroes_info:
        print('\nInfo about {0}:'.format(hero.upper()))
        print('Name: {0}'.format(heroes_info[hero]['name']))
        if not hero == 'orisa':
            if heroes_info[hero]['age'] == 'Classified':
                print('Age: {0}'.format(heroes_info[hero]['age']))
            else:
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
        
        end = False
        while end == False:
            info_input = input('Want more info in the browser? (y/n): ').lower()
            if info_input == 'y':
                while True:
                    source_input = input('From the official or fan-wiki (o/f): ').lower()
                    if source_input == 'o':
                        source = 'official'
                        hero = change_name(hero, source)
                        webbrowser.open(f'https://playoverwatch.com/en-us/heroes/{hero}')
                        end = True # makes it go back to choosing a hero
                        break
                    elif source_input == 'f':
                        source = 'fan'
                        hero = change_name(hero, source)
                        webbrowser.open(f'https://overwatch.gamepedia.com/{hero}')
                        end = True # makes it go back to choosing a hero
                        break
                    elif source_input in ('n', ''):
                        end = True # makes it go back to choosing a hero
                        break
                    else:
                        print('Try again\n')
            elif info_input in ('n', ''):
                break
            else:
                print('Try again\n')
        print()
    else:
        print('Choose again\n')


def change_name(hero, source):
    """Change a heroes name to a string suitable for official or fan-wiki url."""
    if source == 'official':
        if hero == 'd.va':
            hero = 'dva'
        elif hero == 'soldier: 76':
            hero = 'soldier-76'
        elif hero == 'wrecking ball':
            hero = 'wrecking-ball'
    elif source == 'fan':
        if hero == 'soldier: 76':
            hero = 'soldier:_76'
        elif hero == 'wrecking ball':
            hero = 'wrecking_ball'
    return hero


def help():
    """Prints what commands the user can use with some explanation."""
    print('\nhero: choose a role and the program picks a random hero inside that role')
    print('gamemode: choose a category and the program picks a random gamemode inside that category')
    print('role: the program returns a random role, e.g. "tank"')
    print('info: choose a hero to show information about')
    print('height: prints the height of each hero')
    print('age: prints the age of each hero')
    print('quiz: choose how many players you are and how many rounds you want to play. '
        'Try to answer the questions and see how many you can get correct')
    print('open: choose a hero to open a image of')
    print('help: explains what you can with this program')
    print('to go back: just press the enter key when nothing is typed\n')


def heroes_height():
    """Prints the height of each hero."""
    print()
    for hero in heroes_info:
        if not heroes_info[hero]['height'] == 'Unknown':
            print('Height of {0}{1} \t{2} meters'.format(
                hero.upper(),
                " "*5,
                heroes_info[hero]['height']).expandtabs(10)
                )
        else:
            # Add extra spaces depending on the hero
            if hero in ('ana', 'mei', 'moira', 'orisa', 'sombra'):
                print('Height of {0}{1} \tUnknown'.format(
                    hero.upper(),
                    " "*7).expandtabs(10)
                    )
            else:
                print('Height of {0}{1} \tUnknown'.format(
                    hero.upper(),
                    " "*1).expandtabs(10)
                    )
    print()


def heroes_age():
    """Prints the age of each hero."""
    print()
    for hero in heroes_info:
        # Add extra spaces depending on the hero
        if not hero == 'orisa':
            if hero in ('ana', 'ashe', 'd.va', 'genji', 'hanzo', 'lúcio', 'mccree', 'mei', 'mercy', 'moira', 'pharah', 'reaper', 'sigma', 'sombra', 'tracer', 'zarya'):
                print('Age of {0}{1} \t{2} years'.format(
                    hero.upper(),
                    " "*10,
                    heroes_info[hero]['age']).expandtabs(10)
                    )
            else:
                print('Age of {0}{1} \t{2} years'.format(
                    hero.upper(),
                    " "*5,
                    heroes_info[hero]['age']).expandtabs(10)
                    )
        else:
            print('Age of {0}{1} \t{2}'.format(
                hero.upper(),
                " "*7,
                heroes_info[hero]['age']).expandtabs(10)
                )
    print()


def quiz_singleplayer(num_rounds):
    """Quiz with {num_rounds} rounds for 1 player."""
    category = 'what_hero'
    #shown_categories = []
    points = 0
    questions_shown = {"what_hero": []}
    if num_rounds > len(list(quiz_questions[category])):
        num_rounds = len(list(quiz_questions[category]))
        print(f'Number of rounds is bigger than number of questions, so number of rounds is changed to {num_rounds}')
    print(f'\nStarting quiz with {num_rounds} rounds')
    for i in range(1, num_rounds + 1):
        tries = 0
        # Break if all questions have been shown
        if len(list(questions_shown[category])) == len(list(quiz_questions[category])):
            break
        rnd_num = random.randint(1, len(list(quiz_questions[category])))
        # Find a new random number if it's already in "questions_shown"
        while rnd_num in questions_shown[category]:
            rnd_num = random.randint(1, len(list(quiz_questions[category])))
        # Add random number in "questions_shown"
        questions_shown[category].append(rnd_num)

        print(f'Round {i}')
        print(f'Category: {category}')
        # Print question
        print(quiz_questions[category][f'question{rnd_num}']['question'])
        # While the player has tried under 3 times
        while tries < 3:
            answer_input = input('Answer: ').lower()
            # If answer is correct
            if answer_input == quiz_questions[category][f'question{rnd_num}']['answer']:
                print('You answered correct\n')
                points += 1
                break
            elif answer_input == '':
                print('Try again')
            else:
                if tries >= 0 and tries < 2:
                    print('You answered incorrect, try again\n')
                    tries += 1
                else:
                    print('You answeed incorrect, you have no more tries')
                    print('The answer is: {0}\n'.format(quiz_questions[category][f'question{rnd_num}']['answer'].capitalize()))
                    break
    print(f'The quiz is over. You got {points}/{num_rounds} points\n\n')


def quiz_multiplayer(num_rounds, num_players):
    """Multiplayer quiz with {num_rounds} rounds and {num_players} players, each player have 1 try to answer each question."""
    clear_terminal()
    while True:
        input_show_answers = input('Do you want to see what the other player(s) have answered? (y/n): ')
        if input_show_answers == 'y':
            show_answers = True
            break
        elif input_show_answers == 'n':
            show_answers = False
            break
        else:
            print('Please answer \'y\' or \'n\' \n')

    clear_terminal()
    category = 'what_hero'
    # List with already shown questions
    questions_shown = []
    # Store players in a list
    players = []
    if num_rounds > len(list(quiz_questions[category])):
        num_rounds = len(list(quiz_questions[category]))
        print(f'Number of rounds is bigger than number of questions, so number of rounds is changed to {num_rounds}\n')
    print(f'Starting multiplayer quiz with {num_rounds} rounds and {num_players} players')

    # Create players
    for i in range(1, num_players + 1):
        name_input = input(f'Enter name for Player {i}: ')
        # Add player to list
        players.append(Player(name_input))
    for i in range(1, num_rounds + 1):
        # Used to pick random question
        rnd_num = random.randint(1, len(list(quiz_questions[category])))
        while rnd_num in questions_shown:
            # Find a new random number if it's already in questions_shown
            rnd_num = random.randint(1, len(list(quiz_questions[category])))
        # Add question number to list
        questions_shown.append(rnd_num)
        for player in players:
            clear_terminal()
            print(f'Round {i}')
            print(f"Question for {player.name}")
            print(f'Category: {category}\n')
            print(quiz_questions[category][f'question{rnd_num}']['question'])
            player.answer = input('Answer: ').lower()
            # If answer is correct
            if player.answer == quiz_questions[category][f'question{rnd_num}']['answer']:
                player.points += 1
        clear_terminal()

        print('Correct answer for round {0} is: {1}\n'.format(
            i,
            quiz_questions[category][f'question{rnd_num}']['answer'].capitalize()
            ))
        
        # Show what all players have answered
        if show_answers:
            for player in players:
                print(f'{player.name} answered {player.answer}')

        if i < num_rounds:
            input('\nEnter to start the next round')

    # TODO: Maybe add a option to send a mail with the results of a quiz
    # TODO: Make a ranking system and show it when the quiz is over

    print('\nThe quiz is over')
    for player in players:
        player.print_points()
    print()


class Player: # Used in quiz_multiplayer() to create new players
    def __init__(self, name, email=''):
        self.name = name
        self.email = email
        self.points = 0
        self.tries = 0
        self.answer = ''

    def print_points(self):
        """Prints the player's points."""
        print(f'{self.name} got {self.points} points')


def clear_terminal():
    """Clears the terminal."""
    # Check OS
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() in ('Linux', 'Darwin'): # Darwin is MacOS
        os.system('clear')


def open_image(name):
    """Opens the image of name: {name} in the directory ./images/{name}."""
    print(f'Opening image of {name}\n')
    file_image = f'./images/{name}.png'
    img = Image.open(file_image)
    img.show()


def main(): # Start of the program
    # Loops the code, so the user can keep selecting
    while True:
        # Get user input
        start_input = input('Choose what to pick '
            '(hero, gamemode, role, info, height, age, quiz, open, help): ').lower()
        if start_input == 'hero':
            while True:
                role_input = input('Choose a role (all, tank, dps, support): ')
                if role_input == '':
                    print()
                    break
                if hero_picker(role_input):
                    print(f'Picked hero: {hero_picker(role_input)}\n')
                else:
                    print('Please select a role\n')
        elif start_input == 'gamemode':
            while True:
                gamemode_input = input('Choose a category (all, normal, arcade): ')
                if gamemode_input == '':
                    print()
                    break
                if gamemode_picker(gamemode_input):
                    print(f'Picked gamemode: {gamemode_picker(gamemode_input)}\n')
                else:
                    print('Please select a category\n')
        elif start_input == 'info':
            while True:
                info_input = input('Choose a hero: ')
                if info_input == '':
                    print()
                    break
                get_hero_info(info_input)
        elif start_input == 'role':
            print(f'Picked role: {role_picker()}\n')
        elif start_input == 'help':
            help()
        elif start_input == 'height':
            heroes_height()
        elif start_input == 'age':
            heroes_age()
        elif start_input == 'quiz':
            # Ask the player for number of players
            num_players = input('Enter number of players: ')
            # Keep asking the player for an integer
            while not num_players.isdigit():
                num_players = input('Please enter an integer number of players: ')

            # Ask the player for number of rounds
            quiz_num = input('Enter number of rounds: ')
            # Keep asking the player for an integer
            while not quiz_num.isdigit():
                quiz_num = input('Please enter an integer number of rounds: ')

            # Convert from string to integer
            num_players = int(num_players)
            quiz_num = int(quiz_num)

            # Check number of players
            if num_players == 1:
                quiz_singleplayer(quiz_num)
            elif num_players > 1:
                quiz_multiplayer(quiz_num, num_players)
            else:
                print('Please enter an integer equal to 1 or higher')
        elif start_input in ('cls', 'clear'):
            clear_terminal()
        elif start_input == 'open':
            open_input = input('What hero do you want to open a image of? ').lower()
            while open_input not in heroes_info:
                if open_input == '':
                    print()
                    break
                open_input = input('Try again: ').lower()
            if open_input == 'soldier: 76':
                open_input = 'soldier_76'
            elif open_input == 'wrecking ball':
                open_input = 'wrecking_ball'
            if not open_input == '':
                open_image(open_input)
        else:
            print('Try again\n')


if __name__ == "__main__":
    try:
        heroes_info, quiz_questions, HEROES_TANK, HEROES_DPS, HEROES_SUPPORT, HEROES_ALL, GAMEMODES_ARCADE, GAMEMODES_NORMAL, GAMEMODES_ALL, ROLE_ALL = load_json_files()
        main()
    except IOError:
        print('\nImage doesn\'t exist')
        main()
    except KeyboardInterrupt:
        print('\n\nProgram closed by user\n')
