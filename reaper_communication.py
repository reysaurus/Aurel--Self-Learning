import serial
import cv2
import pyaudioy
import wave
import threading
import numpy as np

arduino = serial.Serial('COM3', 9600)

# setup Audio
p = pyaudio.PyAudio()

# fungsi ke arduino untuk data audio
def send_audio_to_arduino():
    while True:
        # menangkap suara dari mic
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=44100,
                        input=True
                        frames_per_buffer=1024)
        data = np.frombuffer(stream.read(1024), dtype=np.int16)

        # mengirim data ke arduino (memproses audio)
        if arduino.IsOpen():
            arduino.write(b'S') # mengirim perintah untuk menyalakan speaker

        stream.stop_stream()

# fungsi untuk melakukan realtime camera Reaper 505
def capture_video():
    cap = cv2.VideoCapture(0) # membuka kamera
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Reaper Cam', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

# thread untuk audio dan camera realtime
audio_thread = threading.Thread(target=send_audio_to_arduino)
audio_thread.start()

video_thread = threading.Thread(target=capture_video)
video_thread.start()

# agar program tetap berjalan
while True:
    pass
