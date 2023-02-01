# made by Thk34: https://github.com/thk34
from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

playlist = Playlist("put the link of the playlist here, it must be unlisted or in public but not in private")

playlist.video_urls # displays all of the playlist's musics URLs 
for url in playlist:
    print(url)

for url in playlist:
   YouTube(url).streams.filter(only_audio=True).first().download()
   
os.system('cmd /k "ren *.mp4 *.mp3"')
