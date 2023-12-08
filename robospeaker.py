# import os
# import pyttsx3
#
# if __name__ == '__main__':
#     print("Welcome to robo-speaker")
#     x = input("Enter your command here")
#     command= f"say{x}"
#     os.system(command)


import pyttsx3

def text_to_speech(text):
    # Initialize the Text-to-Speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    # engine.setProperty('rate', 150)  # Speed of speech

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

text = input()
text_to_speech(text)

