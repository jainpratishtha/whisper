from pydub import AudioSegment
def out():
	sound = AudioSegment.from_wav("path.wav")
	sound = sound.set_channels(1)
	sound.export("test_out1.wav", format="wav")
