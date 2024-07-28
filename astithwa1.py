import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
from playsound import playsound

print('Loading your AI personal assistant ASTITHWA')


def speak(audio_file):
    playsound(audio_file)


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Astithwa\Input\GM1_1.wav")
        print("Good Morning. How are you feeling today?")
    elif hour >= 12 and hour < 18:
        speak("Astithwa\Input\Ga1.wav")
        print("Good Afternoon. Remember to take breaks and be kind to yourself.")
    else:
        speak("Astithwa\Input\GE1.wav")
        print("Good Evening. How was your day?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Astithwa\Input\Pardon1.wav")
            return "None"
        return statement


speak("Astithwa\Input\Load1.wav")
wishMe()

if __name__ == '__main__':
    #supportive_statements = [
    #    "path/to/your/audio/supportive_statement_1.wav",
    #    "path/to/your/audio/supportive_statement_2.wav",
        # Add more paths to your supportive audio files here
    #]

    therapeutic_questions_responses = {
        "i am not feeling well": [
            "Astithwa\Input\I am not feeling well1.m4a.wav"
            # Add more paths to your audio responses here
        ],
        "i feel sad": [
            "Astithwa\Input\I-feel-sad1.m4a.wav"
            # Add more paths to your audio responses here
        ],
        "i feel anxious": [
            "Astithwa\Input\I feel anxious1.m4a.wav"
            # Add more paths to your audio responses here
        ],
        "i feel lonely": [
            "Astithwa\Input\I feel lonely1.m4a.wav"
            # Add more paths to your audio responses here
        ],
        "i feel stressed": [
            "Astithwa\Input\I-feel-stressed1.m4a.wav"
            # Add more paths to your audio responses here
        ],
        "i need help": [
            "Astithwa\Input\I-need-help1.m4a.wav"
            # Add more paths to your audio responses here
        ],
        "i feel overwhelmed": [
            "Astithwa\Input\I-feel-overwhelmed1.m4a.wav"
            # Add more paths to your audio responses here
        ],
        "i can't do this": [
            "Astithwa\Input\I can't do this1.m4a.wav"
            # Add more paths to your audio responses here
        ]
    }

    while True:
        speak("Astithwa\Input\Help1.wav")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("Astithwa\Input\Load1.wav")
            print('your personal assistant ASTITHWA is shutting down, Goodbye')
            break

        if 'wikipedia' in statement:
            speak("path/to/your/audio/searching_wikipedia.wav")
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("path/to/your/audio/according_to_wikipedia.wav")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("path/to/your/audio/youtube_open.wav")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("path/to/your/audio/google_open.wav")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("path/to/your/audio/gmail_open.wav")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("path/to/your/audio/whats_city_name.wav")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(f"path/to/your/audio/weather_description.wav")
                print("Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak("path/to/your/audio/city_not_found.wav")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"path/to/your/audio/time_is.wav")
            print(f"The time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('path/to/your/audio/who_am_i.wav')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("path/to/your/audio/who_made_me.wav")
            print("I was built by Team Atrilligence")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("path/to/your/audio/stackoverflow_open.wav")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('path/to/your/audio/news_open.wav')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('path/to/your/audio/ask_question.wav')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(f"path/to/your/audio/answer_is.wav")
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("path/to/your/audio/log_off.wav")
            subprocess.call(["shutdown", "/l"])

        else:
            # If none of the commands are recognized, provide a supportive statement or therapeutic response
            found_response = False
            for key in therapeutic_questions_responses:
                if key in statement:
                    responses = therapeutic_questions_responses[key]
                    response = responses.pop(0)
                    speak(response)
                    print(response)
                    found_response = True
                    therapeutic_questions_responses[key].append(response)
                    break

          #  if not found_response:
          #      response = supportive_statements.pop(0)
          #      speak(response)
          #      print(response)
          #      supportive_statements.append(response)

    time.sleep(3)
