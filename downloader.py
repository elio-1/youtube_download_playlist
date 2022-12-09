from pytube import YouTube, Playlist

def Dlink(link, res="360p"):
    stream = YouTube(link).streams.filter(res=res).first()
    return stream

def Dplaylist(link, res="360p"):
    p = Playlist(link)
    for video in p.videos:
        video.streams.filter(res=res).first().download()

# print(Dlink("https://www.youtube.com/watch?v=DEHsvQ3Ylwg&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&index=40"))
Dplaylist("https://www.youtube.com/playlist?list=PLfsEr6YiELADnmHqadhdZTBUngZfEMgpz")