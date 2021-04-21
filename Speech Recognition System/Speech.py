#importing speech recognition library
import speech_recognition as sr 
from gtts import gTTS 
from googletrans import Translator
import wikipedia
import warnings
import os
import random

#for ignoring the warnings
warnings.filterwarnings('ignore')
r=sr.Recognizer()
class Speech_recognition:
    #listening from the microphone
    def listen(self):
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source,phrase_time_limit=5)
            try:
                text=r.recognize_google(audio)
                print("You said " +text)
            except sr.UnknownValueError:
                text="System could not understand your audio"
                self.speak(text)
        return text

    def speak(self,text=None,lan='en'):
        if text is None:
            text=self.listen()
        result=gTTS(text=text, lang=lan, slow=False) 
        result.save("play.mp3")
        os.system(" mpg123 play.mp3")

    #searching from the wikipedia
    def search_wikipedia(self):
        self.speak('Welcome to wikipedia, What do you want to search')
        text=self.listen()
        try:
            search=wikipedia.summary(text, sentences=2)
            print(search)
            self.speak(search)
        except wikipedia.exceptions.DisambiguationError as e:
            s = random.choice(e.options)
            p = wikipedia.page(s)
            search=wikipedia.summary(p, sentences=2)
            print(search)
        except:
            print('No results found')
            self.speak('No results found')
    #translating the text
    def translate(self,from_lang="en",to_lang="hi"):
        self.speak('Welcome to translator, Speak the word you want to translate')  
        sentence=self.listen()
        # Translator method for translation 
        try:
            translator = Translator(service_urls=['translate.googleapis.com']) 
            text_to_translate = translator.translate(sentence,src=from_lang,  dest= to_lang)       
            result=text_to_translate.text
            '''you can change translate from_lang and to_lang by passing parameter of lang: Default(English to hindi)'''
            self.speak(text=result,lan='hi')
        except:
            self.speak('Could not translate')

if __name__=="__main__":
    while True:
        speak_recog=Speech_recognition()
        text1=speak_recog.listen()
        if "hello" in text1.lower():
            speak_recog.speak("Welcome Sir, what do you want to do")
            while True:
                text2=speak_recog.listen()
                if "wikipedia" in text2.lower():
                    speak_recog.search_wikipedia()
                elif "translator" in text2.lower():
                    speak_recog.translate()
                elif "bye" in text2.lower():
                    speak_recog.speak('OK exiting the system')
                    exit()
        


        