import traceback
import inspect
import sys
from datetime import datetime
from typing import Optional, Callable
from uuid import uuid4
import gevent
from gevent import monkey
from src.core.data_structures.collector import Collector
from src.core.decorators.validate_types import validate_types
from src.core.enums.log_levels import LogLevel
from src.core.exceptions.base import SystemException

monkey.patch_all()


class AsyncLogger:
    _instance = None
    __format = '[{time}] - [{level}] - [ID: {trace_id}] - [{file}:{line}] - [{message}]'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AsyncLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, log_format=__format, min_level=LogLevel.INFO, id_generator: Optional[Callable[[], str]] = uuid4):
        self.log_format = log_format
        self.min_level = min_level
        self.id_generator = id_generator
        self.trace_id = None
        self.collector = Collector()

    def set_format(self, log_format: str):
        self.log_format = log_format

    @validate_types
    def set_min_level(self, level: LogLevel):
        self.min_level = level

    def start_trace(self):
        self.trace_id = str(self.id_generator())

    def end_trace(self):
        self.trace_id = None
        self.unload_logs()

    def _log(self, level: LogLevel, message: str):
        if level >= self.min_level:
            frame = inspect.currentframe().f_back.f_back
            filename = frame.f_code.co_filename
            line_number = frame.f_lineno

            log_context = {
                'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'level': level.name,
                'file': filename,
                'line': line_number,
                'trace_id': self.trace_id or 'N/A',
                'message': message,
            }
            try:
                log_message = self.log_format.format(**log_context)
            except KeyError as e:
                raise SystemException(f'Invalid field in log format: {e}')

            self._write(log_message)

    def _write(self, message: str):
        self.collector.collect(message)
        if self.collector.interesting_volume() == self.collector.capacity:
            logs = self.collector.unload()
            self._async_write(logs)

    def _async_write(self, message: str):
        gevent.spawn(sys.stdout.write, message).join()

    def unload_logs(self):
        logs = self.collector.unload()
        self._async_write(logs)

    def debug(self, message: str):
        self._log(LogLevel.DEBUG, message)

    def info(self, message: str):
        self._log(LogLevel.INFO, message)

    def warning(self, message: str):
        self._log(LogLevel.WARNING, message)

    def error(self, message: str):
        self._log(LogLevel.ERROR, message)

    def critical(self, message: str):
        self._log(LogLevel.CRITICAL, message)

    def exception(self, message: str):
        exc_info = traceback.format_exc()
        full_message = f'{message}\nTraceback:\n{exc_info}'
        self._log(LogLevel.EXCEPTION, full_message)


logger = AsyncLogger(min_level=LogLevel.DEBUG)
