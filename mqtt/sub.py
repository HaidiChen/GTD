import paho.mqtt.client as mqtt

broker_url = "192.168.72.133"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print('connected with result code', rc)

#def on_message_text(client, userdata, message):
#    print('text message received: ', message.payload)

def on_message(client, userdata, message):
    if message.topic == 'text':
        print('text received:', message.payload.decode())
        return

    with open('test.jpg', 'wb') as f:
        f.write(message.payload)
    print('image received')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_url, broker_port)

client.subscribe('text', qos=1)
client.subscribe('image', qos=1)

client.loop_forever()
