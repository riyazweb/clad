import os
from claude_api import Client
"""
Reverse engineering of Google Bard
"""
import yt_dlp

from moviepy.video.VideoClip import TextClip
from moviepy.video.tools.subtitles import SubtitlesClip
from whisper.utils import write_srt
import whisper
from bing_image_downloader import downloader
from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.fx.all import volumex

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ColorClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.all import resize
import moviepy.editor as mp
 
import os
 
 
import re
 
import os
 
# Import either speak or speak2 from the custom_voice modules based on the user input

print(
        """
        ██████╗ ██╗██████╗ ██████╗ ██╗  ██╗
        ██╔══██╗██║██╔══██╗██╔══██╗╚██╗██╔╝
        ██████╔╝██║██████╔╝██║  ██║ ╚███╔╝ 
        ██╔══██╗██║██╔══██╗██║  ██║ ██╔██╗ 
        ██████╔╝██║██║  ██║██████╔╝██╔╝ ██╗
        ╚═════╝ ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝

        """,
    )
def download_video(video_link, filename):
    ydl_opts = {
        'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
        'outtmpl': f'{filename}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])


def get_cookie():
    cookie = 'sessionKey=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; intercom-device-id-lupk8zyo=b7514ddf-eb6a-4fd5-9950-fc988056aa43; intercom-session-lupk8zyo=ZlRuYm05MEJZNDc1OERCRVZ6Y1d2aURmUWt4dHo4b1NCUHl4SGg4NW5nRWRRdGtTQzlOWWl4a1pvSXNtOVVPby0tZDNpV1dVZTRxbnhFbzFSWWgzQ3hIdz09--a45b5044ec1596ac2dbffcd4a41f115230b8aa51; __cf_bm=OrSLgeavrTKQOAljQjiXakJJ8qbXVq8dVRSNySWFQ44-1690121636-0-AYBqR0nyXxol8TI328D0FM5RDCuKFx80opsMxO87gciTIZdjhvAHBMegV5miYbNrp+y0U9ONADtqhNkRKRZYTYI='
    if not cookie:
        raise ValueError("Please set the 'cookie' environment variable.")
    return cookie

def main():
    cookie = get_cookie()
    claude = Client(cookie)
    conversation_id = None

    print("Welcome to BIRD Chat!")

    while True:
        
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Thank you!")
            break

        if not conversation_id:
            conversation = claude.create_new_chat()
            conversation_id = conversation['uuid']

            response = claude.send_message(user_input, conversation_id)
            print("Chatbot:", response)
            choice = input("Enter 1 or 2: ")

            if choice == "1":
              from feautures.custom_voice import speak
            elif choice == "2": 
              from feautures.custom_voice2 import speak
            else:
               print("Invalid choice")
      
            n = input("Enter 'n' (y/n): ")
            y = n.lower() == 'y'

           
            cop = f"{response}"
            if y:
                cop = cop.split('\n', 1)[1]
            cp = re.sub(r'[^\w\s]', '', cop)

            video_link = input("Enter the video URL: ")
            top = input("images:")
         
            fish = input("Enter the out: ")

            # start_time = int(
            #     input("Enter the start time (in seconds) for the video segment: "))
           
            option = int(input("1 for g 2 for b:"))
            limit = int(input("no of images:"))
            speak(cp)
            # Set the dimensions of the video

            VIDEO_WIDTH = 480
            VIDEO_HEIGHT = 854
            # Download the video
            print("Downloading video...")

            filename = f'{fish}'

            video_filename = f"{fish}.mp4"
            download_video(video_link, filename)

            print(f"Video saved as {video_filename}")

            from pygoogle_image import image as pi

            # Set the directory path to the folder containing the images
            import PIL


            # Split the video into 60-second segments and process each segment
            # Split the video into 60-second segments and process each segment
            video_clip = VideoFileClip(video_filename)

            resized_clip = resize(
                video_clip, width=VIDEO_WIDTH, height=VIDEO_HEIGHT)

            # Add the audio track to the video
            audio_filename = 'data.mp3'
            audio_clip = AudioFileClip(audio_filename)
            audio_duration = audio_clip.duration

# Set the duration of the video to match the audio duration
            video_duration = audio_duration


           
            if resized_clip.duration > video_duration:
                resized_clip = resized_clip.subclip(0, video_duration)

            # Create a blank clip with the target dimensions
            background_clip = ColorClip((VIDEO_WIDTH, VIDEO_HEIGHT), color=[
                                        0, 0, 0], duration=resized_clip.duration)

            # Place the resized video clip at the center of the blank clip
            x_pos = (VIDEO_WIDTH - resized_clip.w) / 2
            y_pos = (VIDEO_HEIGHT - resized_clip.h) / 2
            video_clip_centered = CompositeVideoClip(
                [background_clip, resized_clip.set_pos((x_pos, y_pos))])

            final_clip = video_clip_centered.set_audio(audio_clip)
            IMAGE_PATHS = []
            if option == 1:
                for element in top.split(','):

                    pi.download(keywords=f'{element}', limit=limit)

                    # Replace spaces in title with hyphens
                    dog = element.replace(" ", "_")
                    folder_path = f"images/{dog}/"
                    if not os.path.exists(folder_path):
                        continue
                        # Get the file paths to all the images in the folder except the first two
                    for f in os.listdir(folder_path):
                        if f.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                            image_path = os.path.join(folder_path, f)
                            with PIL.Image.open(image_path) as img:
                                width, height = img.size
                                if width > 80 and height > 36:
                                    IMAGE_PATHS.append(image_path)

            elif option == 2:
                for element in top.split(','):
                    dog = element.replace(".", " ")
                    downloader.download(f"{dog}", limit=limit, output_dir="images",
                                        adult_filter_off=True, force_replace=False)

                    folder_path = f"images/{dog}/"
                    if not os.path.exists(folder_path):
                        continue
                        # Get the file paths to all the images in the folder
                    image_paths = [os.path.join(folder_path, f) for f in os.listdir(
                        folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
                    # Add the image paths to the list
                    IMAGE_PATHS += image_paths
            else:
                print("Invalid option entered. Please enter either 1 or 2.")
            # Set the directory path to the folder containing the images
            folder_path = f"images/{dog}/"

            # Create a list of image clips
            image_clips = []
            for image_path in IMAGE_PATHS:
            # Open the image using PIL
           
                    # Create an ImageClip from the image path
                image_clip = ImageClip(image_path)

                    # Resize the image clip to fit the video width while maintaining aspect ratio
                new_height = int(VIDEO_WIDTH / image_clip.w * image_clip.h)
                image_clip = image_clip.resize((VIDEO_WIDTH, new_height))

                    # Set the position of the image clip to be centered
                image_clip = image_clip.set_position(("center", "center"))

                    # Set the start time and duration of the image clip
                image_clip = image_clip.set_start(10)
                image_clip = image_clip.set_duration(2)

                    # Add the image clip to the list
                image_clips.append(image_clip)

            # Add the image clips to the video clip using CompositeVideoClip
            for i, image_clip in enumerate(image_clips):
                if i == 0:
                    final_clip = CompositeVideoClip([final_clip, image_clip])
                else:
                    final_clip = CompositeVideoClip(
                        [final_clip, image_clip.set_start(i*5)])

            # Set the desired fish file name
            fish_filename = f"{fish}.mp4"

            # Check if the file already exists
            if os.path.isfile(fish_filename):
                # If it does, add a number to the filename to create a unique name
                basename, extension = os.path.splitext(fish_filename)
                i = 1
                while os.path.isfile(f"{basename}_{i}{extension}"):
                    i += 1
                fish_filename = f"{basename}_{i}{extension}"

            # Write the final video file with the updated filename
            final_clip.write_videofile(fish_filename, fps=30)
            # FONT = "Muroslant.otf"
            # input_path = f"{fish}.mp4"
            # print("Transcribing audio...")
            # model = whisper.load_model("base")
            # result = model.transcribe(input_path, verbose=False)

            # subtitle_path = os.path.splitext(input_path)[0] + ".srt"
            # with open(subtitle_path, "w", encoding="utf-8") as srt_file:
            #     write_srt(result["segments"], file=srt_file)

            # print("Generating subtitles...")
            # orig_video = VideoFileClip(input_path)

            # def generator(txt): return TextClip(txt,
            #                                     font=FONT if FONT else "Courier",
            #                                     fontsize=48,
            #                                     color='white',
            #                                     size=orig_video.size,
            #                                     method='caption',
            #                                     align='center',)
            # subs = SubtitlesClip(subtitle_path, generator)

            # print("Compositing final video...")
            # final = CompositeVideoClip(
            #     [orig_video, subs.set_position('center', 'middle')])
            # final_path = os.path.splitext(input_path)[0] + "_final.mp4"
            # final.write_videofile(final_path, fps=orig_video.fps)
            # file_names = [f"{filename}"]
            # for file_name in file_names:
            #     if os.path.exists(file_name):
            #         os.remove(file_name)
            #         print(f"File '{file_name}' deleted successfully.")
            #     else:
            #         print(f"File '{file_name}' does not exist.")

        

if __name__ == "__main__":
    main()
