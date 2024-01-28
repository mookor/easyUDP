# Easy UDP

Easy UDP is a Python package that simplifies UDP communication. It provides convenient classes for UDP Sender and Receiver implementations.

## Installation

```bash
pip install easy-udp
```

## Usage

### UDP Sender
```python
from easy_udp import UDPSender
import numpy as np

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

```

### UDP Receiver
```python
from easy_udp import UDPReceiver
import numpy as np

# Create UDP receiver instance
udp_receiver = UDPReceiver(host="localhost", port=12345)

# receive data
while True:
    received_data = udp_receiver.receive()
    if received_data is not None:
        if isinstance(received_data, np.ndarray):
            received_data = received_data.reshape((1280, 720, 3))
            print("Received: img", received_data)

        if isinstance(received_data, str):
            print("Received: str", received_data)

        if isinstance(received_data, int):
            print("Received: int", received_data)
```
