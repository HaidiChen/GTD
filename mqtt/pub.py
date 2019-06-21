import paho.mqtt.client as mqtt

broker_url = '192.168.72.133'
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)

client.publish('text', 'hello, there! Sent an image.', 1, False)

with open('cat.jpg', 'rb') as f:
    filepayload = f.read()
    filebyte = bytearray(filepayload)

    client.publish('image', filebyte, 1, False)
