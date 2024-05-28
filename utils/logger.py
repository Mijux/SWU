#!/usr/bin/env python3

from enum import Enum
from logging import Logger, FileHandler, StreamHandler, Formatter, getLogger
from logging.handlers import SysLogHandler
from os import getenv
from sys import stdout

from utils.exceptions import ConfigurationException


class LogLevel(Enum):
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0


def setup_logger():
    LOG_LEVEL = getenv("LOG_LEVEL", "WARNING")
    LOG_USE_SYSLOG = getenv("LOG_USE_SYSLOG", "True")
    LOG_FILE_PATH = getenv("LOG_FILE_PATH")

    if LOG_USE_SYSLOG.lower() in ["true", "1"]:
        LOG_USE_SYSLOG = True
    elif LOG_FILE_PATH is None:
        raise ConfigurationException(
            "LOG_USE_SYSLOG is False, LOG_FILE_PATH can't be None"
        )

    log_lvl = LogLevel._member_map_.get(LOG_LEVEL)
    if log_lvl is None:
        log_lvl = LogLevel.WARNING

    format = Formatter("%(asctime)s [%(levelname)s] - %(message)s")

    lggr = getLogger("SWU")
    lggr.setLevel(log_lvl.value)

    if LOG_USE_SYSLOG:
        handler = SysLogHandler(address="/dev/log")
    else:
        handler = FileHandler(filename=LOG_FILE_PATH)
    handler_stdout = StreamHandler(stdout)

    handler.setFormatter(format)
    handler_stdout.setFormatter(format)

    lggr.addHandler(handler)
    lggr.addHandler(handler_stdout)


def get_logger() -> Logger:
    return getLogger("SWU")
