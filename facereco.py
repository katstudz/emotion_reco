import os
import cv2


class EmotionClassifier:
    def __init__(self):
        self.emotions = ["neutral", "anger", "disgust", "happy", "surprise", "fear", "sadness"]
        self.fishface = cv2.face.createFisherFaceRecognizer()
        self.fishface.load("final.json")
        face_cascade_path = "haarcascade/haarcascade_frontalface_alt.xml"
        self.face_cascade = cv2.CascadeClassifier(os.path.expanduser(face_cascade_path))

    def find_face_roi(self, image):
        scale_factor = 1.1
        min_neighbors = 3
        min_size = (30, 30)
        faces = self.face_cascade.detectMultiScale(image, scaleFactor=scale_factor, minNeighbors=min_neighbors,
                                              minSize=min_size)

        for (x, y, w, h) in faces:
            cutedImg = image[y:y + h, x:x + w]
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
            return cutedImg, image
        return [], image

    def make_prediction(self, img):
        cutedImg, image = self.find_face_roi(img)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (60, 60))
        pred, conf = self.fishface.predict(img)
        return self.emotions[pred], conf


def run():

    emotion_classifier = EmotionClassifier()
    cam = cv2.VideoCapture(0)

    while True:
        ret_val, img = cam.read()
        emotion, certainty = emotion_classifier.make_prediction(img)
        print (emotion, certainty)
        if cv2.waitKey(1) == 27:
            cam.release()
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
