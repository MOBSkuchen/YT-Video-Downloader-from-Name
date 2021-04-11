from youtubesearchpython import Search # install with 'pip3 install youtube-search-python'
import string,random,os # String + Random for creating the Random chars, os for renaming the file
from pytube import YouTube # Pytube for Downloading
def byl(length): # Generating a Random String
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
def get_video_url(search):
    allSearch = (Search(search, limit=0)) # Search for Videos with 'search' accept 0 (1)
    giek = str(allSearch.result()) # Get the result as Json
    r = byl(20) # Generate Random String with length 20
    e = "'}, 'link': '" # Define what to get
    f = "', 'shelfTitle': "
    giek = giek.replace(e, r)
    trash, p = giek.split(r)
    link, trash = p.split(f) # Get the String
    return link # Return the String
def download_audio(url):
    yt = YouTube(url) # Define Video
    ys = yt.streams.get_audio_only() # Get Audio Only
    ys.download() # Download Audio Only
    new_title = str(str(yt.title) + ".mp3") # Get new name
    old_title = str(str(yt.title) + ".mp4") # Get old name
    os.rename(old_title, new_title) # Rename file
download_audio(get_video_url("Crab Rave")) # Do Everything
