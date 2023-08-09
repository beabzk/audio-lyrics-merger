import os
from mutagen.id3 import ID3, USLT

def add_lyrics(mp3_file, lrc_file):

    # Load the MP3 file using mutagen
    audio = ID3(mp3_file)

    # Read the lyrics from the LRC file
    with open(lrc_file, "r", encoding="utf-8") as lrc:
        lyrics = lrc.read()

    # Add the USLT frame
    audio.add(USLT(encoding=3, text=lyrics))

    # Save the updated tag data
    audio.save()

if __name__ = "__main__":
    for mp3_file in os.listdir("."):
        if mp3_file.endswith(".mp3"):
            lrc_file = mp3_file.replace(".mp3", ".lrc")
            if os.path.exists(lrc_file):
                add_lyrics(mp3_file, lrc_file)