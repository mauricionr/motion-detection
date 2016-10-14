from picamera import PiCamera
from io import BytesIO
from time import sleep
import telegram

camera = PiCamera();

camera.start_preview()

for i in range(5):
    sleep(1)
    camera.capture('/home/pi/Documents/images/image%s.png' % i)

camera.stop_preview()

