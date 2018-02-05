import cv2
import glob
import random
import numpy as np

emotions = ["neutral", "happy", "sadness"]
fishface = cv2.face.FisherFaceRecognizer_create()
data = {}


def get_files(emotion):
    files = glob.glob("dataset/%s/*" % emotion)
    random.shuffle(files)
    training = files[:int(len(files) * 0.8)]
    prediction = files[-int(len(files) * 0.2):]
    return training, prediction


def make_sets():
    training_data = []
    training_labels = []
    prediction_data = []
    prediction_labels = []
    for emotion in emotions:
        training, prediction = get_files(emotion)
        # Append data to training and prediction list, and generate labels 0-7
        for item in training:
            image = cv2.imread(item)  # open image
            image = cv2.resize(image, (60, 60))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert to grayscale
            training_data.append(gray)  # append image array to training data list
            training_labels.append(emotions.index(emotion))

        for item in prediction:  # repeat above process for prediction set
            image = cv2.imread(item)
            image = cv2.resize(image, (60, 60))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            prediction_data.append(gray)
            prediction_labels.append(emotions.index(emotion))
        print(emotion)

    return training_data, training_labels, prediction_data, prediction_labels


def run_recognizer():
    training_data, training_labels, prediction_data, prediction_labels = make_sets()

    print "training fisher face classifier"
    print "size of training set is:", len(training_labels), "images"
    fishface.train(training_data, np.asarray(training_labels))
    print "predicting classification set"
    cnt = 0
    correct = 0
    incorrect = 0
    for image in prediction_data:
        pred, conf = fishface.predict(image)
        if pred == prediction_labels[cnt]:
            correct += 1
            cnt += 1
        else:
            incorrect += 1
            cnt += 1
    correctNum = ((100 * correct) / (correct + incorrect))
    fishface.write("saved.json")


def runLoaded():
    training_data, training_labels, prediction_data, prediction_labels = make_sets()
    fishface.load("fishfacestart.json")
    image = cv2.imread("happy.png", 0)
    image = cv2.resize(image, (350, 350))
    print (len(image[0]))
    print (len(image[1]))
    pred, conf = fishface.predict(image)
    print emotions[pred]
    return 0


if __name__ == "__main__":
    metascore = []
    # for i in range(15):
    correct = run_recognizer()
    print (correct)