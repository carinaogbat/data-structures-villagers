"""Functions to parse a file containing villager data."""


from unittest import findTestCases


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    file = open(filename)
    species = set()
    for line in file:
        line.strip()
        charac = line.split("|")[1]
        species.add(charac)
    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    file = open(filename)
    villagers = []
    species = search_string
    for line in file:
        line.strip()
        char = line.split("|")
        if species == char[1]:
            villagers.append(char[0])

    return villagers

# def all_names_by_hobby(filename):
#     """Return a list of lists containing villagers' names, grouped by hobby.

#     Arguments:
#         - filename (str): the path to a data file

#     Return:
#         - list[list[str]]: a list of lists containing names
#     """
#     education = []
#     fitness = []
#     nature = []
#     music = []
#     play = []
#     fashion = []
#     name = []
#     file = open(filename)
#     for line in file:
#         char = line.split("|")
#         if char[3] == "Education":
#             education.append(char[0])
#         elif char[3] == "Fitness":
#             fitness.append(char[0])
#         elif char[3] == 'Nature':
#             nature.append(char[0])
#         elif char[3] == "Music":
#             music.append(char[0])
#         elif char[3] == "Play":
#             play.append(char[0])
#         elif char[3] == "Fashion":
#             fashion.append(char[0]) 
#     hobbies_by_name = []
#     hobbies_by_name.append(fitness, nature, education, music, fashion, play)
    # return hobbies_by_name


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    file = open(filename)
    all_data = []
    for line in file:
        all_data.append(tuple(line.rstrip().split('|')))

    

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    file = open(filename)
   
    for line in file:
        name, _, _, _, motto = line.rstrip().split("|")
        if name == villager_name
        return motto


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    villager_name = name
    file = open(filename)
    for line in filename:
        name, _, personality, _, _ = set(line.rstrip().split('|'))
        if name & personality:
            return name

