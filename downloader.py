from pytube import YouTube, Playlist, extract
from pytube.cli import on_progress
import os
from pathlib import Path
import sys
import re


def main():
    link = input("Link: ")
    res, audio_only = arg_parse()
    is_playlist = re.search("list", link) != None
    if is_playlist:
        Dplaylist(link, res=res, only_audio=audio_only)
    else:
        Dlink(link, res=res, only_audio=audio_only)


def Dplaylist(link: str, res="360p", only_audio=False):
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
        file_path = output_path + "\\" + yt.title + ".mp4"
        if os.path.exists(file_path):
            pass
        else:
            if extract.is_age_restricted(yt.watch_html):
                print(yt.title + "is aged restricted and couldn't be download")
                pass
            else:
                yt.streams.filter(res=res, only_audio=only_audio).first().download(
                    output_path=output_path
                )


def Dlink(link: str, res="360p", only_audio=False):
    yt = YouTube(link, on_progress_callback=on_progress)
    output_path = str(Path.home() / "Downloads")
    yt.streams.filter(res=res, only_audio=only_audio).first().download(
        output_path=output_path
    )


def arg_parse():
    audio_only = False
    res = "360p"
    if len(sys.argv) == 2:
        match sys.argv[1]:
            case "144p":
                res = "144p"
            case "240p":
                res = "240p"
            case "360p" | 360:
                res = "360p"
            case "480p" | 480:
                res = "480p"
            case "720p" | 720:
                res = "720p"
            case "720p60":
                res = "720p"
            case "1080p" | "1080p60" | "hd" | 1080:
                res = "1080p60"
            case "audio" | "a" | "-a" | "novid" | "song":
                res = None
                audio_only = True
            case "-h" | "--help":
                print(
                    f"Usage {sys.argv[0]} [options]\nOptions: \n[resolutions] ex: {sys.argv[0]} 1080p\n[audio only] ex: {sys.argv[0]} novid | {sys.argv[0]} audio | {sys.argv[0]} a\nIf no arguments are specify the default is video with 360p"
                )
            case _:
                pass
    return res, audio_only


if __name__ == "__main__":
    main()
