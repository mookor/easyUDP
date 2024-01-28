from easy_udp import UDPSender
import numpy as np
import time
# Create UDP sender instance
udp_sender = UDPSender(host="localhost", port=12345, send_pause=0.000001)

# Sending data
# print("Sending: [1, 2, 3]")
# udp_sender.send(np.array([1, 2, 3]))

# print("Sending: Hello, World!")
# udp_sender.send(np.array("Hello, World!"))


print("Sending: img-like")
udp_sender.send(np.random.randint(0, 255, (1280, 720, 3), dtype=np.uint8))
print(1280*720*3)
# t = time.time()
# for i in range(1000):
#     print(f"Sending: {i}")
#     udp_sender.send(i)
# print(f"Total time: {time.time() - t} s")