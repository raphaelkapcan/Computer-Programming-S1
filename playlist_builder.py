# PART 1
playlist = ["Testify", "Renegades of Funk", "Suck My Kiss", "Sleep Now in the Fire", "My Lovely Man"]
new_song = input("Enter a song title to add to the playlist: ")
new_song = new_song.strip().title()
playlist.append(new_song)
# PART 2
print("Total number of songs:", len(playlist))
playlist.insert(0, "Sabatoge")
playlist.remove("My Lovely Man")
del playlist[2]
print("Alphabetical preview:", sorted(playlist))
playlist.sort()
playlist.reverse()
# PART 3
print("Is 'Californiacation' in playlist?", "Californiacation" in playlist)
for song in playlist:
    print(song.upper())
# PART 4
for i in range(len(playlist)):
    print(i + 1, playlist[i])
