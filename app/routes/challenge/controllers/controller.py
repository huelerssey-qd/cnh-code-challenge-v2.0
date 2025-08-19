from typing import Optional
from pydantic import ValidationError
from fastapi.responses import JSONResponse

from app.routes.challenge.dtos.dto import ChallengeRequestDTO, ChallengeResponseDTO
from app.routes.challenge.services.service import ChallengeService
from app.logs.setup_logger import LoggerManager, LOGGER


class ChallengeController:
    """
    Controller responsible for handling challenge requests and coordinating the service layer.

    Attributes:
        logger (LoggerManager): Logger instance for logging events, debugging, and errors.
        service (ChallengeService): Service instance responsible for business logic of the challenge.
    """

    def __init__(
        self,
        service: Optional[ChallengeService] = None,
        logger: Optional[LoggerManager] = None,
    ):
        self.logger = logger or LOGGER
        self.service = service or ChallengeService()

    def process(self, request: ChallengeRequestDTO) -> ChallengeResponseDTO:
        """
        Processes the incoming challenge request and returns the corresponding response.

        This method handles the orchestration between receiving the request,
        invoking the business logic, and handling potential exceptions.

        Args:
            request (ChallengeRequestDTO): The request data containing the operation and operands.

        Returns:
            ChallengeResponseDTO: Response containing the result of the operation or an error message.

        Raises:
            ValidationError: If request validation fails.
            Exception: For any unexpected errors during processing.
        """
        try:
            self.logger.log_info(
                f"[controller] request payload: {request.model_dump()}"
            )
            response: ChallengeResponseDTO = self.service.handle(request)
            self.logger.log_debug(f"[controller] response: {response.model_dump()}")
            status_code = 200 if response.success else 400
            self.logger.log_info(f"[controller] response sent: {response.model_dump()}")
            
            return JSONResponse(
                status_code=status_code,
                content=response.model_dump(),
            )

        except ValidationError as e:
            self.logger.log_error(f"[controller] validation error: {e.errors()}")
            dto = ChallengeResponseDTO(
                success=False,
                message="Validation failed.",
                data={"errors": e.errors()},
            )
            return JSONResponse(status_code=422, content=dto.model_dump())

        except Exception as e:
            self.logger.log_error(f"[controller] internal error: {str(e)}")
            dto = ChallengeResponseDTO(
                success=False,
                message="Internal server error.",
                data={"error": str(e)},
            )
            return JSONResponse(status_code=500, content=dto.model_dump())
