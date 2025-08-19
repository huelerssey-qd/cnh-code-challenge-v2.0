from settings.setting import get_settings, Environment


class AppConfig:
    """
    Application configuration handler, including dynamic root path resolution
    based on the current environment.
    """

    def __init__(self):
        self.environment = get_settings().env.environment

    def get_root_path(self) -> str:
        if self.environment == Environment.HOMOLOG:
            return "/ai_agents/homolog"
        elif self.environment == Environment.PROD:
            return "/ai_agents/prod"
        return ""
