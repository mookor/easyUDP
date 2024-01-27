# Easy UDP

Easy UDP is a Python package that simplifies UDP communication. It provides convenient classes for UDP client and server implementations.

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
udp_sender = UDPSender(host="localhost", port=12345, send_pause=0.1)

# Sending data
print("Sending: [1, 2, 3]")
udp_sender.send(np.array([1, 2, 3]))

print("Sending: Hello, World!")
udp_sender.send(np.array("Hello, World!"))

```

### UDP Receiver
```python
from easy_udp import UDPReceiver

# Create UDP Receiver instance
udp_receiver = UDPReceiver(host="localhost", port=12345, timeout=0.1)

# Receiving  data
while True:
    received_data = udp_receiver.receive()
    if received_data is not None:
        print(received_data)
```
