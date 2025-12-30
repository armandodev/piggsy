from models.base import Base
from models.credit_metadata import CreditMetadata


class Account(Base):
    def __init__(
        self,
        financial_period_id: str,
        code: str,
        name: str,
        description: str,
        is_debtor: bool,
        id: str | None = None,
        initial_balance: float = 0.0,
        metadata: None | CreditMetadata = None,
    ) -> None:
        super().__init__(id)
        self.__financial_period_id: str = financial_period_id
        self.__code: str = code
        self.__name: str = name
        self.__description: str = description
        self.__is_debtor: bool = is_debtor
        self.__initial_balance: float = initial_balance
        self.__debit: float = 0.0
        self.__credit: float = 0.0
        self.__balance: float = initial_balance
        self.__metadata: None | CreditMetadata = metadata

    @property
    def financial_period_id(self) -> str:
        """ID of the associated financial period"""
        return self.__financial_period_id

    @property
    def code(self) -> str:
        """Account code"""
        return self.__code

    @property
    def name(self) -> str:
        """Account name"""
        return self.__name

    @property
    def description(self) -> str:
        """Account description"""
        return self.__description

    @property
    def is_debtor(self) -> bool:
        """Indicates if the account is a debtor nature account or a creditor nature account"""
        return self.__is_debtor

    @property
    def initial_balance(self) -> float:
        """Initial balance of the account"""
        return self.__initial_balance

    @property
    def debit(self) -> float:
        """Total debit amount"""
        return self.__debit

    @property
    def credit(self) -> float:
        """Total credit amount"""
        return self.__credit

    @property
    def balance(self) -> float:
        """Current balance of the account"""
        return self.__balance

    @property
    def metadata(self) -> None | CreditMetadata:
        """Metadata associated with the account, if any"""
        return self.__metadata
