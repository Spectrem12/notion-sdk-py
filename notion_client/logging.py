"""Custom logging for notion-sdk-py."""

import logging
from functools import wraps, partial
from logging import Logger
import sys


def make_console_logger() -> Logger:
    """Return a custom logger."""
    logger = logging.getLogger(__package__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
#
# def attach_wrapper(obj,
#                    func=None):  # Helper function that attaches function as attribute of an object
#     if func is None:
#         return partial(attach_wrapper, obj)
#     setattr(obj, func.__name__, func)
#     return func
#
# def log(level, message):  # Actual decorator
#     def decorate(func):
#         logger = logging.getLogger(func.__module__)  # Setup logger
#         formatter = logging.Formatter(
#             '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         handler = logging.StreamHandler()
#         handler.setFormatter(formatter)
#         logger.addHandler(handler)
#         log_message = f"{func.__name__} - {message}"
#
#         @wraps(func)
#         def wrapper(*args,
#                     **kwargs):  # Logs the message and before executing the decorated function
#             logger.log(level, log_message)
#             return func(*args, **kwargs)
#
#         @attach_wrapper(wrapper)  # Attaches "set_level" to "wrapper" as attribute
#         def set_level(new_level):  # Function that allows us to set log level
#             nonlocal level
#             level = new_level
#
#         @attach_wrapper(wrapper)  # Attaches "set_message" to "wrapper" as attribute
#         def set_message(new_message):  # Function that allows us to set message
#             nonlocal log_message
#             log_message = f"{func.__name__} - {new_message}"
#
#         return wrapper
#
#     return decorate
