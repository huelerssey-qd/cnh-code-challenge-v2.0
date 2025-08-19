from typing import List, Optional

from app.schemas.schema import Number
from app.logs.setup_logger import LoggerManager, LOGGER


class ChallengeValidator:
    """
    Validator class responsible for validating operations and operands for mathematical challenges.

    Ensures that operations are performed with valid operands, including special handling
    for division to prevent division by zero errors.

    Attributes:
        logger (LoggerManager): Logger instance for recording validation steps and errors.
    """

    def __init__(self, logger: Optional[LoggerManager] = None,):
        self.logger = logger or LOGGER

    def validate(self, operation: str, operands: List[Number]) -> bool:
        """
        Validates the operation and operands before performing the mathematical challenge.

        For division operations, ensures that no operand (except the first) is zero.

        Args:
            operation (str): The mathematical operation to validate (e.g., "divide").
            operands (List[Number]): The list of numeric operands.

        Returns:
            bool: True if the operation and operands are valid, False otherwise.
        """
        self.logger.log_debug(
            f"[validator] Validating operation '{operation}' with operands: {operands}"
        )

        if operation == "divide":
            if any(value == 0 for value in operands[1:]):
                self.logger.log_error("[validator] Division by zero detected")
                return False

        self.logger.log_debug("[validator] Validation passed")
        return True
