from flask import Flask, request, jsonify
import serial
import time

app = Flask(__name__, template_folder='templates')

# Define the serial port and baud rate
port = '/dev/ttyUSB0'  # Change this to match your Raspberry Pi's serial port
baud_rate = 9600

@app.route('/home', methods=['GET'])
def get():
    return jsonify(response)

# Initialize serial connection
ser = serial.Serial(port, baud_rate)


@app.route('/', methods=['GET'])
def query_records():
    tray = request.args.get('tray')
    print(tray)

    # Construct input in the format <8-1 | 10-2>
    input_value = f"<{tray}-1 | 10-2>"

    # Write data to serial port
    ser.write(input_value.encode())

    res = {
        'Tray' : tray,
        'Success': True
    }
    return jsonify(res)

response = {
    'Success' : 'True'
}


if __name__ == '__main__':
   app.run(port= 5000,debug=True)
