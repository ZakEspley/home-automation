import paho.mqtt.client as mqtt
run = True

def on_connect(client, userdata, flags, rc):
    print()
    print("Connected with result code " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def toggleLight(client, last_state):
    if last_state:
        client.publish("homie/z-room-light-1/light/on/set", 'false')
    else:
        client.publish("homie/z-room-light-1/light/on/set", 'true')
    return not last_state

def turn_off_light(client):
    client.publish("homie/z-room-light-1/light/on/set", 'false')
    return False

def turn_on_light(client):
    client.publish("homie/z-room-light-1/light/on/set", 'true')
    return True

def ledOn(client):
    for i in range(30):
        topic = "homie/z-room-light-1/led/pixel_" + str(i+1) +"/set"
        client.publish(topic, "255255255255")

def ledOff(client):
    for i in range(30):
        topic = "homie/z-room-light-1/led/pixel_" + str(i+1) +"/set"
        client.publish(topic, "000000000000")

def dc(client):
    client.loop_stop()
    client.disconnect()
    global run
    run = False


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect('192.168.1.106', 1883, 60)
mqttc.subscribe("homie/z-room-light-1/light/on")
mqttc.subscribe("homie/z-room-light-1/led/on")
mqttc.subscribe("homie/z-room-light-1/led/$name")
mqttc.loop_start()

last_state = True

while run:
    print()
    response = input("What would you like to do?   ")
    print('')
    if response == 'toggle':
        last_state = toggleLight(mqttc, last_state)
    elif response == 'dc':
        dc(mqttc)
    elif response == 'on':
        last_state = turn_on_light(mqttc)
    elif response == 'off':
        last_state = turn_off_light(mqttc)
    elif response == "led-on":
        ledOn(mqttc)
    elif response == "led-off":
        ledOff(mqttc)
    else:
        print("Sorry, I didn't understand that. Please try again. \r\n")