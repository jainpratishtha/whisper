from pydub import AudioSegment
def trim(): 
	
	sound1 = AudioSegment.from_wav("corrections/path-corrected.wav")   
	beginning = sound1[:5000]
	beginning.export("corrections/path-corrected.wav", format="wav")
trim()
