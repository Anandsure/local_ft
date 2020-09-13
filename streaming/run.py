import shutil
import time as t
import json

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import transcode
import glob

app = Flask(__name__)

@app.route('/player')
def main():
   return render_template('player.html',click = clicked)
@app.route('/upload')
def upload_file():
   return render_template('uppp.html')

@app.route('/')
def ser():
   filenames=[]
   caption=[]
   for i in glob.glob("static/thumbnails/*.jpg"):
      filenames.append('../'+i)
      caption.append(i[18:-4:1])
   filenames.reverse()
   caption.reverse()
   return render_template('gallery.html',fnames=filenames,cap=caption)

@app.route('/player/update', methods=['POST', 'GET'])
def get_names():
   if request.method == 'POST':
      resp_json = request.get_json()
      global clicked
      clicked = resp_json['text']
   return json.dumps({"response": 'could be anything noone cares'}), 200
      
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      shutil.move(secure_filename(f.filename),'../simulated_server_storage')
      t.sleep(3)
      transcode.change_it(secure_filename(f.filename))
      return render_template('uppp.html')

if __name__ == '__main__':
   global clicked
   clicked = 'dumb_dude_syke'
   app.run(debug=True,host='0.0.0.0')
