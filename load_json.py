import json
import requests
import os

def load_json_files():
    """Get JSON files from GitHub and/or load JSON files."""
    # Check if hero json file is in the current working directory
    if os.path.isfile('./data/hero_info_overwatch.json'):
        # Loads/reads hero json file
        with open('./data/hero_info_overwatch.json', encoding='utf-8') as f:
            info_json = f.read()
        # Saves data from hero json file to a variable
        heroes_info = json.loads(info_json)
    else:
        input('Files from Github is about to be downloaded, press \'Enter\' to continue\n')
        # If hero json file not found, get hero json data from GitHub,
        # create a new hero json file and dump hero json data in the new file,
        # then load the hero json data in a variable
        print('Getting info about heroes data from GitHub...')
        # Get hero json file from GitHub
        get_hero_json = requests.get(
            'https://raw.github.com/Crinibus/overwatch/master/hero_info_overwatch.json'
            )
        # Load hero json from string to dictionary
        json_hero_data = get_hero_json.json()
        print('Creating file with hero data...')
        # Create new hero json file
        with open('./data/hero_info_overwatch.json', 'w') as json_hero_file:
            # Dump the hero json data in the new file and make it more readable
            json.dump(
                json_hero_data,
                json_hero_file,
                indent=4,
                sort_keys=True
                )
        print('Done creating file\n')
        # Loads/reads hero json file
        with open('./data/hero_info_overwatch.json', encoding='utf-8') as f:
            info_json = f.read()
        # Saves data from hero json file to a variable
        heroes_info = json.loads(info_json)

    # Check if quiz json file is in the current working directory
    if os.path.isfile('./data/quiz_overwatch.json'):
        # Loads/reads quiz json file
        with open('./data/quiz_overwatch.json', encoding='utf-8') as f:
            quiz_json = f.read()
        # Saves data from quiz json file to a variable
        quiz_questions = json.loads(quiz_json)
    else:
        input('Files from Github is about to be downloaded, press \'Enter\' to continue\n')
        # If quiz json file not found, get quiz json data from GitHub,
        # create a new quiz json file and dump quiz json data in the new file,
        # then load the quiz json data in a variable
        print('Getting quiz data from GitHub...')
        # Get quiz json file from GitHub
        get_quiz_json = requests.get(
            'https://raw.github.com/Crinibus/overwatch/master/quiz_overwatch.json'
            )
        # Load quiz json from string to dictionary
        json_quiz_data = get_quiz_json.json()
        print('Creating file with quiz data...')
        # Create new quiz json file
        with open('./data/quiz_overwatch.json', 'w') as json_quiz_file:
            # Dump the quiz json data in the new file and make it more readable
            json.dump(
                json_quiz_data,
                json_quiz_file,
                indent=4,
                sort_keys=True
                )
        print('Done creating file\n')
        # Loads/reads quiz json file
        with open('./data/quiz_overwatch.json', encoding='utf-8') as f:
            quiz_json = f.read()
        # Saves data from quiz json file to a variable
        quiz_questions = json.loads(quiz_json)

    # Check if lists json file is in the current working directory
    if os.path.isfile('./data/lists_overwatch.json'):
        # Loads/reads lists json file
        with open('./data/lists_overwatch.json', encoding='utf-8') as f:
            lists_json = f.read()
        # Saves data from lists json file to a variable
        lists = json.loads(lists_json)
        HEROES_TANK = lists["HEROES_TANK"]
        HEROES_DPS = lists["HEROES_DPS"]
        HEROES_SUPPORT = lists["HEROES_SUPPORT"]
        HEROES_ALL = lists["HEROES_ALL"]
        GAMEMODES_ARCADE = lists["GAMEMODES_ARCADE"]
        GAMEMODES_NORMAL = lists["GAMEMODES_NORMAL"]
        GAMEMODES_ALL = lists["GAMEMODES_ALL"]
        ROLE_ALL = lists["ROLE_ALL"]
    else:
        input('Files from Github is about to be downloaded, press \'Enter\' to continue\n')
        # If lists json file not found, get lists json data from GitHub,
        # create a new lists json file and dump lists json data in the new file,
        # then load the lists json data in a variable
        print('Getting lists data from GitHub...')
        # Get lists json file from GitHub
        get_lists_json = requests.get(
            'https://raw.github.com/Crinibus/overwatch/master/lists_overwatch.json'
            )
        # Load lists json from string to dictionary
        json_lists_data = get_lists_json.json()
        print('Creating file with quiz data...')
        # Create new lists json file
        with open('./data/lists_overwatch.json', 'w') as json_lists_file:
            # Dump the lists json data in the new file and make it more readable
            json.dump(
                json_lists_data,
                json_lists_file,
                indent=4,
                sort_keys=True
            )
        print('Done creating file\n')
        # Loads/reads lists json file
        with open('./data/lists_overwatch.json', encoding='utf-8') as f:
            lists_json = f.read()
        # Saves data from lists json file to a variable
        lists = json.loads(lists_json)
        HEROES_TANK = lists["HEROES_TANK"]
        HEROES_DPS = lists["HEROES_DPS"]
        HEROES_SUPPORT = lists["HEROES_SUPPORT"]
        HEROES_ALL = lists["HEROES_ALL"]
        GAMEMODES_ARCADE = lists["GAMEMODES_ARCADE"]
        GAMEMODES_NORMAL = lists["GAMEMODES_NORMAL"]
        GAMEMODES_ALL = lists["GAMEMODES_ALL"]
        ROLE_ALL = lists["ROLE_ALL"]

    return heroes_info, quiz_questions, HEROES_TANK, HEROES_DPS, HEROES_SUPPORT, HEROES_ALL, GAMEMODES_ARCADE, GAMEMODES_NORMAL, GAMEMODES_ALL, ROLE_ALL


def get_images():
    """Not implemented yet."""
    #print('Getting images from GitHub')
    input('This feature is not yet implemented')