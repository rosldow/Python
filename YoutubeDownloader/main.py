from pytube import YouTube
def Download(url):
    youtubeObject = YouTube(url)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occured")
    print("The video has been downloaded successfully")



url = input("Enter video url: ")

Download(url)
