from pytube import YouTube
link = input("Enter the link: ")
yt = YouTube(link)

print("Title: ",yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of video: ",yt.length,"seconds")
#Description of video
print("Description: ",yt.description)
#Rating
print("Ratings: ",yt.rating)

ys = yt.streams.get_highest_resolution()
#Starting download
print("Downloading...")
ys.download("D:")
print("Download completed!!")

#printing all the available streams
#print(yt.streams)

#print(yt.streams.filter(only_audio=True))