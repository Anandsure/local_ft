import subprocess
def extract(vid):
    video_input_path = '../simulated_server_storage/'
    img_output_path = 'static/thumbnails/'
    subprocess.call(['ffmpeg', '-i', video_input_path+vid, '-ss', '00:00:00.000', '-vframes', '1', img_output_path+vid[:-4:1]+'.jpg'])

if __name__ == '__main__':
    extract('dumb_dude_syke.mp4')