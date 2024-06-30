import cv2
import numpy as np
import smtplib
from email.message import EmailMessage
import serial
import time

def send_email(video_path):
    msg = EmailMessage()
    msg['Subject'] = 'Spaghetti Problem Detected in 3D Printing'
    msg['From'] = 'khalil.mekki@insat.ucar.tn'
    msg['To'] = 'maram.mastouri@insat.ucar.tn'
    msg.set_content('A spaghetti problem has been detected. Please find the attached video of the incident.')

    with open(video_path, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='video', subtype='mp4', filename=file_name)

    with smtplib.SMTP_SSL('smtp.example.com', 465) as smtp:
        smtp.login('khalil.mekki@insat.ucar.tn', 'maaloul10')
        smtp.send_message(msg)

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use appropriate camera index
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Flags
problem_detected = False
start_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Predict using the trained model
   

# Define serial port and baud rate
serial_port = '/dev/ttyUSB0'  # Adjust for your operating system and port
baud_rate = 115200  # Adjust according to your printer's baud rate

# Open serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Function to send G-code to printer
def send_gcode(gcode):
    ser.write((gcode + '\n').encode())
    response = ser.readline().decode().strip()
    print(f'Sent: {gcode}, Response: {response}')

try:
    # Connect and initialize
    ser.open()

 # Check if the model detected a spaghetti problem
    if len(results[0].boxes) > 0 and not problem_detected:
        print("Spaghetti problem detected!")
        problem_detected = True
        start_time = time.time()

    if problem_detected:
        # Record video for 10 seconds after problem detection
        if time.time() - start_time <= 10:
            out.write(frame)# Define serial port and baud rate
        send_gcode('M112')

    time.sleep(2)  # Wait for 2 seconds

finally:
    # Close serial connection
    ser.close()
    
problem_detected = False
out.release()
            

