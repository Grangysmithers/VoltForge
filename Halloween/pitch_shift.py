import librosa
import soundfile as sf

# load the file we recorded earlier
audio, sample_rate = librosa.load("test.wav", sr=None)

# n_steps tells it how much to shift the pitch
# negative number = deeper/scary voice
# positive number = higher/squeaky voice
n_steps = -6

# apply the pitch shift
new_audio = librosa.effects.pitch_shift(audio, sr=sample_rate, n_steps=n_steps)

# save the new voice as a separate file
sf.write("witch_voice.wav", new_audio, sample_rate)

print("Done, saved as witch_voice.wav")