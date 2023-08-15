import os
from claude_api import Client
import re
def get_cookie():
    cookie = 'sessionKey=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; intercom-device-id-lupk8zyo=b7514ddf-eb6a-4fd5-9950-fc988056aa43; intercom-session-lupk8zyo=ZlRuYm05MEJZNDc1OERCRVZ6Y1d2aURmUWt4dHo4b1NCUHl4SGg4NW5nRWRRdGtTQzlOWWl4a1pvSXNtOVVPby0tZDNpV1dVZTRxbnhFbzFSWWgzQ3hIdz09--a45b5044ec1596ac2dbffcd4a41f115230b8aa51; __cf_bm=OrSLgeavrTKQOAljQjiXakJJ8qbXVq8dVRSNySWFQ44-1690121636-0-AYBqR0nyXxol8TI328D0FM5RDCuKFx80opsMxO87gciTIZdjhvAHBMegV5miYbNrp+y0U9ONADtqhNkRKRZYTYI='
    if not cookie:
        raise ValueError("Please set the 'cookie' environment variable.")
    return cookie

def main():
    cookie = get_cookie()
    claude = Client(cookie)
    conversation_id = None

    print("Welcome to Claude AI Chat!")

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
        import openai
        from PIL import Image, ImageDraw, ImageFont, ImageOps
        import textwrap

        import os
        import time

        from bing_image_downloader import downloader

        openai.api_key = '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'
       
        dog = input("ENTER THE PHOTO NAME:")

        n = input("Enter 'n' (y/n): ")
        y = n.lower() == 'y'

            
        cop = f"{response}"
        if y:
            cop = cop.split('\n', 1)[1]
        OP = re.sub(r'[^\w\s]', '', cop)

    
      
        downloader.download(f"{dog}", limit=1, output_dir="images",
                                adult_filter_off=True, force_replace=False)

            # Set the directory path to the folder containing the images
        img = Image.open(f"images/{dog}/image_1.jpg")

            # Resize the image to 600x600
        img = img.resize((600, 600))

            # Display the image

            # Create an Image object with the randomly chosen background color

            # Create a Draw object for drawing on the image
        draw = ImageDraw.Draw(img)
            # Create a black layer with transparency of 30%
        alpha = 77  # 30% transparency
        black_layer = Image.new(
            'RGBA', (img.width, img.height), (0, 0, 0, alpha))
            # Choose a font and size for the text
            # reduced font size to 24
        font = ImageFont.truetype(
            'Muroslant.otf', size=40)

            # Define the text to draw
        text = f"{OP}"

            # Wrap the text to fit within the image width
        wrapped_text = textwrap.wrap(text, width=25)

            # Calculate the position of the text in the center of the image
        x = (img.width - draw.textbbox((0, 0),
                                    wrapped_text[0], font=font)[2]) // 2
        y = (img.height -
            font.getsize(wrapped_text[0])[1] * len(wrapped_text)) // 2

            # Draw each line of wrapped text on the image
        for line in wrapped_text:
            text_width, text_height = draw.textsize(line, font=font)
            draw.text(((img.width - text_width) // 2, y), line, fill='white', font=font, outline='black')
            y += text_height


        img_filename = f"{dog}.png"

        img.save(img_filename)
        print(f"Saved image as {img_filename}")
         

 

if __name__ == "__main__":
    main()
