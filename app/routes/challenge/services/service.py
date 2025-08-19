from typing import Optional

from app.routes.challenge.dtos.dto import ChallengeRequestDTO, ChallengeResponseDTO
from app.core.workflow import ChallengeWorkflow
from app.logs.setup_logger import LoggerManager, LOGGER


class ChallengeService:
    """
    Service class responsible for handling challenge business logic.

    This class orchestrates the workflow execution and manages error handling and logging.

    Attributes:
        workflow (ChallengeWorkflow): The workflow instance used to process the challenge logic.
        logger (LoggerManager): Logger instance for logging service events and errors.
    """

    def __init__(
        self,
        workflow: Optional[ChallengeWorkflow] = None,
        logger: Optional[LoggerManager] = None,
    ):
        self.workflow = workflow or ChallengeWorkflow()
        self.logger = logger or LOGGER

    def handle(self, request: ChallengeRequestDTO) -> ChallengeResponseDTO:
        """
        Handles the challenge request by invoking the workflow and manages any arising errors.

        Args:
            request (ChallengeRequestDTO): The challenge request data containing operation and operands.

        Returns:
            ChallengeResponseDTO: Response DTO with the operation result or error information.

        Raises:
            ValueError: If input validation or operation fails.
            Exception: For any unexpected errors during the operation.
        """
        try:
            self.logger.log_info("[service] processing challenge request")
            self.logger.log_debug(f"[service] request data: {request.model_dump()}")
            result = self.workflow.process(request)
            self.logger.log_debug(f"[service] response: {result}")
            return ChallengeResponseDTO(**result)

        except ValueError as ve:
            self.logger.log_error(f"[service] value error: {str(ve)}")
            return ChallengeResponseDTO(
                success=False,
                message="Invalid input or operation error.",
                data={"error": str(ve)},
            )

        except Exception as e:
            self.logger.log_error(f"[service] unexpected error: {str(e)}")
            return ChallengeResponseDTO(
                success=False,
                message="Unexpected error during operation.",
                data={"error": str(e)},
            )
