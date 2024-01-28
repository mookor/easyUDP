from easy_udp import UDPSender
import numpy as np
import time

# Create UDP sender instance
udp_sender = UDPSender(host="localhost", port=12345)

# Sending data
print("Sending: 123")
udp_sender.send(123)

print("Sending: Hello, World!")
udp_sender.send("Hello, World!")

img = np.random.randint(0, 255, (1280, 720, 3), dtype=np.uint8)
print("Sending: img", img)
udp_sender.send(img)
