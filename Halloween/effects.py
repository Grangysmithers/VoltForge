import librosa
import soundfile as sf
import numpy as np
from scipy import signal


def _normalize(y):
    peak = np.max(np.abs(y))
    if peak > 0:
        y = y / peak * 0.92
    return y


def _filter(y, sr, cutoff, kind):
    sos = signal.butter(
        4,
        cutoff,
        btype=kind,
        fs=sr,
        output="sos"
    )
    return signal.sosfilt(sos, y)


def _delay_layer(y, sr, seconds, volume):
    delay = int(seconds * sr)
    result = np.zeros(len(y) + delay)

    result[:len(y)] += y
    result[delay:delay + len(y)] += y * volume

    return result


def witch_effect(input_file, output_file="booth_witch.wav"):

    y, sr = librosa.load(input_file, sr=None, mono=True)

    # Main witch voice: raised, but not cartoonishly high
    main = librosa.effects.pitch_shift(
        y=y,
        sr=sr,
        n_steps=3.2
    )

    # Unsettling second voice
    upper = librosa.effects.pitch_shift(
        y=y,
        sr=sr,
        n_steps=5.8
    )

    # Slightly lower whisper-like body
    shadow = librosa.effects.pitch_shift(
        y=y,
        sr=sr,
        n_steps=-1.2
    )

    length = min(len(main), len(upper), len(shadow))

    main = main[:length]
    upper = upper[:length]
    shadow = shadow[:length]

    # Main voice stays dominant so words remain understandable
    mixed = (
        0.72 * main +
        0.18 * upper +
        0.10 * shadow
    )

    # Remove unnecessary low rumble
    mixed = _filter(mixed, sr, 120, "highpass")

    # Add presence to the witch voice
    presence = _filter(mixed, sr, 1700, "highpass")
    mixed = mixed + 0.12 * presence

    # Mild distortion gives a supernatural texture
    mixed = np.tanh(mixed * 1.35)

    # Short supernatural echo
    mixed = _delay_layer(
        mixed,
        sr,
        seconds=0.065,
        volume=0.16
    )

    mixed = _normalize(mixed)

    sf.write(output_file, mixed, sr)

    return output_file


def monster_effect(input_file, output_file="booth_monster.wav"):

    y, sr = librosa.load(input_file, sr=None, mono=True)

    # Deep but still understandable
    main = librosa.effects.pitch_shift(
        y=y,
        sr=sr,
        n_steps=-3.8
    )

    # Very deep supporting layer
    deep = librosa.effects.pitch_shift(
        y=y,
        sr=sr,
        n_steps=-7.0
    )

    # Keep some original articulation
    natural = y.copy()

    length = min(len(main), len(deep), len(natural))

    main = main[:length]
    deep = deep[:length]
    natural = natural[:length]

    mixed = (
        0.67 * main +
        0.23 * deep +
        0.10 * natural
    )

    # Emphasize dark frequencies
    dark = _filter(mixed, sr, 2200, "lowpass")

    mixed = (
        0.72 * mixed +
        0.28 * dark
    )

    # Controlled growl / saturation
    mixed = np.tanh(mixed * 1.65)

    # Heavy short reflection
    mixed = _delay_layer(
        mixed,
        sr,
        seconds=0.045,
        volume=0.13
    )

    mixed = _normalize(mixed)

    sf.write(output_file, mixed, sr)

    return output_file