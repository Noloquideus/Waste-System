class Settings:
    """It is used to determine the settings of the application logic. Constants are stored to avoid hardcode"""
    MAX_LENGTH_NAME = 50
    MIN_LENGTH_NAME = 3
    NAME_PATTERN = r'^[\w\-]+$'


SETTINGS = Settings()
