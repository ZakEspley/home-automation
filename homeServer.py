from flask import Flask, render_template, request, redirect, url_for
import paho


app = Flask(__name__)

household_objects = [
    {"name": "Bedroom Lights",
    "description": "Turn on/off lights",
    'imgPath':"/static/imgs/lightbulb100.png",
    "commands": ["On", "Off"],
    "deviceID":"z-lights"},
    {"name":"House Fan",
    "description": "Turn on/off fan",
    "imgPath":"/static/imgs/fan.png",
    "commands": ["On", "Off"],
    "deviceID":"h-fan"}
]

@app.route('/')
def index():
    return render_template("index.html", household_objects=household_objects)

@app.route('/device/<deviceID>', methods=['POST'])
def executeCommand(deviceID):
    if request.method == 'POST':
        print(deviceID, request.values)
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)