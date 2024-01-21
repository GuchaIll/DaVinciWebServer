import serial 
import os
import time


class EstablishConnection:
    def __init__(self):
        
        os.getcwd()


        ser = serial.Serial('/dev/ttyACM6', 9600)
        ser.write('5,')

        if ser:
            print("connected")
            file = open('mapping.csv')
            while True:
                line = file.readline()
                if not line:
                    break
                ser.write(line)
                time.sleep(3)
        else:
            print("failed to connect")