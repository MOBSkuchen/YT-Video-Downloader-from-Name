from youtubesearchpython import Search  # install with 'pip3 install youtube-search-python'
import string, random, os  # String + Random for creating the Random chars, os for renaming the file
from pytube import YouTube  # Pytube for Downloading

def byl(length):  # Generating a Random String
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def get_video_url(search):
    allSearch = (Search(search, limit=0))  # Search for Videos with 'search' accept 0 (1)
    turn = str(allSearch.result())  # Get the result as Json
    if not turn == "{'result': []}":
        r = byl(20)  # Generate Random String with length 20
        e = "'}, 'link': '"  # Define what to get
        f = "', 'shelfTitle': "
        turn = turn.replace(e, r)
        trash, p = turn.split(r)
        link, trash = p.split(f)  # Get the String
        return link  # Return the String
    else: # Detected Error
        print("Video not found") 
        return "Error" # Tell the Programm to Stop

def download_audio(url):
    if url == "Error": # Detected Error
        return # Stop
    yt = YouTube(url)  # Define Video
    ys = yt.streams.get_audio_only()  # Get Audio Only
    try:
        ys.download()  # Download Audio Only
        new_title = str(str(yt.title) + ".mp3")  # Get new name
        old_title = str(str(yt.title) + ".mp4")  # Get old name
        os.rename(old_title, new_title)  # Rename file
    except FileExistsError: # If already Dowloaded
        return
    except:
        print("Could not Rename File") # Other Error
        return

download_audio(get_video_url(""))  # Do Everything
