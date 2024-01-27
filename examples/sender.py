from easyudp_sender import UDPSender
import numpy as np

# Create UDP sender instance
udp_sender = UDPSender(host='localhost', port=12345, send_pause=1.0)

# Sending data
print("Sending: [1, 2, 3]")
udp_sender.send(np.array([1, 2, 3]))

print("Sending: Hello, World!")
udp_sender.send(np.array("Hello, World!"))
