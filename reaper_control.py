import tkinter as tk
from tkinter import Label
import cv2
import serial
import threading
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

def read_data():
    while True:
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').strip()
            temp, humidity, voltage, current = data.split(', ')
            temp = temp.split(': ')[1]
            humidity = humidity.split(': ')[1]
            voltage = voltage.split(': ')[1]
            current = current.split(': ')[1]

            temp_label.config(text=f"Temperature: {temp}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            voltage_label.config(text=f"Voltage: {voltage}V")
            current_label.config(text=f"Current: {current}A")

        time.sleep(1)


def show_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("RPR-505 Cam", frame)
            cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()

# UI UNTUK APLIKASI
root = tk.Tk()
root.title("Reaper 505 Control Panel")

# LABEL DATA SUHU, KELEMBABAN, VOLTAGE, CURRENT
temp_label = Label(root, text="Temperature: --°C", font=('Helvetica', 16))
temp_label.pack()

humidity_label = Label(root, text="Humidity: --%", font=("Helvetica", 16))
humidity_label.pack()

voltage_label = Label(root, text="Voltage: --V", font=("Helvetica", 16))
voltage_label.pack()

current_label = Label(root, text="Current: --A", font=("Helvetica", 16))
current_label.pack()

#Thread untuk membaca data dari arduino
data_threadn = threading.Thread(target=read_data, daemon=True)
data_threadn.start()

#Thread data camera real-time reaper
camera_thread = threading.Thread(target=show_camera, daemon=True)
camera_thread.start()

#Menjalankan aplikasi
root.mainloop()
