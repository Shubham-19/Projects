from translate import Translator
import UserInput as UI
import win32com.client

def main():
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    if __name__ == '__main__':
        try:
            print("Welcome to the Python Translator")
            speaker.Speak("Welcome to the Python Translator")
            
            print("What language would you like your text translated to?")
            speaker.Speak("What language would you like your text translated to?")
            lang = UI.talk().lower()
            speaker.Speak('You chose {}'.format(lang))
            print("Say something to the bot to convert...")
            speaker.Speak("Say something to the bot to convert...")
            
            print("Human: ")
            request = UI.talk().lower()
            if(request.lower() == 'exit'):
                print('Getting you otta here!')
                speaker.Speak('You have requested to exit, so we are getting you otta here! We hope you got your query resolved, Thank you for using our service')

                return 0
            else:
                Tl = Translator(to_lang = lang)
                line = Tl.translate(request)
                print("Bot: " + line)
                speaker.Speak('{} in {} sounds like {}'.format(request, lang, line))
            
            main()
        except KeyboardInterrupt:        
            print("Program Interrupted")

main()
