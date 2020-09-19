import os
import json
from moviepy.editor import *


def convert():

    SAVE_PATH = "C:/Users/jsidg/Desktop/VIEJO"

    for count, filename in enumerate(os.listdir(SAVE_PATH + "/VIDEO")):
        video = VideoFileClip(SAVE_PATH + "/VIDEO/" + filename)
        video.audio.write_audiofile(
            SAVE_PATH + "/MUSICA/" + filename[:-4] + '.mp3', bitrate='256k', logger=None)
        video.close()
        print(jsonify('-', filename[:-4], 'Completo'))


def jsonify(link, title, status):

    resp = {
        "link": link,
        "title": title,
        "status": status
    }

    return json.dumps(resp)


convert()
sys.stdout.flush()
