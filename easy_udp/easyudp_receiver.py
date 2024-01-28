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

from easy_udp import EasyUDP
from easy_udp import UDPSendException
import pickle
from typing import Union
from numpy import ndarray
import socket
import errno
import numpy as np


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
        self.socket.setblocking(False)

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
        received_flag = False
        received_data = []
        dtype = None
        while True:
            try:
                fragment, _ = self.socket.recvfrom(4500)
                if b"Meta::" in fragment:
                    dtype = fragment.replace(b"Meta::", b"")
                    break

                received_data.append(fragment)
                received_flag = True

            except socket.error as e:
                if e.errno == errno.EWOULDBLOCK or e.errno == errno.EAGAIN:
                    continue
                else:
                    break

        if received_flag:
            if dtype == b"ndarray":
                array = np.concatenate(
                    [pickle.loads(fragment) for fragment in received_data]
                )
                return array

            elif dtype == b"str":
                return "".join([pickle.loads(fragment) for fragment in received_data])

            elif dtype == b"int":
                return pickle.loads(received_data[0])

    def receive(self) -> Union[ndarray, str, int]:
        """
        Receive data from the socket.

        Returns:
            Union[ndarray, str, int, None]: The assembled array if data is received, otherwise returns None.
        """
        return self.__receive_fragments()
