import os.path
from os.path import join as pjoin
from ffmpy import FFmpeg
# spectrogram
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
# mel spectrogram
import numpy as np
import librosa.display
# neuron networks
import tensorflow as tf
from tensorflow import keras

import librosa


def convert_to_wav(input_path, output_path):
    if os.path.isfile(output_file):
        return 'File ' + output_file + ' already exists'
    ff = FFmpeg(inputs={input_path: None}, outputs={output_path: None})
    ff.cmd
    ff.run()
    return 'File ' + input_path + ' was successfully converted to ' + output_path


def print_spectrogram(output_file):
    sample_rate, samples = wavfile.read(output_file)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

    plt.pcolormesh(times, frequencies, spectrogram)
    plt.imshow(spectrogram)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()
    return 'Painting plot...'


def create_MEL_spectrogram(output_file):
    y, sr = librosa.load(output_file)
    S = librosa.feature.melspectrogram(y=y, sr=sr)
    return S


def print_MEL_spectrogram(output_file):
    S = create_MEL_spectrogram(output_file)

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max), fmax=8000)
    plt.colorbar(format='%+2.0f dB')
    plt.title(output_file)
    plt.show()
    # plt.tight_layout()
    return 'Painting plot...'


def create_and_save_spectrogram(output_file):
    S = create_MEL_spectrogram(output_file)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max), fmax=8000)
    plt.colorbar(format='%+2.0f dB')

    name = output_file[:-4]
    plt.title(name)
    plt.savefig(name, bbox_iches='tight')
    return 'Save sectrogram to file: ' + name + '.png'


# Preparing file
path_to_file = pjoin('../data', 'die.au')
# path_to_file = pjoin('../data', 'disco.00000.au')
# path_to_file = pjoin('../data', 'metal.00000.au')
output_file = path_to_file[:-2] + 'wav'
result = convert_to_wav(path_to_file, output_file)
print(result)

# Painting spectrogram
print_MEL_spectrogram(output_file)

create_and_save_spectrogram(output_file)
