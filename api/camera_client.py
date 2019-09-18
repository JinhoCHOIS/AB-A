import io
import socket
import struct
import picamera

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.0.87', 6000)) # host ip, port 입력
connection = client_socket.makefile('wb')

try:
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (320, 240)
            camera.framerate = 15
            stream = io.BytesIO()

            for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                connection.write(struct.pack('<L', stream.tell()))
                connection.flush()
                stream.seek(0)
                connection.write(stream.read())
                stream.seek(0)
                stream.truncate()
        connection.write(struct.pack('<L', 0))
    finally:
        connection.close()
        client_socket.close()

except BrokenPipeError :
    print('timeend')
