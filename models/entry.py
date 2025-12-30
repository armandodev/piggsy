from models.base import Base


class Entry(Base):
    def __init__(
        self,
        financial_period_id: str,
        account_id: str,
        transaction_id: str,
        debit: float,
        credit: float,
        id: str | None = None,
    ) -> None:
        super().__init__(id)
        self.__financial_period_id: str = financial_period_id
        self.__account_id: str = account_id
        self.__transaction_id: str = transaction_id
        self.__debit: float = debit
        self.__credit: float = credit

    @property
    def financial_period_id(self) -> str:
        """ID of the associated financial period"""
        return self.__financial_period_id

    @property
    def account_id(self) -> str:
        """ID of the associated account"""
        return self.__account_id

    @property
    def transaction_id(self) -> str:
        """ID of the associated transaction"""
        return self.__transaction_id

    @property
    def debit(self) -> float:
        """Debit amount for the entry"""
        return self.__debit

    @property
    def credit(self) -> float:
        """Credit amount for the entry"""
        return self.__credit
