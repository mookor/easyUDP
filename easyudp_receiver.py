"""
easyudp_receiver module provides the UDPReceiver class for handling UDP communication.

Classes:
    UDPReceiver: A class for creating a UDP receiver with easy UDP communication.

Usage:
    from easyudp_receiver import UDPReceiver

    # Create UDP receiver instance
    udp_receiver = UDPReceiver(host='localhost', port=12345, timeout=5.0)

    # receive data
    while True:
        received_data = udp_receiver.receive()
        print(received_data)

Author: [Andrey Mazko] https://github.com/mookor
"""

from easyudp import EasyUDP
import pickle
from exceptions import *
from typing import Union
from numpy import ndarray


class UDPReceiver(EasyUDP):
    def __init__(self, host: str, port: int, timeout: float) -> None:
        """
        Initialize a UDPReceiver instance.

        Args:
            host (str): The host address for the socket connection.
            port (int): The port number for the socket connection.
            timeout (float): The timeout value for the socket connection.

        """
        super().__init__()
        self.host = host
        self.port = port
        self.socket.bind((self.host, self.port))
        self.socket.settimeout(timeout)

    def send(self):
        """
        Raise UDPSendException when the UDP Client cannot send.
        """
        raise UDPSendException("UDP Client cannot send")

    def __receive_fragments(self) -> Union[ndarray, str, int]:
        """
        Receive fragments from a socket and concatenate them into a single data array.

        Returns:
            Union[ndarray, str, int]: The assembled array if data is received, otherwise returns None.
        """
        received_data = b""
        received_flag = False
        while True:
            try:
                fragment, _ = self.socket.recvfrom(1024)
                received_data += fragment
                received_flag = True
            except:
                break
        if received_flag:
            array = pickle.loads(received_data)
            return array

    def receive(self) -> Union[ndarray, str, int]:
        """
        Receive data from the socket.

        Returns:
            Union[ndarray, str, int, None]: The assembled array if data is received, otherwise returns None.
        """
        return self.__receive_fragments()
