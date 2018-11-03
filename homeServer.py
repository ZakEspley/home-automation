from flask import Flask, render_template, request, redirect, url_for
import paho.mqtt.client as mqtt


app = Flask(__name__)
mc = mqtt.Client()

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

mainTopic = "homie"


@app.route('/')
def index():
    return render_template("index.html", household_objects=household_objects)

@app.route('/device/<deviceID>', methods=['POST'])
def executeCommand(deviceID):
    if request.method == 'POST':
        print(deviceID, request.values)
        return redirect(url_for("index"))

def join(*args):
    topic = ""
    for arg in args:
        topic += str(arg) + "/"
    
    return topic[:-1]

def on_connect(client, userdata, flags, rc):
    print()
    print("Connected with result code " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mc.on_connect = on_connect
mc.on_message = on_message

if __name__ == "__main__":
    # app.run(debug=True)
    mc.connect('192.168.1.106', 1883, 60)
    mc.subscribe("#")
    mc.loop_start()
    while True:
        pass