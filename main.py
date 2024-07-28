import requests

def get_lyrics(artist, title):
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('lyrics', 'Lyrics not found.')
    else:
        return 'Error: Unable to fetch lyrics.'

title = input("Song: ")
artist = input("Artist: ")
lyrics = get_lyrics(artist, title)
print(lyrics)
