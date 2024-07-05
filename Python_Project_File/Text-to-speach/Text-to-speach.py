from gtts import gTTS
import os


def text_to_speech(text, lang='en', slow=False):

    tts = gTTS(text=text, lang=lang, slow=slow)
    filename = "Output Audio.mp3"

    # Save the speech audio into file
    tts.save(filename)
    print(filename)

    # Optionally, play the audio file
    # os.system(f"mpg321 {filename}")


# Example usage
text_to_speech("hi welcome to my profile", lang='en', slow=True)
