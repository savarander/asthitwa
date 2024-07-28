import speech_recognition as sr
import pyttsx3
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

print('Loading your AI personal assistant ASTITHWA')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning. How are you feeling today?")
        print("Good Morning. How are you feeling today?")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon. Remember to take breaks and be kind to yourself.")
        print("Good Afternoon. Remember to take breaks and be kind to yourself.")
    else:
        speak("Good Evening. How was your day?")
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
            speak("I'm sorry, I didn't catch that. Could you please say it again?")
            return "None"
        return statement

speak("Loading your AI personal assistant ASTITHWA")
wishMe()


if __name__ == '__main__':
    supportive_statements = [
        "I'm here for you.",
        "It's okay to feel what you're feeling.",
        "Take a deep breath.",
        "You are stronger than you think.",
        "You are not alone.",
        "Your feelings are valid.",
        "It's okay to ask for help.",
        "Remember to take care of yourself.",
        "You are important.",
        "I'm listening.",
        "Would you like to talk about what's on your mind?",
        "Remember to be kind to yourself.",
        "It's okay to take things one step at a time.",
        "You are capable of overcoming this.",
        "It's okay to take a break.",
        "You are doing your best.",
        "You deserve to be happy.",
        "I'm proud of you for reaching out.",
        "It's okay to cry.",
        "You are not a burden.",
        "You are enough.",
        "It's okay to feel down sometimes.",
        "Your feelings matter.",
        "Take one day at a time.",
        "You are brave.",
        "It's okay to ask for support.",
        "You are valued.",
        "You are not defined by your struggles.",
        "It's okay to take it easy.",
        "You are loved.",
        "It's okay to not be okay.",
        "You are making progress, even if it doesn't feel like it.",
        "You are not your thoughts.",
        "You are worthy of love and respect.",
        "It's okay to prioritize your mental health.",
        "You are doing the best you can.",
        "You are resilient.",
        "It's okay to seek help.",
        "You are not alone in this.",
        "You are enough just as you are.",
        "You have the strength to get through this.",
        "You are not your mistakes.",
        "It's okay to need time for yourself.",
        "You are a good person.",
        "You are not defined by your past.",
        "You have people who care about you.",
        "You deserve to feel better.",
        "It's okay to take care of your mental health.",
        "You are not weak for asking for help.",
        "You are making a difference.",
        "It's okay to take things slow.",
        "You are worthy of happiness.",
        "You are not alone in feeling this way.",
        "You are more than your struggles.",
        "It's okay to talk about your feelings.",
        "You are deserving of love.",
        "You are capable of change.",
        "It's okay to have bad days.",
        "You are doing a great job.",
        "You are not alone in this journey.",
        "You are enough, just as you are.",
        "You are not your thoughts or feelings.",
        "You have the power to get through this.",
        "You are worthy of self-care.",
        "It's okay to seek out comfort.",
        "You are valuable.",
        "You are not defined by your depression.",
        "You have a bright future ahead.",
        "You are not alone, even when it feels like it.",
        "You are capable of overcoming challenges.",
        "You are loved, even when you don't feel it.",
        "You are not your struggles.",
        "It's okay to take things one day at a time.",
        "You are a strong and capable person.",
        "You are worthy of all good things.",
        "You are not alone in this battle.",
        "You are important to those around you.",
        "You deserve to be happy and healthy.",
        "You are not your depression.",
        "You are a valuable person.",
        "You have people who care about you.",
        "You are not a burden.",
        "You are doing your best.",
        "It's okay to feel overwhelmed.",
        "You are not alone in feeling this way.",
        "You are stronger than you think.",
        "It's okay to take breaks.",
        "You are not alone in this fight.",
        "You are deserving of love and happiness.",
        "You are not defined by your mental health.",
        "You are a wonderful person.",
        "You are not alone, and help is available.",
        "You are capable of overcoming this.",
        "You are not your depression."
    ]

    therapeutic_questions_responses = {
        "i am not feeling well": [
            "I'm sorry to hear that. Can you tell me more about what's going on?",
            "It's okay to feel this way. I'm here to listen.",
            "Would you like to talk about it? Sometimes sharing can help.",
            "Remember, it's okay to ask for help when you need it."
        ],
        "i feel sad": [
            "I'm here for you. Do you want to talk about what's making you feel this way?",
            "It's okay to feel sad sometimes. Is there anything specific that's bothering you?",
            "You don't have to go through this alone. I'm here to support you.",
            "Would it help to talk about what's making you feel sad?"
        ],
        "i feel anxious": [
            "Anxiety can be really tough. Do you want to talk about what's making you feel this way?",
            "It's okay to feel anxious. I'm here to listen and support you.",
            "Would you like to share more about what's causing your anxiety?",
            "Remember, you are not alone. Many people feel this way and there is support available."
        ],
        "i feel lonely": [
            "Loneliness can be really hard. I'm here for you.",
            "It's okay to feel lonely sometimes. Do you want to talk about it?",
            "You are not alone. I'm here to support you.",
            "Would you like to share more about what's making you feel lonely?"
        ],
        "i feel stressed": [
            "Stress can be overwhelming. Would you like to talk about what's causing it?",
            "It's okay to feel stressed. I'm here to listen and support you.",
            "Would you like to share more about what's making you feel stressed?",
            "Remember to take breaks and take care of yourself. You are doing your best."
        ],
        "i need help": [
            "It's okay to ask for help. How can I assist you?",
            "You are not alone. I'm here to help you.",
            "What do you need help with? I'm here to support you.",
            "It's okay to seek support. How can I assist you today?"
        ],
        "i feel overwhelmed": [
            "Feeling overwhelmed can be tough. Would you like to talk about it?",
            "It's okay to feel overwhelmed. I'm here to listen.",
            "Would you like to share more about what's making you feel this way?",
            "Remember to take things one step at a time. You are doing your best."
        ],
        "i can't do this": [
            "I'm here for you. Can you tell me more about what's making you feel this way?",
            "It's okay to feel this way sometimes. You are stronger than you think.",
            "Would you like to talk about what's making you feel like this?",
            "Remember, you don't have to go through this alone. I'm here to support you."
        ]
    }

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant ASTITHWA is shutting down, Goodbye')
            print('your personal assistant ASTITHWA is shutting down, Goodbye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What's the city name?")
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
                speak("Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidity) +
                      "\n description  " +
                      str(weather_description))
                print("Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak("City Not Found")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am ASTITHWA version 1.0, your personal assistant. I am programmed to perform minor tasks like opening YouTube, Google Chrome, Gmail, and Stack Overflow, predicting time, taking a photo, searching Wikipedia, predicting weather in different cities, getting top headline news from Times of India, and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Team Atrilligence")
            print("I was built by Team Atrilligence")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is Stack Overflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India, Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer computational and geographical questions. What question do you want to ask now?')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok, your PC will log off in 10 seconds. Make sure you exit from all applications")
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

            if not found_response:
                response = supportive_statements.pop(0)
                speak(response)
                print(response)
                supportive_statements.append(response)

    time.sleep(3)
