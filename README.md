# MQTT
MQTT stands for Message Queuing Telemetry Transport. It's a lightweight messaging protocol designed for constrained devices and low-bandwidth, high-latency, or unreliable networks. MQTT is commonly used for IoT (Internet of Things) applications where devices need to communicate with each other or with a central server.

### 0. Setting up and running your own MQTT broker locally or on a cloud server.
    ### . broker on a cloud server
        In my code, I am connecting to the EMQX broker hosted at "broker.emqx.io" on port 1883. This assumes that there's a public MQTT broker running at that address.
    ### . Installing broker locall
        It communicates between MQTT clients, providing message routing, delivery, and management features. I chose mosquitto broker.
        ```bash
        sudo apt update
        sudo apt install mosquitto
        sudo apt install mosquitto-clients
        sudo systemctl start mosquitto
        sudo systemctl enable mosquitto

### 1. set up and activate a virtual environment for your Python project:
    Navigate to the directory where you want to create your Python project, then create a virtual environment using virtualenv. You can name your virtual environment directory whatever you like; commonly it's named venv.
    
    Step 1: Install Virtualenv: pip install virtualenv
    Step 2: Create a Virtual Environment: virtualenv venv
    Step 3: Activate the Virtual Environment/On macOS and Linux:/: source venv/bin/activate

### 2. Installing paho-mqtt
    First you need to install paho-mqtt library, to implement mqtt communication.
    `pip install paho-mqtt==1.5.1`

```

### 3. Running the code
    Navigate to the directory where you want to create your Python project and run the code on many terminals with `python3 chat.py` enter your name and send messages to each other.
