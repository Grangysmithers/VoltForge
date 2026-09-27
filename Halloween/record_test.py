import pyaudio
import wave

# basic settings for recording
FORMAT = pyaudio.paInt16   # type of audio format
CHANNELS = 1                # mono audio (1 mic input)
RATE = 44100                 # sample rate (standard for audio)
CHUNK = 1024                 # how much audio we read at a time
SECONDS = 3                  # how long to record

# start pyaudio
p = pyaudio.PyAudio()

# open the microphone stream
stream = p.open(format=FORMAT,
                 channels=CHANNELS,
                 rate=RATE,
                 input=True,
                 frames_per_buffer=CHUNK)

print("Recording now, speak for 3 seconds...")

frames = []  # this will store all the audio pieces

# keep reading small chunks of audio until 3 seconds is done
for i in range(0, int(RATE / CHUNK * SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished")

# stop and close the mic
stream.stop_stream()
stream.close()
p.terminate()

# save the recorded audio into a file called test.wav
wf = wave.open("test.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print("Saved recording as test.wav")