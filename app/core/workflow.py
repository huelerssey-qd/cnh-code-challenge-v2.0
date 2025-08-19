from typing import Any, Dict, Optional

from app.logs.setup_logger import LoggerManager, LOGGER
from app.routes.challenge.dtos.dto import ChallengeRequestDTO
from app.core.engine import ChallengeEngine
from app.core.validator import ChallengeValidator


class ChallengeWorkflow:
    """
    Workflow class responsible for orchestrating validation and execution of challenge operations.

    This class manages the end-to-end process of validating input, selecting the correct
    mathematical operation, invoking the appropriate engine method, and handling results and errors.

    Attributes:
        engine (ChallengeEngine): Instance responsible for performing mathematical operations.
        validator (ChallengeValidator): Instance responsible for validating operations and operands.
        logger (LoggerManager): Logger instance for recording workflow steps and errors.
    """

    def __init__(
        self,
        engine: Optional[ChallengeEngine] = None,
        validator: Optional[ChallengeValidator] = None,
        logger: Optional[LoggerManager] = None,
    ) -> None:
        self.engine = engine or ChallengeEngine()
        self.validator = validator or ChallengeValidator()
        self.logger = logger or LOGGER

    def process(self, request: ChallengeRequestDTO) -> Dict[str, Any]:
        """
        Processes a challenge request by validating input and executing the specified operation.

        Handles success and error cases, including logging relevant events.

        Args:
            request (ChallengeRequestDTO): The incoming challenge request data.

        Returns:
            Dict[str, Any]: Dictionary containing success status, message, and data (result or error details).
        """
        self.logger.log_info("[workflow] processing challenge operation")
        self.logger.log_debug(f"[workflow] request data: {request.model_dump()}")

        operation = request.operation
        operands = request.operands

        if not self.validator.validate(operation, operands):
            self.logger.log_info("[workflow] invalid operation or operands")
            return {
                "success": False,
                "message": "Invalid operation or operands.",
                "data": None,
            }
        try:
            if operation == "sum":
                result = self.engine.sum_operands(operands)
            elif operation == "subtract":
                result = self.engine.subtract_operands(operands)
            elif operation == "multiply":
                result = self.engine.multiply_operands(operands)
            elif operation == "divide":
                result = self.engine.divide_operands(operands)

            self.logger.log_info("[workflow] operation successful")
            self.logger.log_debug(f"[workflow] operation result: {result}")

            return {
                "success": True,
                "message": "Operation completed successfully.",
                "data": {"result": result},
            }

        except Exception as e:
            self.logger.log_error(f"[workflow] error during operation: {e}")
            return {
                "success": False,
                "message": "Error during operation execution.",
                "data": {"error": str(e)},
            }
