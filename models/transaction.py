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
