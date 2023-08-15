import subprocess
# v= 'en-IN-NeerjaNeural'
voice = 'en-CA-ClaraNeural'


def speak(data):
    voice = 'en-US-ChristopherNeural'
    filename = "data.mp3"

    # Split the input text into chunks
    chunks = data.split()
    chunk_size = 10000
    chunks = [chunks[i:i + chunk_size]
              for i in range(0, len(chunks), chunk_size)]

    # Convert and write each chunk to file
    for chunk in chunks:
        text = ' '.join(chunk)
        command = f'edge-tts --voice "{voice}" --text "{text}"  --rate=+24%  --write-media "{filename}"'
        subprocess.run(command, shell=True)

    return True
