# Project: Spotify's Discover Weekly
# Week 3

import csv
import random
import Week_2
from typing import List, Dict

# Solution Strategy
# Divide the problem into several sub problems or steps
# Make a model - making a diagram or drawing a picture

dataset: List = []  # Create an empty list


def read_dataset(path: str) -> List[Dict[str, any]]:  # Open spotify dataset
    """
    Open and reads the csv-file and stores it in a list of dictionaries. It also cleans the data.
    :param path: string which is path of the csv file.
    :returns: list of dictionaries which contain string as a key and value could be anything.
    """

    with open(path) as file:  # open a csv file and named as a file
        reader = csv.DictReader(file)
        fn = reader.fieldnames  # Creates list of field name

        for row in reader:
            for x in fn:
                if x != "title" and x != "artist" and x != "the genre of the track":
                    # Change all numbers from string to integer
                    row[x] = int(row[x])

            dataset.append(row)  # Add the row into the dataset list

    return dataset


def user_listened() -> List:  # # Songs that the user have listen
    """
    Randomly choosing songs to represent what the user listened.
    :return: A list that user had listened.
    """

    read_dataset("spotify-dataset.csv")
    music: List = []  # All the songs in the dataset
    user_music: List = []  # Songs that user had listened

    for dct in dataset:
        music.append(dct["title"])
        # Adding titles from the dataset to a list

    for i in range(50):
        r = random.choice(music)
        user_music.append(r)
        # Randomly choosing music from the music list

    return user_music


# Define in your own algorithm if you think one song can be classified as two of those at the same time.
def music_types() -> any:
    """
    Classifying the type of song.
    :param: None.
    :return: List of different type of songs.
    """
    read_dataset("spotify-dataset.csv")
    happy_songs: List = []  # Songs that contains more positive mood
    party_songs: List = []  # Songs that are suitable for party
    calming_songs: List = []  # Songs that make you calm
    lounge_music: List = []  # Songs that contain acoustic

    for dct in dataset:
        if dct["Valence - The higher the value, the more positive mood for the song"] >= 70:
            happy_songs.append(dct["title"])

        if dct["Danceability - The higher the value, the easier it is to dance to this song"] >= 70:
            party_songs.append(dct["title"])

        if dct["Beats.Per.Minute -The tempo of the song"] <= 100:
            calming_songs.append(dct["title"])

        if dct["Acousticness - The higher the value the more acoustic the song is"] >= 70:
            lounge_music.append(dct["title"])

    return happy_songs, party_songs, calming_songs, lounge_music


def type_user_listen() -> Dict[str, int]:
    """
    Counting the types of music the user listen.
    :return: A dictionary which the type of music as keys and the amount of music the user listened as values.
    """

    music = music_types()  # list of different music types
    user_music = user_listened()
    num_types: Dict = {}

    for x in music[0]:
        for y in user_music:
            if x == y:
                if "happy music" not in num_types:
                    num_types["happy music"] = 1
                else:
                    num_types["happy music"] += 1

    for x in music[1]:
        for y in user_music:
            if x == y:
                if "party music" not in num_types:
                    num_types["party music"] = 1
                else:
                    num_types["party music"] += 1

    for x in music[2]:
        for y in user_music:
            if x == y:
                if "calm music" not in num_types:
                    num_types["calm music"] = 1
                else:
                    num_types["calm music"] += 1

    for x in music[3]:
        for y in user_music:
            if x == y:
                if "lounge music" not in num_types:
                    num_types["lounge music"] = 1
                else:
                    num_types["lounge music"] += 1

    if "happy music" not in num_types:
        num_types["happy music"] = 0
    if "party music" not in num_types:
        num_types["party music"] = 0
    if "calm music" not in num_types:
        num_types["calm music"] = 0
    if "lounge music" not in num_types:
        num_types["lounge music"] = 0

    return num_types


def genre_songs() -> tuple[List[str], List[str], List[str]]:
    """
    Import lists in which the names of the songs sorted by genre from Week 2.
    :returns: three different lists which represent pop, rock and techno.
    """
    pop_songs = Week_2.pop_names
    rock_songs = Week_2.rock_names
    techno_songs = Week_2.techno_names

    return pop_songs, rock_songs, techno_songs


def num_genres() -> Dict:
    """
    Import the percentage of the genres the user had listen
    :return: A dictionary with the genre types as a key and the amount of suggest as value.
    """
    songs_pop = Week_2.songs_pop
    songs_rock = Week_2.songs_rock
    songs_techno = Week_2.songs_techno

    amount_genres = {"pop": songs_pop, "rock": songs_rock, "techno": songs_techno}

    return amount_genres


def highest_genre() -> str:
    """
    To find which genre the users had listened to the most.
    :return: A string which is the highest of the genres.
    """

    genres_num = num_genres()
    highest: int = 0
    highest_gen: str = ""

    for i in genres_num:
        if genres_num[i] > highest:
            highest = genres_num[i]
            highest_gen = i

    return highest_gen

# Define, in your own terms what this should mean: if the user listened to 3 “calming” songs,
# should we provide 3 more without considering other factors? What if he or she also listened to 3 “party” songs and
# 4 “lounge” style songs?


def suggestion() -> tuple:
    """
    Calculate the number of suggestion for each type of music.
    :return: A dictionary with the type as keys, and integer as values. Also, return the highest types.
    """
    num_music_types = type_user_listen()

    total_music_type = num_music_types["happy music"] + num_music_types["party music"] + num_music_types["calm music"] + num_music_types["lounge music"]
    # Calculate the total amount of music types that user listen

    percentage_happy = num_music_types["happy music"] / total_music_type
    percentage_party = num_music_types["party music"] / total_music_type
    percentage_calm = num_music_types["calm music"] / total_music_type
    percentage_lounge = num_music_types["lounge music"] / total_music_type
    # Calculate the percentage for each type of music that the user listened

    happy = round(percentage_happy * 5)
    party = round(percentage_party * 5)
    calm = round(percentage_calm * 5)
    lounge = round(percentage_lounge * 5)
    # Calculate the amount of suggestion for each type

    num_suggest = {"happy": happy, "party": party, "calm": calm, "lounge": lounge}

    total = happy + party + calm + lounge

    highest = 0
    highest_type = ""

    # Depending on the percentage, the total suggestion may not reach five
    # Therefore, if there are missing songs
    # The algorithm will add 1 to the type that user listen to the most
    while total < 5:
        for i in num_suggest:
            if num_suggest[i] > highest:
                highest = num_suggest[i]
                highest_type = i

        num_suggest[highest_type] += 1
        total += 1

    return num_suggest, highest_type


def genre_highest_list() -> List[str]:
    """
    Choosing the list that have the highest genre from Week 2.
    :return: The highest genre list.
    """
    gen = highest_genre()
    genres_list = genre_songs()

    gen_list: List = []

    if gen == "pop":
        for i in genres_list[0]:
            gen_list.append(i)

    elif gen == "rock":
        for i in genres_list[1]:
            gen_list.append(i)

    elif gen == "techno":
        for i in genres_list[2]:
            gen_list.append(i)

    return gen_list


def combine_genres_types() -> tuple:
    """
    Combining the music type list with the highest genre list.
    :return: four different music type list combined with the highest genre.
    """
    music_list = music_types()
    gen_list = genre_highest_list()

    happy_list: List = []
    party_list: List = []
    calm_list: List = []
    lounge_list: List = []

    # combining 2 list
    for x in gen_list:
        for y in music_list[0]:
            if x == y:
                happy_list.append(x)

    for x in gen_list:
        for y in music_list[1]:
            if x == y:
                party_list.append(x)

    for x in gen_list:
        for y in music_list[2]:
            if x == y:
                calm_list.append(x)

    for x in gen_list:
        for y in music_list[3]:
            if x == y:
                lounge_list.append(x)

    return happy_list, party_list, calm_list, lounge_list


def suggested_song() -> str:
    """
    Randomly choosing songs form the music type list combined with the highest genre.
    :return: A string which contain five suggestion to the user.
    """
    num_suggest = suggestion()
    music_list = combine_genres_types()

    suggested_list: List = []  # Creating an empty list for suggestion

    if num_suggest[0]["happy"] > 0:
        for i in range(num_suggest[0]["happy"]):
            r = random.choice(music_list[0])

            while r in suggested_list:
                r = random.choice(music_list[0])
            # We do not want to suggest the same song more than once
            # So, while the random selected song already in the list, we randomly choose another song
            # Until there is no repeated element in the list
            suggested_list.append(r)

    if num_suggest[0]["party"] > 0:
        for i in range(num_suggest[0]["party"]):
            r = random.choice(music_list[1])
            while r in suggested_list:
                r = random.choice(music_list[1])
            suggested_list.append(r)

    if num_suggest[0]["calm"] > 0:
        for i in range(num_suggest[0]["calm"]):
            r = random.choice(music_list[2])
            while r in suggested_list:
                r = random.choice(music_list[2])
            suggested_list.append(r)

    if num_suggest[0]["lounge"] > 0:
        for i in range(num_suggest[0]["lounge"]):
            r = random.choice(music_list[3])
            while r in suggested_list:
                r = random.choice(music_list[3])
            suggested_list.append(r)

    return f"Dear user,\nHere is our suggest song from our week 3 Discover Weekly:\n{suggested_list}\nHope you will enjoy it!"


print(f"\n{suggested_song()}")
