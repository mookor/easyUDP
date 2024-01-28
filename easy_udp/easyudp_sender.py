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
from numpy import ndarray
import pickle
from typing import Union


class UDPSender(EasyUDP):
    def __init__(self, host: str, port: int) -> None:
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

    def _send_metadata(self, message_type: Union[ndarray, str, int]) -> None:
        """
        Sends metadata based on the message type to the specified host and port.

        Args:
            message_type (Union[ndarray, str, int]): The type of the message to be sent.

        """
        if message_type == ndarray:
            self.socket.sendto(b"Meta::ndarray", (self.host, self.port))
        elif message_type == str:
            self.socket.sendto(b"Meta::str", (self.host, self.port))
        elif message_type == int:
            self.socket.sendto(b"Meta::int", (self.host, self.port))

    def _send_ndarray(self, message: ndarray) -> None:
        """
        Send a NumPy array as fragments.

        Args:
            message (ndarray): The NumPy array to be sent.

        """

        message = message.flatten()
        length = len(message)
        byte_size = message[0].nbytes
        self._send_fragments(message, length, byte_size, ndarray)

    def _send_integer(self, message: int) -> None:
        """
        Send an integer as a serialized byte stream.

        Args:
            message (int): The integer to be sent.

        """

        bit_length = message.bit_length()
        byte_size = (bit_length + 7) // 8
        number_bytes = pickle.dumps(message)
        if byte_size > 4096:
            raise UDPSendException("UDP sender only supports integers up to 4096 bytes")

        self.socket.sendto(number_bytes, (self.host, self.port))
        self._send_metadata(int)

    def _send_fragments(self, message, length, byte_size, dtype) -> None:
        """
        Send fragments of a message.

        Args:
            message: The message to be sent.
            length: The length of the message.

        """

        fragment_size = 4096 // byte_size
        for i in range(0, length, fragment_size):
            fragment = message[i : i + fragment_size]
            pickled_fragment = pickle.dumps(fragment)
            self.socket.sendto(pickled_fragment, (self.host, self.port))

        self._send_metadata(dtype)

    def send(self, message) -> None:
        """
        Send a message through UDP.

        Args:
            message: The message to be sent.

        Raises:
            UDPSendException: If the message type is not supported.

        """

        if isinstance(message, ndarray):
            self._send_ndarray(message)

        elif isinstance(message, str):
            self._send_fragments(message, len(message), 1, str)

        elif isinstance(message, int):
            self._send_integer(message)

        else:
            raise UDPSendException(
                "UDP sender only supports numpy arrays, strings, and integers"
            )

    def receive(self):
        """
        Receive method not supported for UDPSender.

        Raises:
            UDPTypeException: If receive method is called on UDPSender.

        """

        raise UDPTypeException(
            "UDP sender does not support receiving messages, use UDPClient instead"
        )
