from youtubesearchpython import Search
import string, random, os
from pytube import YouTube


def byl(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def get_video_url(search):
    allSearch = (Search(search, limit=0))
    turn = str(allSearch.result())
    if not turn == "{'result': []}":
        r = byl(20)
        e = "'}, 'link': '" 
        f = "', 'shelfTitle': "
        turn = turn.replace(e, r)
        trash, p = turn.split(r)
        link, trash = p.split(f)
        return link  
    else:
        print("Video not found")
        return "Error"

def download_audio(url):
    if url == "Error":
        return
    yt = YouTube(url) 
    ys = yt.streams.get_audio_only() 
    try:
        ys.download()  # Download Audio Only
        new_title = str(str(yt.title) + ".mp3") 
        old_title = str(str(yt.title) + ".mp4") 
        os.rename(old_title, new_title)  
    except FileExistsError:
        return
    except:
        print("Could not Rename File")
        return


download_audio(get_video_url("")
