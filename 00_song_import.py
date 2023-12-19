import lyricsgenius
import shutil

#Read in key
with open("credentials/genius_key.txt", 'r') as myFile:
    key = myFile.read()
#Create connection to API
genius = lyricsgenius.Genius(key)


#Search for songs with API connection
    #Can take quite a while. ~23min for 220 songs. 
    #Many of which were skipped (Instrumentals/Skits)
artist = genius.search_artist(max_songs = None,
                                sort = "title",
                                artist_name = "MF DOOM") #All caps when you spell the man name


#Can't specify file path using this command, move manually below
artist.save_lyrics("lyrics.json")

#Move to data folder
shutil.move("lyrics.json", "data/lyrics.json")