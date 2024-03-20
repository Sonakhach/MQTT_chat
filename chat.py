import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"{str(message.payload.decode('utf-8'))}")

client = mqtt.Client()
broker_address = "broker.emqx.io"
port = 1883
topic = "chat/group"
client.connect(broker_address, port, 60)
client.subscribe(topic)

client.on_message = on_message
client.loop_start()

def send_message(name, message):
    client.publish(topic, f"{name}: {message}")

user_name = input("Enter your name('exit' to quit): ")
while True:
    user_input = input("Enter your message : ")
    if user_input.lower() == "exit":
        break  
    send_message(user_name, user_input)


client.loop_stop()