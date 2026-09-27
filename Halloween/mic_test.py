import sounddevice as sd
import soundfile as sf

sample_rate = 44100
duration = 5

print("Recording for 5 seconds... Speak now!")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1
)

sd.wait()

sf.write("my_voice.wav", audio, sample_rate)

print("Recording finished!")
print("Saved as my_voice.wav")