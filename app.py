from flask import Flask, request, jsonify
import serial
import time

app = Flask(__name__, template_folder='templates')

# Define the serial port and baud rate
port = '/dev/ttyUSB1'  # Change this to match your Raspberry Pi's serial port
baud_rate = 9600

@app.route('/home', methods=['GET'])
def get():
    return jsonify(response)

ser = serial.Serial(port, baud_rate)
try:
    # Initialize serial connection
    ser = serial.Serial(port, baud_rate)
    serial_available = True
except serial.SerialException:
    serial_available = False
    print("Serial port not detected. Starting API without serial connection.")


@app.route('/', methods=['GET'])
def query_records():
    tray = request.args.get('tray')
    print(tray)

#    if serial_available:
        # Construct input in the format <8-1 | 10-2>
    input_value = f"<11-1 | 10-2>"

        # Write data to serial port
    ser.write(input_value.encode())

    res = {
        'Input' : input_value,
        'Tray' : tray,
        'Success': True
    }
    return jsonify(res)

response = {
    'Success' : 'True'
}


if __name__ == '__main__':
   app.run(port= 5000,debug=True)
