from fastapi import APIRouter, status

from app.routes.challenge.dtos.dto import ChallengeRequestDTO, ChallengeResponseDTO
from app.routes.challenge.controllers.controller import ChallengeController

router = APIRouter()


@router.post(
    "/challenge",
    summary="Perform a mathematical operation",
    description="Executes a specified mathematical operation ('sum', 'subtract', 'multiply', 'divide') on the provided operands.",
    response_model=ChallengeResponseDTO,
    status_code=status.HTTP_200_OK,
)
def challenge(request: ChallengeRequestDTO):
    """
    Handles the POST request to perform a mathematical operation on provided operands.

    This endpoint accepts a JSON body specifying the operation type and operands,
    then returns the result of the operation.

    Args:
        request (ChallengeRequestDTO): The request body containing the operation type and operands.

    Returns:
        ChallengeResponseDTO: The result of the performed operation.

    Raises:
        HTTPException: If the request is invalid or an error occurs during processing.
    """
    controller = ChallengeController()
    return controller.process(request)
