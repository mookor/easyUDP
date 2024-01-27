"""
easyudp_sender module provides the UDPSender class for handling UDP sender communication.

Classes:
    UDPSender: A class for creating a UDP sender with easy UDP communication.

Usage:
    from easyudp_sender import UDPSender

    # Create UDP sender instance
    udp_sender = UDPSender(host='localhost', port=12345, send_pause=0.1)

    # Sending data
    udp_sender.send(np.array([1, 2, 3]))


Author: [Andrey Mazko] https://github.com/mookor
"""

from easy_udp import EasyUDP
from easy_udp import UDPSendException, UDPTypeException
import numpy as np
import pickle
import time


class UDPSender(EasyUDP):
    def __init__(self, host: str, port: int, send_pause: float = 0.1) -> None:
        """
        Initialize a UDPSender instance.

        Args:
            host (str): The host address for the socket connection.
            port (int): The port number for the socket connection.
            send_pause (float): The pause duration between sending messages.

        """

        super().__init__()
        self.host = host
        self.port = port
        self.send_pause = send_pause

    def __send_ndarray(self, message: np.ndarray) -> None:
        """
        Send a NumPy array as fragments.

        Args:
            message (np.ndarray): The NumPy array to be sent.

        """

        message = message.flatten()
        length = len(message)
        self.__send_fragments(message, length)

    def __send_integer(self, message: int) -> None:
        """
        Send an integer as a serialized byte stream.

        Args:
            message (int): The integer to be sent.

        """

        bit_length = message.bit_length()
        byte_size = (bit_length + 7) // 8
        number_bytes = pickle.dumps(message)
        if byte_size > 1024:
            raise UDPSendException("UDP sender only supports integers up to 1024 bytes")

        self.socket.sendto(number_bytes, (self.host, self.port))

    def __send_fragments(self, message, length) -> None:
        """
        Send fragments of a message.

        Args:
            message: The message to be sent.
            length: The length of the message.

        """

        fragment_size = 1024
        for i in range(0, length, fragment_size):
            fragment = message[i : i + fragment_size]
            pickled_fragment = pickle.dumps(fragment)
            self.socket.sendto(pickled_fragment, (self.host, self.port))

    def send(self, message) -> None:
        """
        Send a message through UDP.

        Args:
            message: The message to be sent.

        Raises:
            UDPSendException: If the message type is not supported.

        """

        if isinstance(message, np.ndarray):
            self.__send_ndarray(message)

        elif isinstance(message, str):
            self.__send_fragments(message, len(message))

        elif isinstance(message, int):
            self.__send_integer(message)

        else:
            raise UDPSendException(
                "UDP sender only supports numpy arrays, strings, and integers"
            )
        time.sleep(self.send_pause)

    def receive(self):
        """
        Receive method not supported for UDPSender.

        Raises:
            UDPTypeException: If receive method is called on UDPSender.

        """

        raise UDPTypeException(
            "UDP sender does not support receiving messages, use UDPClient instead"
        )
