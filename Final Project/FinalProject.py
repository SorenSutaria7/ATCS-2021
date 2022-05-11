import numpy as np
import pandas as pd
from python_speech_features import mfcc
import scipy.io.wavfile as wav
from python_speech_features import logfbank
import sox
import pickle
from tempfile import TemporaryFile
import os
import pickle
import random
import operator
import math
import numpy as np
import matplotlib as plt
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score

#Taking in the large data set
genres = "/Users/Soren/Desktop/ATCS-2021/Final Project/genres"

#converts all the files within the genre file to .wav files
#Citation: github of suhasshrinivasan who had
# certain lines of code that assisted me to convert from .au to .wav
for current_genre in os.walk(genres):
    os.chdir(current_genre)
    for audio_file in os.listdir(current_genre):
        os.system("sox " + str(audio_file) + " " + str(audio_file[:-3]) + ".wav")
    os.system("rm *.au")

directory = "/Users/Soren/Desktop/ATCS-2021/Final Project/genres"
f = open("data.dat", 'wb')
i = 0

#Walks through the files and reads in datapoints about the wave files
#Sends them over to the load dataset file in which the data set is created

#Citation: music genre classification on dataflair (similar to my project)
# Used the same selected data and the same data loading method
for current_genre in os.walk(genres):
    os.chdir(current_genre)
    i += 1
    if i == 2:
        break
    for wav_file in os.listdir(current_genre):
        (rate, sig) = wav.read(wav_file)
        mfcc_feat = mfcc(sig, rate, winlen=0.020, appendEnergy=False)
        covariance = np.cov(np.matrix.transpose(mfcc_feat))
        mean_matrix = mfcc_feat.mean(0)
        feature = (mean_matrix, covariance, i)
        pickle.dump(feature, f)


dataset = []
genres = []

#Loads the datapoints into a dataset
def loadDataset(filename , split , trSet , teSet):
    with open(filename, 'rb') as f:
        #places the correct genre
        genres.append(str(os.cwd()))
        while True:
            try:
                dataset.append(pickle.load(f))
            except EOFError:
                f.close()
                break
    for x in range(len(dataset)):
        if random.random() <split :
            trSet.append(dataset[x])
        else:
            teSet.append(dataset[x])

trainingSet = []
testingSet = []
loadDataset("data.dat", 0.8, trainingSet, testingSet)
print(dataset)

''' Load Data '''
# Read in features and classes
feature_genre = genres.values
feature_signal = dataset["sig"].values
feature_rate = dataset["rate"].values
feature_covariance = dataset["covariance"].values
feature_mfcc_feat = dataset["mfcc_feat"].values
feature_mean_matrix= dataset["mean_matrix"].values

#Transform qualitative data to quantitative
genre_transformer = LabelEncoder().fit(feature_genre)
feature_genre = genre_transformer.transform(feature_genre)


# Set the features to be a 2d array
features = np.array([feature_genre, feature_signal, feature_rate, feature_covariance,
                     feature_mfcc_feat, feature_mean_matrix]).transpose()
print(features)

# Get the unique classes for the labels
class_labels = np.unique(genres)

#Standardize data
scaler = StandardScaler().fit(features)
features = scaler.transform(features)
print(features)

# Split test and training data
features_train, features_test, genres_train, genres_test = train_test_split(features, genres, test_size=0.2)

values = []
accuracy = []
'''Create the Model'''
num_training_points = len(features_train)
for k in range(2, num_training_points):
    model = KNeighborsClassifier(n_neighbors=k).fit(features_train, genres_train)
    genres_pred = model.predict(features_test)
    values.append(k)
    accuracy.append(accuracy_score(genres_test, genres_pred))
    print("Accuracy:", accuracy_score(genres_test, genres_pred))

#Plotting a K value vs Accuracy graph to help me optimize k value
plt.plot(values, accuracy)
plt.xlabel("K Values")
plt.ylabel("Accuracy")
plt.title("Accuracy vs K Values")
plt.show()















