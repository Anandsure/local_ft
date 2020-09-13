# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import cv2

# define various tweak flags
options = {'flag' : 0, 'copy' : False, 'track' : False,'compression_format': '.jpg', 'compression_param':[cv2.IMWRITE_JPEG_QUALITY, 60]}

# Open live video stream on webcam at first index(i.e. 0) device
stream = VideoGear(source='../simulated_server_storage/LVL5-GREIFER.mp4').start()

# Define Netgear server at given IP address and define parameters (!!! change following IP address '192.168.x.xxx' with client's IP address !!!)
server = NetGear(address = '192.168.0.103', port = '5454', protocol = 'tcp',  pattern = 1, logging = True, **options)

# loop over until KeyBoard Interrupted
while True:

  try: 

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # send frame to server
    server.send(frame)

  except KeyboardInterrupt:
    break

# safely close video stream
stream.stop()

# safely close server
server.close()
