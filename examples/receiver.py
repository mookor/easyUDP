from easy_udp import UDPReceiver
import numpy as np
import time

# Create UDP receiver instance
udp_receiver = UDPReceiver(host="localhost", port=12345)

# receive data
while True:
    t = time.time()
    received_data = udp_receiver.receive()
    if received_data is not None:
        if isinstance(received_data, np.ndarray):
            received_data = received_data.reshape((1280, 720, 3))
            print("Received: img", received_data)

        if isinstance(received_data, str):
            print("Received: str", received_data)

        if isinstance(received_data, int):
            print("Received: int", received_data)
        print("Time: ", time.time() - t)
