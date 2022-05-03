# import numpy as np
# import pandas as pd
# from python_speech_features import mfcc
# import scipy.io.wavfile as wav
# from python_speech_features import logfbank
import sox

import os

genres = "/test_genre"

for current_genre in os.walk(genres):
    os.chdir(current_genre)
    for audio_file in os.listdir(current_genre):
        os.system("sox " + str(audio_file) + " " + str(audio_file[:-3]) + ".wav")
    os.system("rm *.au")













