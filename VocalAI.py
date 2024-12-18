import openai

import speech_recognition as sr

import pyttsx3

openai.api_key = "YOUR API KEY"
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

while True:
    # create a new recognizer instance
    r = sr.Recognizer()

    # use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
    if (text == "Break" or text == "break"):
        break
    message = text
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set the voice and language
    voice_id = "com.apple.speech.synthesis.voice.samantha"
    engine.setProperty('voice', voice_id)

    # Convert text to speech
    engine.say(reply)
    engine.runAndWait()
    text = ""


