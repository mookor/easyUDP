from easyudp_receiver import UDPReceiver

# Create UDP receiver instance
udp_receiver = UDPReceiver(host="localhost", port=12345, timeout=1.0)

# receive data
while True:
    received_data = udp_receiver.receive()
    if received_data is not None:
        print(received_data)
