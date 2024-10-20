from enum import Enum


class LogLevel(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
    EXCEPTION = 60

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"[{self.value}, '{self.name}']"

    def __eq__(self, other):
        if isinstance(other, LogLevel):
            return self.value == other.value
        return self.value == other

    def __ne__(self, other):
        if isinstance(other, LogLevel):
            return self.value != other.value
        return self.value != other

    def __lt__(self, other):
        if isinstance(other, LogLevel):
            return self.value < other.value
        return self.value < other

    def __le__(self, other):
        if isinstance(other, LogLevel):
            return self.value <= other.value
        return self.value <= other

    def __gt__(self, other):
        if isinstance(other, LogLevel):
            return self.value > other.value
        return self.value > other

    def __ge__(self, other):
        if isinstance(other, LogLevel):
            return self.value >= other.value
        return self.value >= other
