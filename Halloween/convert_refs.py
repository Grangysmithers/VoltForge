import librosa
import soundfile as sf

print("Converting reference voices...")

monster_audio, monster_sr = librosa.load(
    "Monster voice.mp3",
    sr=None,
    mono=True
)

sf.write(
    "monster_reference.wav",
    monster_audio,
    monster_sr
)

print("Monster reference converted.")

witch_audio, witch_sr = librosa.load(
    "Witch voice.mp3",
    sr=None,
    mono=True
)

sf.write(
    "witch_reference.wav",
    witch_audio,
    witch_sr
)

print("Witch reference converted.")

print("Done!")