import datetime

from models.financial_period import FinancialPeriod
from utils.input_reader import InputReader


class FinancialPeriodService:
    def __init__(self) -> None:
        self.__obi = InputReader()

    def __read_financial_period_data(
        self, previous_period: FinancialPeriod | None = None
    ) -> FinancialPeriod:
        """Private method to read financial period data and return a FinancialPeriod object."""
        if previous_period:
            start_date = previous_period.end_date + datetime.timedelta(days=1)
            financial_period_duration = previous_period.financial_period_duration
        else:
            start_date = None
            financial_period_duration = self.__obi.integer(
                "Duración del período financiero en meses"
            )
        obf = FinancialPeriod(
            start_date=start_date,
            financial_period_duration=financial_period_duration,
        )
        return obf

    def register_financial_period(
        self, previous_period: FinancialPeriod | None = None
    ) -> None:
        """Method to end a financial period if a previous one exists and create a new one, if a previous one does not exist, start the first financial period."""
        if previous_period and previous_period.status:
            raise Exception("El período financiero no ha finalizado.")
        new_period = self.__read_financial_period_data(previous_period=previous_period)  # pyright: ignore[reportUnusedVariable]  # noqa: F841
        # TODO: Save the new financial period to the data store
