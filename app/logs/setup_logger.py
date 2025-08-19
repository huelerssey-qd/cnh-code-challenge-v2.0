import logging
import sentry_sdk

from sentry_sdk.integrations.logging import LoggingIntegration

from app.settings.setting import get_settings, Environment


class LoggerManager:
    """
    Class for managing logging in the application.

    This class centralizes logging functionalities, supporting both terminal outputs
    and Sentry integration for error tracking in debug environments.

    Features:
        - Logs informational messages directly to the terminal.
        - Sends error messages to Sentry when in debug mode.
        - Supports user-specific logging by including user IDs in log messages.

    Attributes:
        debug (bool): Flag indicating if the logger is running in debug mode.
        logger (logging.Logger): The logger instance for managing logs.
    """

    def __init__(self, debug: bool = False):
        self.settings = get_settings()
        self.debug = debug

        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG if self.debug else logging.INFO)

        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG if self.debug else logging.INFO)

            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

        if not self.debug:
            sentry_logging = LoggingIntegration(
                level=logging.INFO, event_level=logging.ERROR
            )

            sentry_sdk.init(
                dsn=self.settings.sentry.dns,
                integrations=[sentry_logging],
                send_default_pii=True,
                traces_sample_rate=1.0,
            )

    def log_info(self, message: str, conversation_id: str = None) -> None:
        """
        Logs an informational message to the terminal.

        Args:
            message (str): The message to log.
            conversation_id (str, optional): The conversation UUID.
        """
        log_message = (
            f"Conversation UUID: {conversation_id} - {message}"
            if conversation_id
            else message
        )
        self.logger.info(log_message)

    def log_debug(self, message: str, conversation_id: str = None) -> None:
        """
        Logs a debug message only when in debug mode.

        Args:
            message (str): The message to log.
            conversation_id (str, optional): The conversation UUID.
        """
        if self.debug:
            debug_message = (
                f"Conversation UUID: {conversation_id} - {message}"
                if conversation_id
                else message
            )
            self.logger.debug(debug_message)

    def log_error(self, message: str, conversation_id: str = None) -> None:
        """
        Logs an error message and sends it to Sentry if in debug mode.

        Args:
            message (str): The error message to log.
            conversation_id (str, optional): The conversation UUID.
        """
        error_message = (
            f"Conversation UUID: {conversation_id} - {message}"
            if conversation_id
            else message
        )
        self.logger.error(error_message)

        if not self.debug:
            sentry_sdk.capture_message(error_message, level="error")


ENV = get_settings().env.environment
DEBUG_FLAG = ENV == Environment.DEV

LOGGER = LoggerManager(debug=DEBUG_FLAG)
