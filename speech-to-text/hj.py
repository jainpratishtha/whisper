import pyaudio
import speech_recognition as sr
r = sr.Recognizer()

harvard = sr.AudioFile('file_trim.wav')
with harvard as source:
	audio = r.record(source)



