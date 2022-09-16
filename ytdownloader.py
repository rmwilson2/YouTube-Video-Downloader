from pytube import YouTube
from sys import argv

try:
    link = argv[1]
    path = argv[2]
    video_url = YouTube(link)
except IndexError:
    print('Incorrect syntax. Provide the following format: python3 ytdownloader.py URL PATH')
    exit()

# if link or path == False:
#     print('Incorrect syntax. Provide the following format: python3 ytdownloader.py URL PATH')


print("Title: ", video_url.title)
print("Views: ", video_url.views)

target_res = video_url.streams.get_highest_resolution()

print("\nDownloading Video... ")
target_res.download(path)