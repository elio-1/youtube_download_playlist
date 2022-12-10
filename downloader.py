from pytube import YouTube, Playlist
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
