class SystemException(Exception):
    """Base exception for not-business logic"""
    def __init__(self, message: str):
        self.message = message
