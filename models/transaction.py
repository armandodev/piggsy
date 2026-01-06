from models.base import Base


class Transaction(Base):
    def __init__(
        self,
        financial_period_id: str,
        title: str,
        description: str,
        id: str | None = None,
    ) -> None:
        super().__init__(id)
        self.__financial_period_id: str = financial_period_id
        self.__title: str = title
        self.__description: str = description

    @property
    def financial_period_id(self) -> str:
        """ID of the associated financial period"""
        return self.__financial_period_id

    @property
    def title(self) -> str:
        """Title of the transaction"""
        return self.__title

    @property
    def description(self) -> str:
        """Description of the transaction"""
        return self.__description

    @title.setter
    def title(self, value: str) -> None:
        self.__title = value

    @description.setter
    def description(self, value: str) -> None:
        self.__description = value
