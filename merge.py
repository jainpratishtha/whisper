from pydub import AudioSegment
import time
def merge():
	time.sleep(3)
	sound1 = AudioSegment.from_wav("../o.wav")
	# sound2 = AudioSegment.from_wav("test1.wav")

	combined_sounds = sound1
	combined_sounds.export("path.wav", format="wav")
