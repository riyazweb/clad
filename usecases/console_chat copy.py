import os
from claude_api import Client
"""
Reverse engineering of Google Bard
"""
from moviepy.video.VideoClip import TextClip
from moviepy.video.tools.subtitles import SubtitlesClip
 
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
            top = input("images:")
            option = int(input("1 for g 2 for b:"))
         
            fish = input("output:")
      
            limit = int(input("limit of images :"))

            n = input("Enter 'n' (y/n): ")
            y = n.lower() == 'y'

            
            cop = f"{response}"
            if y:
                cop = cop.split('\n', 1)[1]
            cp = re.sub(r'[^\w\s]', '', cop)

            speak(cop)
            # Set the dimensions of the video

     
            VIDEO_WIDTH = 480
            VIDEO_HEIGHT = 854
         

                # Set the duration of each image

                # Set the path to the music file
            MUSIC_PATH = "data.mp3"
            # Replace spaces in title with hyphens
            # Download images of cats
            # Download images of cats
            from pygoogle_image import image as pi

            # Set the directory path to the folder containing the images
            import PIL

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

                    downloader.download(f"{element}", limit=limit, output_dir="images",
                                        adult_filter_off=True, force_replace=False)

                    folder_path = f"images/{element}/"
                    if not os.path.exists(folder_path):
                        continue
                        # Get the file paths to all the images in the folder
                    image_paths = [os.path.join(folder_path, f) for f in os.listdir(
                        folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
                    # Add the image paths to the list
                    IMAGE_PATHS += image_paths
            else:
                print("Invalid option entered. Please enter either 1 or 2.")

            num_images = len(IMAGE_PATHS)
            audio_clip = AudioFileClip(MUSIC_PATH)
            audio_duration = audio_clip.duration
            IMAGE_DURATION = audio_duration / num_images

            # Create a list of video clips
            # Set the blur amount
            # Create a list of video clips
            video_clips = []
            for image_path in IMAGE_PATHS:
                # Create an image clip for the current image
                image_clip = ImageClip(image_path)
                # Calculate the new height based on the aspect ratio of the original image
                new_height = int(
                    VIDEO_WIDTH / image_clip.w * image_clip.h)
                # Resize the image to fit the video dimensions without black bars
                image_clip = image_clip.resize(
                    (VIDEO_WIDTH, new_height))
                image_clip = image_clip.set_position(
                    ("center", "center"))
                image_clip = image_clip.set_duration(IMAGE_DURATION)

                # Create a black background clip
                bg_clip = ColorClip(
                    (VIDEO_WIDTH, VIDEO_HEIGHT), color=(0, 0, 0))
                bg_clip = bg_clip.set_duration(IMAGE_DURATION)

                # Combine the image clip with the background clip
                video_clip = CompositeVideoClip([bg_clip, image_clip])

                # Append the video clip to the list
                video_clips.append(video_clip)

                # Concatenate the video clips in a loop until the audio ends

            # Concatenate the video clips in a loop until the audio ends
             # Concatenate the video clips in a loop until the audio ends
            audio_clip = AudioFileClip(MUSIC_PATH)
            audio_duration = audio_clip.duration
            final_clip = concatenate_videoclips(
                video_clips, method="compose", bg_color=(0, 0, 0))
            final_clip = final_clip.set_duration(
                audio_duration).loop(duration=audio_duration)

            # Set the audio file for the final video clip
            final_clip = final_clip.set_audio(
                audio_clip.set_duration(final_clip.duration))

            # Set the audio file for the final video clip
            # Set the desired output file name
            filename = f"{fish}.mp4"

            # Check if the file already exists
            if os.path.isfile(filename):
                # If it does, add a number to the filename to create a unique name
                basename, extension = os.path.splitext(filename)
                i = 1
                while os.path.isfile(f"{basename}_{i}{extension}"):
                    i += 1
                filename = f"{basename}_{i}{extension}"

                # Write the video file with the updated filename
            final_clip.write_videofile(filename, fps=30)

        

if __name__ == "__main__":
    main()
