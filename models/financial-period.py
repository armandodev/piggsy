import datetime

from dateutil.relativedelta import relativedelta

from models.base import Base


class FinancialPeriod(Base):
    def __init__(
        self,
        id: str | None = None,
        start_date: datetime.date | None = None,
        financial_period_duration: int = 1,  # Meses
    ) -> None:
        super().__init__(id)
        current_date = datetime.date.today()
        self.__start_date: datetime.date = (
            current_date if not start_date else start_date
        )
        self.__financial_period_duration: int = financial_period_duration
        self.__end_date: datetime.date = self.__calculate_end_date()

    def __calculate_end_date(self) -> datetime.date:
        return (
            self.__start_date + relativedelta(months=self.__financial_period_duration)
        ) - datetime.timedelta(days=1)

    @property
    def start_date(self) -> datetime.date:
        """Start date of the financial period"""
        return self.__start_date

    @property
    def financial_period_duration(self) -> int:
        """Duration of the financial period in days"""
        return self.__financial_period_duration

    @financial_period_duration.setter
    def financial_period_duration(self, value: int) -> None:
        if not self.status:
            raise Exception("No se puede modificar un período financiero inactivo.")
        if value <= 0:
            raise ValueError(
                "La duración del período financiero debe ser un número positivo."
            )
        self.__financial_period_duration = value
        self.__end_date = self.__calculate_end_date()

    @property
    def end_date(self) -> datetime.date:
        """End date of the financial period"""
        return self.__end_date

    @property
    def status(self) -> bool:
        """Status of the financial period (active: True/inactive: False)"""
        current_date = datetime.date.today()
        return self.__end_date >= current_date
