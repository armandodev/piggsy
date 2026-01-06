from models.transaction import Transaction
from utils.input_reader import InputReader


class TransactionService:
    def __init__(self) -> None:
        self.__obi = InputReader()

    def __read_transaction_data(self) -> Transaction:
        """Private method to read transaction data and return a Transaction object."""
        # TODO: Implement the period selection logic
        financial_period_id = ""  # Placeholder for period ID selection
        obt = Transaction(
            financial_period_id=financial_period_id,
            title=self.__obi.string("Título de la transacción"),
            description=self.__obi.string("Descripción de la transacción"),
        )
        return obt

    def register_transaction(self) -> None:
        """Method to register a new transaction."""
        # TODO: Validate and register all the data for the transaction out of the transaction model
        new_transaction = self.__read_transaction_data()  # pyright: ignore[reportUnusedVariable]  # noqa: F841
        # TODO: Save the new transaction to the data store
