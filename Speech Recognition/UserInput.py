import speech_recognition as sr
r = sr.Recognizer()
def talk():
	r.energy_threshold = 4000
	with sr.Microphone() as source:               # use the default microphone as the audio source
		audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
		issue = r.recognize_google(audio)
		try:
			print("You said: " + issue)    				# recognize speech using Google Speech Recognition
		except LookupError:                            # speech is unintelligible
			print("Could not understand audio")

	return ("{}".format(issue))
