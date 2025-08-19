from typing import List, Optional

from app.schemas.schema import Number
from app.logs.setup_logger import LoggerManager, LOGGER


class ChallengeEngine:
    """
    Engine responsible for executing mathematical operations on a list of operands.

    This class provides methods for summing, subtracting, multiplying, and dividing
    numeric operands, along with logging the computation steps.

    Attributes:
        logger (LoggerManager): Logger instance for recording debug information and errors.
    """

    def __init__(self, logger: Optional[LoggerManager] = None,):
        self.logger = logger or LOGGER

    def sum_operands(self, operands: List[Number]) -> float:
        """
        Calculates the sum of all operands.

        Args:
            operands (List[Number]): A list of numeric operands to be summed.

        Returns:
            float: The sum of the operands.
        """
        self.logger.log_debug(f"[engine] Summing: {operands}")
        return sum(operands)

    def subtract_operands(self, operands: List[Number]) -> float:
        """
        Subtracts all subsequent operands from the first operand.

        Args:
            operands (List[Number]): A list of numeric operands. The first value is
            the initial value, and each subsequent value is subtracted from it.

        Returns:
            float: The result of the subtraction.
        """
        self.logger.log_debug(f"[engine] Subtracting: {operands}")
        result = operands[0]
        for value in operands[1:]:
            result -= value
        return result

    def multiply_operands(self, operands: List[Number]) -> float:
        """
        Multiplies all operands together.

        Args:
            operands (List[Number]): A list of numeric operands to be multiplied.

        Returns:
            float: The product of all operands.
        """
        self.logger.log_debug(f"[engine] Multiplying: {operands}")
        result = 1.0
        for value in operands:
            result *= value
        return result

    def divide_operands(self, operands: List[Number]) -> float:
        """
        Divides the first operand by each of the subsequent operands in order.

        Args:
            operands (List[Number]): A list of numeric operands. The first value is divided by each of the subsequent values.

        Returns:
            float: The result of the division.

        Raises:
            ValueError: If any of the subsequent operands is zero.
        """
        self.logger.log_debug(f"[engine] Dividing: {operands}")
        result = operands[0]
        for value in operands[1:]:
            if value == 0:
                raise ValueError("Division by zero is not allowed.")
            result /= value
        return result
