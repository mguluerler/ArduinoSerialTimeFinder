import serial
import time
import math

class ArduinoSerialTimeFinder:
    def __init__(self, arduino=None, baudrate=None, port=None, dt=0.00001, limit=None):
        if arduino != "None":
            self.arduino = arduino
        else:
            self.arduino = serial.Serial(baudrate=baudrate, timeout=None, port=port)
        self.dt = dt

        self.time_com = 0

    def test(self, len_serial_data, limit=-1):
        serial_data = ""
        is_dataavailable = False
        while limit != 0:
            while self.arduino.in_waiting > 0:
                serial_data += self.arduino.read().decode("ascii")
                is_dataavailable = True
            if is_dataavailable == True:
                print("\rNew Time: {}".format(self.time_com), len(serial_data), end="", sep=" ")
                if type(len_serial_data) == int:
                    if len_serial_data > len(serial_data):
                        self.time_com += self.dt
                    elif len_serial_data < len(serial_data):
                        self.time_com -= self.dt
                    else:
                        print("\rCalculated Time:", self.time_com, len_serial_data, end="", sep=" ")
                        limit -= 1
                elif type(len_serial_data) == list:
                    if max(len_serial_data) < len(serial_data):
                        self.time_com -= self.dt
                    elif min(len_serial_data) > len(serial_data):
                        self.time_com += self.dt
                    else:
                        print("\rCalculated Time:", self.time_com, len_serial_data, end="", sep=" ")
                        limit -= 1
                if self.time_com < 0:
                    self.time_com = self.time_com * -1
            is_dataavailable = False
            serial_data = ""
            try:
                time.sleep(self.time_com)
            except:
                time.sleep(0)

if __name__ == "__main__":
    x = ArduinoSerialTimeFinder(port="COM6", baudrate=115200)
    x.test()