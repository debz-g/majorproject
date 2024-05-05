import serial

port = '/dev/ttyUSB0'  # Change this to match your Raspberry Pi's serial port
baud_rate = 9600

ser = serial.Serial(port, baud_rate)

input_value = f"<11-1 | 10-2>"

print(input_value)

encoded=input_value.encode()

# Write data to serial port
ser.write(encoded)
