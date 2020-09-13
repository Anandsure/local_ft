# import required libraries
from vidgear.gears import NetGear
import cv2

# define various tweak flags
options = {'flag' : 0, 'copy' : False, 'track' : False,'compression_param':cv2.IMREAD_COLOR}

# Define Netgear Client at given IP address and define parameters (!!! change following IP address '192.168.x.xxx' with yours !!!)
client = NetGear(address = '192.168.0.103', port = '5454', protocol = 'tcp',  pattern = 1, receive_mode = True, logging = True, **options)

# loop over
while True:

    # receive frames from network
    frame = client.recv()

    # check for received frame if Nonetype
    if frame is None:
        break


    # {do something with the frame here}


    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()