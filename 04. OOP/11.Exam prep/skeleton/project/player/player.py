from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository


class Player(ABC):

    @abstractmethod
    def __init__(self, username: str, health: int):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Player's username cannot be an empty string.")
        self.__username = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero")
        self.__health = value

    @property
    def is_dead(self):
        if self.health <= 0:
            return True
        return False

    @staticmethod
    def take_damage(damage_points):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        Player.health -= damage_points
