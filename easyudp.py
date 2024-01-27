import socket
from abc import ABC, abstractmethod

class EasyUDP(ABC):
    def __init__(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    @abstractmethod
    def send(self, message: list) -> None:
        raise NotImplementedError

    @abstractmethod
    def receive(self) -> list:
        raise NotImplementedError
    


