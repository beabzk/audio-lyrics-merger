# Audio Lyrics Merger

`audio-lyrics-merger` is a Python script that embeds lyrics from an LRC file into an MP3 file.

## Requirements

- Python 3.x
- [mutagen](https://pypi.org/project/mutagen/) library

## Usage

1. Install the `mutagen` library by running `pip install mutagen` in a terminal window.
2. Save the `add_lyrics.py` script to your computer.
3. Open a terminal window and navigate to the directory where the script is located.
4. Run the script using the command `python add_lyrics.py`.

The script will process all MP3 and LRC files in the current directory. For each MP3 file, it will look for a corresponding LRC file with the same name (except for the file extension). If it finds one, it will add the lyrics from the LRC file to the MP3 file as a tag.

## Options

By default, the script adds lyrics to the MP3 file without specifying the language or description of the lyrics. If you want to specify these values, you can modify the `add_lyrics` function in the script.

To specify the language of the lyrics, set the `lang` parameter of the `USLT` frame to a three-letter ISO 639-2 code for your language. For example, to specify that the lyrics are in Japanese, you can use `lang='jpn'`.

To specify a description for the lyrics, set the `desc` parameter of the `USLT` frame to a short text string. For example, to add a description that says "Translated Lyrics", you can use `desc='Translated Lyrics'`.

## License

This project is licensed under the MIT License.