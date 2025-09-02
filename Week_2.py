import csv, random
from typing import List

# list in which to store the genres of the songs
playlist = []

# list in which to store the names of the songs
playlist_names = []

# list in which to store the recommendations
recommendations = []

# Separate all the different types of genres into the 3 main genres
rock_genres = ["neo mellow", "permanent wave", "celtic rock"]
pop_genres = ["detroid hip hop", "dance pop", "pop", "canadian pop", "hip hop", "barbadian pop", "atl hip hop",
              "australian pop", "indie pop", "art pop", "colombian pop", "british soul", "chicago rap", "acoustic pop",
              "boy band", "baroque pop", "candy pop", "alaska indie", "folk-pop", "metropopolis", "australian hip hop",
              "electropop", "hollywood", "irish singer-songwriter", "french indie pop", "danish pop",
              "canadian hip hop", "latin", "canadian latin", "contemporary country", "detroit hip hop", "moroccan pop",
              "escape room"]
techno_genres = ["big room", "electro", "complextro", "house", "tropical house", "belgian edm",
                 "canadian contemporary r&b", "australian dance", "edm", "belgian edm", "downtempo", "brostep",
                 "alternative r&b"]

# Create lists in which to store the names of the songs sorted by genre
rock_names = []
pop_names = []
techno_names = []

# Open and read the csv file
with open("spotify-dataset.csv", encoding="utf-8") as f:
    csv_dict_reader = csv.DictReader(f)

    # Loop in which to get the names and genres of the songs in their respective lists
    for row in csv_dict_reader:
        type = row["the genre of the track"]
        title = row["title"]
        playlist.append(type)
        playlist_names.append(title)

        # Loops in which the names of the songs get sorted into different genres
        for x in rock_genres:
            if type == x:
                rock_names.append(title)
        for x in pop_genres:
            if type == x:
                pop_names.append(title)
        for x in techno_genres:
            if type == x:
                techno_names.append(title)

# Lists for all the listened songs and for their respective genres
listened_songs = []
listened_to_rock = []
listened_to_pop = []
listened_to_techno = []

# Generating random list of listened songs
for i in range(100):
    listened_songs.append(random.choice(playlist))

# Sorting the listened song in their respective genres
for i in listened_songs:
    for x in rock_genres:
        if i == x:
            listened_to_rock.append(i)
    for x in pop_genres:
        if i == x:
            listened_to_pop.append(i)
    for x in techno_genres:
        if i == x:
            listened_to_techno.append(i)

# Get the length of the listened songs by genre
num_rock = len(listened_to_rock)
num_pop = len(listened_to_pop)
num_techno = len(listened_to_techno)

# Calculate the fractions of how much each genre has been listened to
denominator = num_rock + num_pop + num_techno
percent_rock = (num_rock / denominator)
percent_pop = (num_pop / denominator)
percent_techno = (num_techno / denominator)

percent_random = 0
random_rock_pop = 0
random_rock_techno = 0
random_pop_techno = 0

# Check if and which of the fractions are less than 0.1 apart and if they are, ignore them.
if abs(percent_rock - percent_pop) <= 0.1 and abs(percent_rock - percent_techno) <= 0.1 and abs(percent_techno - percent_pop) <= 0.1:
    percent_rock = 0
    percent_pop = 0
    percent_techno = 0
    percent_random = 5

if abs(percent_rock - percent_pop) <= 0.1:
    random_rock_pop = percent_rock + percent_pop
    percent_rock = 0
    percent_pop = 0

if abs(percent_rock - percent_techno) <= 0.1:
    random_rock_techno = percent_rock + percent_techno
    percent_techno = 0
    percent_rock = 0

if abs(percent_techno - percent_pop) <= 0.1:
    random_pop_techno = percent_pop + percent_techno
    percent_pop = 0
    percent_techno = 0

# Round the fractions into whole numbers
songs_rock = round(percent_rock * 5)
songs_pop = round(percent_pop * 5)
songs_techno = round(percent_techno * 5)
songs_rock_pop = round(random_rock_pop * 5)
songs_rock_techno = round(random_rock_techno * 5)
songs_pop_techno = round(random_pop_techno * 5)

# Adjusting the values in case we end up with a value different than 5, because of the rounding.
all_songs = songs_rock + songs_pop + songs_techno + songs_rock_pop + songs_rock_techno + songs_pop_techno
difference_under = 0
difference_over = 0
if all_songs - 5 < 0:
    difference_under = abs(all_songs - 5)
elif all_songs - 5 > 0:
    difference_over = abs(all_songs - 5)

# Create lists with lists so that we can later get random list in case we have equal values
rock_pop = [rock_names, pop_names]
rock_techno = [rock_names, techno_names]
pop_techno = [pop_names, techno_names]
all_names = [rock_names, pop_names, techno_names]

# For loops to fill the recommendations list
for i in range(songs_rock):
    recommendations.append(random.choice(rock_names))
for i in range(songs_pop):
    recommendations.append(random.choice(pop_names))
for i in range(songs_techno):
    recommendations.append(random.choice(techno_names))

for i in range(percent_random):
    random_genre = random.choice(all_names)
    recommendations.append(random.choice(random_genre))

for i in range(songs_rock_pop):
    random_genre_rock_pop = random.choice(rock_pop)
    recommendations.append((random.choice(random_genre_rock_pop)))

for i in range(songs_rock_techno):
    random_genre_rock_techno = random.choice(rock_techno)
    recommendations.append((random.choice(random_genre_rock_techno)))

for i in range(songs_pop_techno):
    random_genre_pop_techno = random.choice(pop_techno)
    recommendations.append((random.choice(random_genre_pop_techno)))

for i in range(difference_under):
    recommendations.append(random.choice(playlist_names))

for i in range(difference_over):
    recommendations.remove(random.choice(recommendations))

# Recursive function to check if we have the same song twice or more.
# If we do the copy is removed and a new song is picked from the same genre.
# This is repeated until we get a list with no copies
def double_song() -> str:
    no_double = True
    double_check = []
    for i in recommendations:
        if i not in double_check:
            double_check.append(i)
        else:
            if i in rock_names:
                recommendations.append(random.choice(rock_names))
            if i in pop_names:
                recommendations.append((random.choice(pop_names)))
            if i in techno_names:
                recommendations.append(random.choice(techno_names))
            recommendations.remove(i)
            no_double = False

    if no_double == False:
        double_song()

    return f"Dear user,\nHere is our suggest song from our week 2 Discover Weekly:\n{recommendations}\nHope you will enjoy it!"

print(double_song())

