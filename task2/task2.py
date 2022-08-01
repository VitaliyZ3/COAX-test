import requests
from datetime import datetime
from moviepy.editor import *
import os

# function to get unix date to create filename
def get_unix_date():
    return datetime.timestamp(datetime.now())

# function to download video from url
def download_video(url:str):
    try:
        # download video from url
        r = requests.get(url, allow_redirects=True)
    except:
        print("Error opening url")
    finally:
        # create directory to save the video
        path = "resources/video/"
        if not os.path.exists(path):
            os.makedirs(path)
        # create videoname variable
        video_name = f"{path}video-{get_unix_date()}.mp4"
        print(video_name)
        # write content from our url to file
        open(video_name, 'wb').write(r.content)

        return video_name

# function to convert video to gif with with time frames
def convert_to_gif(video_name:str, start_time:int, end_time:int):
    # create directory to save the gif
    path = "resources/gif/"
    if not os.path.exists(path):
        os.makedirs(path)
    # create gif name variable
    gif_name = f"{path}gif-{get_unix_date()}.gif"
    # create VideoFileClip object
    clip = VideoFileClip(video_name)
    # cut video with time witg user time frames
    clip = clip.subclip(start_time, end_time)
    # convertin our file to gif
    clip.write_gif(gif_name)

    return gif_name

url = input("Enter your tik-tok video link: ")
start_time, end_time = input("Enter the start and end times of your clip: ").split()

v = download_video(url)
gif = convert_to_gif(v, start_time, end_time)
print(f"You`r gif here ==> {gif}")