import os
import random


def getRandomFile():
    path = os.path.abspath(os.path.dirname(__file__))
    pathAudio = path + '/static/audio/'

    files = os.listdir(pathAudio)
    index = random.randrange(0, len(files))
    randomFile = files[index]
    pathRandom = '/static/audio/' + randomFile

    return {'name': randomFile, 'path': pathRandom}
