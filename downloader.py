from pytube import YouTube, Playlist, extract
from pytube.cli import on_progress
import os
from pathlib import Path
import sys
import re

def Dplaylist(link, res="360p"):
    p = Playlist(link)
    title = p.title.replace(":", "")
    output_path = str(Path.home() / "Downloads" / title)
    try:
        os.mkdir(output_path)
    except FileExistsError: 
        pass
    video_urls = p.video_urls
    for video in video_urls:
        yt = YouTube(video, on_progress_callback=on_progress)
        file_path = output_path + '\\' + yt.title + '.mp4'
        if os.path.exists(file_path):
            pass
        else:
            if extract.is_age_restricted(yt.watch_html):
                print(yt.title + "is aged restricted and couldn't be download")
                pass
            else:
                yt.streams.filter(res=res).first().download(output_path=output_path)
            

def Dlink(link, res="360p"):
    yt = YouTube(link, on_progress_callback=on_progress)
    output_path = str(Path.home() / "Downloads")
    yt.streams.filter(res=res).first().download(output_path=output_path)


link = input("Link: ")
if len(sys.argv) == 2:
    res = sys.argv[1]
else:
    res = "360p"

is_playlist = re.search("list", link) != None

if is_playlist:
    Dplaylist(link, res)
else:
    Dlink(link, res)
