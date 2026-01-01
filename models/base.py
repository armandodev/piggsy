import datetime
import uuid


class Base:
    def __init__(self, id: str | None = None) -> None:
        date = datetime.datetime.now()
        self.__id: str = uuid.uuid7().hex if not id else id
        self.__created_at: datetime.datetime = date
        self.__updated_at: datetime.datetime = date

    @property
    def id(self) -> str:
        """Unique identifier"""
        return self.__id

    @property
    def created_at(self) -> datetime.datetime:
        """Date and time of creation"""
        return self.__created_at

    @property
    def updated_at(self) -> datetime.datetime:
        """Date and time of the last update"""
        return self.__updated_at

    def update(self) -> None:
        date = datetime.datetime.now()
        self.__updated_at = date
