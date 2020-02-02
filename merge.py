from pydub import AudioSegment
def merge():
	sound1 = AudioSegment.from_wav("../../../../Downloads/o.wav")
	sound2 = AudioSegment.from_wav("test1.wav")

	combined_sounds = sound1 + sound2
	combined_sounds.export("path.wav", format="wav")
