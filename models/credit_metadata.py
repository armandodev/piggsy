import datetime


class CreditMetadata:
    def __init__(
        self,
        payment_date: datetime.date,
        cutoff_date: datetime.date,
        limit_amount: float,
        available_amount: float,
        minimum_payment_amount: float,
        payment_amount: float,
        is_paid: bool = False,
    ) -> None:
        self.__payment_date: datetime.date = payment_date
        self.__cutoff_date: datetime.date = cutoff_date
        self.__limit_amount: float = limit_amount
        self.__available_amount: float = available_amount
        self.__minimum_payment_amount: float = minimum_payment_amount
        self.__payment_amount: float = payment_amount
        self.__is_paid: bool = is_paid

    @property
    def payment_date(self) -> datetime.date:
        """Date when the payment is due"""
        return self.__payment_date

    @property
    def cutoff_date(self) -> datetime.date:
        """Date when the statement is cut off"""
        return self.__cutoff_date

    @property
    def limit_amount(self) -> float:
        """Credit limit amount"""
        return self.__limit_amount

    @property
    def available_amount(self) -> float:
        """Available credit amount"""
        return self.__available_amount

    @property
    def minimum_payment_amount(self) -> float:
        """Minimum amount required to be paid"""
        return self.__minimum_payment_amount

    @property
    def payment_amount(self) -> float:
        """Amount required to be paid"""
        return self.__payment_amount

    @property
    def is_paid(self) -> bool:
        """Indicates whether the payment has been made"""
        return self.__is_paid
