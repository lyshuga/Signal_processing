import numpy as np
import scipy #Library for signal analysis
import matplotlib.pyplot as plt #Plot
import numpy as np #Operations
import cv2 #Read images and do operations
import IPython.display as ipd
import numpy.random #For generating noise
import copy

from copy import deepcopy

from numpy import linalg

from scipy import signal
from scipy.io import wavfile #Read wavfiles
from scipy.signal import welch,stft,istft #Get power density estimated, short fourier transform

audio_file = 'mmusic.wav'

fs, data = wavfile.read(audio_file)

Ls = len(data)

print('Setting up the frame parameters\n')


inputSDR = 7


wtype = 'hann'
w = 8192
a = w / 4
M = 2*8192

shrinkage = 'EW'
print('Setting up shrinkage operator: %s\n', shrinkage)

verbose = True


print('Generating clipped signal\n')
[data_clipped, masks, theta, trueSDR, percentage] = clip_sdr(data, inputSDR)
print('Clipping threshold %4.3f, true SDR value is %4.2f dB and %4.2f%% samples has been clipped \n', theta, trueSDR, percentage)

