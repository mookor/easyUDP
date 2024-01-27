"""
easyudp module provides the EasyUDP abstract class for handling UDP communication.

Classes:
    EasyUDP: An abstract class for creating UDP communication.

"""

import socket
from abc import ABC, abstractmethod


class EasyUDP(ABC):
    def __init__(self) -> None:
        """
        Initialize a new EasyUDP instance.

        """

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    @abstractmethod
    def send(self, message) -> None:
        """
        Abstract method for sending data through UDP.

        Raises:
            NotImplementedError: This method must be implemented in the derived class.

        """

        raise NotImplementedError

    @abstractmethod
    def receive(self):
        """
        Abstract method for receiving data through UDP.


        Raises:
            NotImplementedError: This method must be implemented in the derived class.

        """
        raise NotImplementedError
