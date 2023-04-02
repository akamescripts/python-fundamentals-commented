from pytube import YouTube

# ask the user for the YouTube video URL
url = input("Enter the YouTube video URL: ")

# create a YouTube object
yt = YouTube(url)

# print the video title
print("Downloading:", yt.title)

# select the highest resolution video and audio streams
stream = yt.streams.get_highest_resolution()

# download the video
stream.download()

# print a success message
print("Download complete!")
