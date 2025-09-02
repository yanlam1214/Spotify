# 🎵 Discover Weekly 

A simplified version of Spotify’s Discover Weekly recommendation system. This project simulates how new songs can be suggested to users over time, based on their listening history, favorite genres, and mood shifts.

📌 Project Overview

This project mimics the idea behind Spotify’s "Discover Weekly," where users receive personalized song recommendations every week. Since the scope is simplified, the algorithm evolves in three weekly stages:

Week 1 – Individual Choice

Users receive 5 suggested songs based on similarity to their past listening history.

Rule: If a playlist contains 3 songs the user already listened to and 3 songs they haven’t heard yet, that playlist is chosen.

From that playlist, 5 songs are suggested.

Week 2 – Genres

Songs are classified into Pop, Rock, or Techno.

The dominant genre(s) are determined based on listening percentages:

If one genre >10% higher than the second most played → user is classified under that genre.

If the difference ≤10% → multiple genres are considered equally important.

5 new songs are suggested from the identified genre(s).

Week 3 – Mood Shifts

Songs are classified into Happy, Party, Calming, or Lounge.

A song can belong to more than one category (e.g., "Happy + Party").

Mood-based suggestions:

If one mood dominates → more songs of that type are suggested.

If multiple moods are close in count → the system balances suggestions across them.

Again, 5 songs are recommended.

⚙️ Assumptions

100 users, each with a listening history.

100 pre-made playlists, each containing 50 songs.

Recommendations may repeat across weeks.

Simplified rules for determining "dominant" genres/moods.

🛠️ Tech Stack

Python (core logic & algorithms)

Data structures: lists, dictionaries for users/playlists/songs

🚀 How It Works

Generate user listening history.

Apply weekly algorithms (Week 1 → Week 2 → Week 3).

Output suggested songs for each user.

📊 Example Flow

User A listens to: Rock (20), Pop (18), Techno (5).

Week 1: Finds a playlist match, suggests 5 songs.

Week 2: Rock & Pop are close → suggest from both.

Week 3: Mostly “Calming” songs → suggest more calming tracks.
