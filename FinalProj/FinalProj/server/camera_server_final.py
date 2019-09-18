import io
import socket
import struct
from PIL import Image
import cv2
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model


def preprocess_input(x, v2=True):
    x = x.astype('float32')
    x = x / 255.0
    if v2:
        x = x - 0.5
        x = x * 2.0
    return x


face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
emotion_classifier = load_model('total_2.h5')
EMOTIONS = ["angry", "disgust", "scared", "happy", "sad", "surprised", "neutral"]

emo_cnt = [0, 0, 0, 0, 0, 0, 0]
emo = 'neutral'

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)

server_socket = socket.socket()
server_socket.bind(('141.223.140.11', 8000))

while True:
    server_socket.listen(0)

    emo_cnt = np.array([0, 0, 0, 0, 0, 0, 0])
    flag = 0

    print("=====서버 준비 완료======")

    # Accept a single connection and make a file-like object out of it
    conn, addr_info = server_socket.accept()
    connection = conn.makefile('rb')

    print('Connected')
    try:
        while True:
            # Read the length of the image as a 32-bit unsigned int. If the
            # length is zero, quit the loop
            image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
            if not image_len:
                print('not image_len\n')
              ##  cv2.destroyAllWindows()
                break
            # Construct a stream to hold the image data and read the image
            # data from the connection
            image_stream = io.BytesIO()
            image_stream.write(connection.read(image_len))

            # Rewind the stream, open it as an image with PIL and do some
            # processing on it
            image_stream.seek(0)
            image = Image.open(image_stream)
            cv_image = np.array(image)

            orig_frame = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
            frame = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            faces = face_detection.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

            if len(faces) > 0:
                faces = sorted(faces, reverse=True, key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
                (fX, fY, fW, fH) = faces
                roi = frame[fY:fY + fH, fX:fX + fW]
                roi = cv2.resize(roi, (48, 48))
                roi = preprocess_input(roi)
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                preds = emotion_classifier.predict(roi)[0]
                label = EMOTIONS[preds.argmax()]
                emo_cnt[preds.argmax()] += 1

           ##     cv2.putText(orig_frame, label, (fX, fY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
           ##     cv2.rectangle(orig_frame, (fX, fY), (fX + fW, fY + fH), (0, 0, 255), 2)
                print(label)
                flag = 1

         ##   cv2.imshow('Stream', orig_frame)

            if flag == 0:
                emo = 'neutral'
            else:
                emo = EMOTIONS[emo_cnt.argmax()]
            conn.send(emo.encode())

        ##    if cv2.waitKey(1) & 0xFF == ord('q'):
        ##        break

    finally:
        connection.close()
        conn.close()
        # server_socket.close()
        print("Complete emotion detection")


