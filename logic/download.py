import os
import sys
import json
from pytube import YouTube
import urllib.request

input = sys.argv[1]


def download(route):

    SAVE_PATH = "C:/Users/jsidg/Desktop/VIEJO/VIDEO"

    lines = []
    with open(route) as f:
        lines = f.readlines()

    for line in lines:
        yt = YouTube(line.strip())
        video = yt.streams.filter(
            resolution='360p').first()
        video.download(SAVE_PATH)
        print(jsonify(line.strip(), video.title, 'Descargado'))


def jsonify(link, title, status):

    resp = {
        "link": link,
        "title": title,
        "status": status
    }

    return json.dumps(resp)


download(input)
sys.stdout.flush()
