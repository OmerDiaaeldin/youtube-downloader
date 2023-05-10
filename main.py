from pytube import YouTube

def Download(link, resolution: int = 480):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_by_resolution(resolution)
    try:
        youtubeObject.download()
    except:
        print("An error occured")
    print("Downloaded succesfully")


link = input("Enter the link: ")
resolution = int(input("Enter the resolution: "))
Download(link, resolution=720)