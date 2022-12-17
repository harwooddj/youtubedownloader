from pytube import YouTube
from pytube.cli import on_progress
from os import path

def download(url):
    youtubeObject = YouTube(link, on_progress_callback = on_progress)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    destination = path.expanduser("~") + "/Downloads"
    try:
        youtubeObject.download(destination)
    except:
        print("Download error")
    else:
        print("Download successful")

link = input("Insert your download link here! URL: ")
download(link)
print("(:")
