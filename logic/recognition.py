import os
import sys
import json
from pytube import YouTube
import urllib.request

input = sys.argv[1]


def printInput(param):
    return param


def getVideoTitles(filePath):

    FILE_PATH = filePath
    lines = []
    with open(FILE_PATH) as f:
        lines = f.readlines()

    for line in lines:
        yt = YouTube(line.strip())
        video = yt.streams.filter(only_audio=True).first()
        print(jsonify(line.strip(), video.title, 'Descargando'))


def jsonify(link, title, status):

    resp = {
        "link": link,
        "title": title,
        "status": status
    }

    return json.dumps(resp)


def getNames(fileRoute):
    with open(fileRoute) as f:
        lines = f.readlines()

    for line in lines:
        download(line.strip())


def download(route):

    SAVE_PATH = "C:/Users/jsidg/Desktop/VIEJO/VIDEO"

  #  try:
    print(route)
    yt = YouTube(route)
    video = yt.streams.filter(only_audio=True).first()
    print(video)
    print(video.title)
    print(video.download(SAVE_PATH))
    print()
    print()


def change():

    pathname = "D:\musica\\"

    for count, filename in enumerate(os.listdir(pathname)):
        print("#### Changing Name ####")
        print("INITIAL FILENAME: " + filename)

        newname = filename.replace("y2mate.com - ", "")
        lenght = len(newname)

        split = newname.split("_")

        newname = newname[(lenght - 15): -4]

        _format = split[len(split) - 1]

        newname = split[0] + _format[-4:]

        os.rename(pathname + filename, pathname + newname)

        print("NEW FILENAME: " + newname)

        print("")
        print("")


# if __name__ == '__main__':
   # main()

getVideoTitles(input)
sys.stdout.flush()
