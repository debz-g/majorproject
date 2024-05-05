from flask import Flask, request
from flask import jsonify


app = Flask(_name_, template_folder='templates')
@app.route('/home', methods=['GET'])
def get():
    return response;


@app.route('/', methods=['GET'])
def query_records():
    tray = request.args.get('tray')
    print(tray)
    res = {
        'Tray' : tray
    }
    return jsonify(res)

response = {
    'Success' : 'True'
}


if _name_ == '_main_':
   app.run(port= 5000,debug=True)
