import ffmpeg_streaming
import thumbnail
from ffmpeg_streaming import Formats
import sys
import datetime
import os

def change_it(fn):
    video = ffmpeg_streaming.input('../simulated_server_storage/'+fn)

    def monitor(ffmpeg, duration, time_, time_left, process):
        per = round(time_ / duration * 100)
        sys.stdout.write(
            "\rTranscoding...(%s%%) %s left [%s%s]" %
            (per, datetime.timedelta(seconds=int(time_left)), '#' * per, '-' * (100 - per))
        )
        sys.stdout.flush()

    hls = video.hls(Formats.h264())
    thumbnail.extract(fn)
    hls.auto_generate_representations()
    os.mkdir('static/media/'+fn[:-4:1])

    hls.output('static/media/'+fn[:-4:1]+'/'+fn[:-4:1]+'.m3u8', monitor=monitor)



if __name__ =='__main__':
    change_it('LVL5-GREIFER.mp4')