import yt_dlp
import json
from pathlib import Path
import os

SUBTITLES_PATH = "subtitles"

ydl_opts = {
    "writesubtitles": "auto",
    "skip_download": True,
    "subtitlesformat": "json3",
    "allsubtitles": True,
    "outtmpl": f"{SUBTITLES_PATH}/%(uploader_id)s/%(id)s/%(ext)s",
    "verbose": False,
    "compat_opts": {"no-live-chat": True},
    "ignoreerrors": True
}

channel_list = []
with open("data_sample/channel_with_subs.txt", "r") as f:
    channel_list = f.read().splitlines()

for channel in channel_list:
    info = {}
    channel_name = channel.rsplit("@")[1]
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel)

    if not os.path.exists("Thai-Youtube-info"):
        os.makedirs("Thai-Youtube-info")
    with open(f"Thai-Youtube-info/{channel_name}.json", "w") as f:
        json.dump(info, f)

p = list(Path(SUBTITLES_PATH).glob("*/*/*.json3"))
for path in p:
    newname = path.parent.joinpath(f"{path.stem.split('.')[1]}.json3")
    path.rename(newname)

# delete empty folder (no subtitle)
p = list(Path(SUBTITLES_PATH).glob("*/*/"))
for path in p:
    # delete empty folder
    if len(list(path.glob("*.json3"))) == 0:
        path.rmdir()
