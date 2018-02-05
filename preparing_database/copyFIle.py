import  os
from shutil import copy2

def getFolderName(i):
    return "00" + str(i)



path = "/home/katarzyna/PycharmProjects/FaceReco/source_emotion"
selectedSetPath = "/home/katarzyna/PycharmProjects/FaceReco/selected_set/"
emotionPath = "/home/katarzyna/PycharmProjects/FaceReco/Emotion/"


files = os.listdir(path)
print len(files)

# emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", ""]
emotions = ["suprise", "sadness", "fear", "disgust", "anger", "happy"]
emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness" , "7 = surprise"]
# 0 = neutral, 1 = anger, 2 = contempt, 3 = disgust, 4 = fear, 5 = happy, 6 = sadness, 7 = surprise
emotionsNum = [0,0,0 ,0,0,0]
for folder in files:
    personFolder = path +"/"+ str(folder)

    personEmotion = os.listdir(personFolder)
    for i in range(0, 6):
        oneEmotionFolder = getFolderName(i + 1)
        if personEmotion.__contains__(oneEmotionFolder):
            personEmotionListFolder = personFolder + "/" + oneEmotionFolder
            personEmotionList = os.listdir(personFolder + "/" + oneEmotionFolder)

            if len(personEmotionList) > 0:

                #getEmotionDestctription
                thisEmotionPath = emotionPath + folder + "/" + oneEmotionFolder
                print os.listdir(thisEmotionPath)


                try:
                    src = personEmotionListFolder + "/" + str(personEmotionList[-1])
                    dst = selectedSetPath + emotions[i]+ "/" # + str(emotionsNum[i]) + ".jpg" #+ "/" + str(personEmotionList[-1])
                    emotionsNum[i] = emotionsNum[i] + 1
                    #shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext
                    copy2(src, dst)
                except OSError:
                    print "trudno"




