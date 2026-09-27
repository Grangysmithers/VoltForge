import torch
import torchaudio
import soundfile as sf
from speechbrain.inference.speaker import EncoderClassifier
from speechbrain.utils.fetching import LocalStrategy

print("=" * 45)
print("SignalVerse - Reference Voice Analyzer")
print("=" * 45)

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device:", device.upper())

print("\nLoading speaker model...")

classifier = EncoderClassifier.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec-ecapa-voxceleb",
    local_strategy=LocalStrategy.COPY,
    run_opts={"device": device}
)

def analyze_voice(filename):
    print(f"\nAnalyzing: {filename}")

    audio, sample_rate = sf.read(filename, dtype="float32")

    signal = torch.from_numpy(audio)

    if signal.ndim == 1:
        signal = signal.unsqueeze(0)
    else:
        signal = signal.T

    # Convert stereo audio to mono
    if signal.shape[0] > 1:
        signal = torch.mean(signal, dim=0, keepdim=True)

    # Model expects 16 kHz audio
    if sample_rate != 16000:
        signal = torchaudio.functional.resample(
            signal,
            sample_rate,
            16000
        )

    signal = signal.to(device)

    with torch.no_grad():
        embedding = classifier.encode_batch(signal)

    print("Voice analyzed successfully.")
    print("Embedding shape:", tuple(embedding.shape))

    return embedding


print("\n--- MONSTER REFERENCE ---")
monster_embedding = analyze_voice("monster_reference.wav")

print("\n--- WITCH REFERENCE ---")
witch_embedding = analyze_voice("witch_reference.wav")

similarity = torch.nn.functional.cosine_similarity(
    monster_embedding.flatten().unsqueeze(0),
    witch_embedding.flatten().unsqueeze(0)
)

print("\n" + "=" * 45)
print("REFERENCE ANALYSIS COMPLETE")
print("Monster/Witch similarity:", round(similarity.item(), 3))
print("=" * 45)