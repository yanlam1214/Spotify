import csv
import random

# 
# Solution strategy = Divide the problem into several subproblems


# Create an empty list to store the 100 lists
playlists = []

# Read the file and get the list of sublists
with open('spotify-dataset.csv', encoding='utf-8-sig') as all_songs:
    csv_dict_reader = csv.DictReader(all_songs)
    sublists = []
    for row in csv_dict_reader:
        title = row['title']
        sublists.append(title)

# Generate 100 lists with 50 random sublists from the list of sublists
for i in range(100):

    # Generate a random list of 50 sublists wit h the first elements
    playlists.append(random.sample(sublists, 50))
    
# Set listened_songs to None
listened_songs = None

# Select a random playlist
selected_playlist = random.choice(playlists)

# Select 3 random songs from that playlist and add it to listened_songs
listened_songs = random.sample(selected_playlist, 3)

# Create a function that will recommend 5 random songs from a playlist
def recommended_songs(playlists):
    """Identify the playlist that contains at least 3 songs that the user has listened to
     and 3 songs that the user has not listened to
    """
    # Check if there are at least 3 songs in a playlist that the user has listened to and 
    # 3 songs that the user has not listened to
    for playlist in playlists:
        listened_count = 0
        not_listened_count = 0
        for song in playlist:
            if song in listened_songs:
                listened_count += 1
            else:
                not_listened_count += 1

        # Select the playlist that meets the requirements
        if listened_count >= 3 and not_listened_count >= 3:
            selected_playlist = playlist
            
            # Use a random number generator to select 5 songs from the selected playlist
            selected_songs = random.sample(selected_playlist, 5)
            return selected_songs

# Print the recommended songs    
recommending = recommended_songs(playlists)
print(recommending)