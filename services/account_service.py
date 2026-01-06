from models.account import Account
from utils.input_reader import InputReader


class AccountService:
    def __init__(self) -> None:
        self.__obi = InputReader()

    def __read_account_data(
        self, previous_period_account: Account | None = None
    ) -> Account:
        """Private method to read account data and return an Account object."""
        # TODO: Implement code validation logic
        if previous_period_account:
            code = previous_period_account.code
            name = previous_period_account.name
            description = previous_period_account.description
            is_debtor = previous_period_account.is_debtor
            initial_balance = previous_period_account.balance
        else:
            code = ""
            name = self.__obi.string("Nombre de la cuenta")
            description = self.__obi.string("Descripción de la cuenta")
            is_debtor = False
            initial_balance = self.__obi.float("Saldo inicial de la cuenta")
        # TODO: Implement debtor/creditor nature selection
        # TODO: Implement credit metadata input if applicable
        # TODO: Implement the period selection logic
        financial_period_id = ""  # Placeholder for period ID selection
        oba = Account(
            financial_period_id=financial_period_id,
            code=code,
            name=name,
            description=description,
            is_debtor=is_debtor,
            initial_balance=initial_balance,
        )
        return oba

    def register_account(self, previous_period_account: Account | None = None) -> None:
        """Method to create a new financial period account."""
        new_account = self.__read_account_data()  # pyright: ignore[reportUnusedVariable]  # noqa: F841
        # TODO: Save the new financial period to the data store
