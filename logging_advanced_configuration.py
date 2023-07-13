import logging

# Create loggers
logger1 = logging.getLogger("module1")
logger2 = logging.getLogger("module2")

# Create handlers
handler1 = logging.StreamHandler()
handler2 = logging.FileHandler("module2.log")

# Set log levels to each logger
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.INFO)

# Set log levels and formats to each handler
handler1.setLevel(logging.DEBUG)
handler2.setLevel(logging.INFO)

formatter1 = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
formatter2 = logging.Formatter("%(levelname)s: %(message)s @ %(asctime)s")
handler1.setFormatter(formatter1)
handler2.setFormatter(formatter2)

# Add handlers to loggers
logger1.addHandler(handler1)
logger2.addHandler(handler2)

logger1.debug("This is Debug message from logger1")
logger1.info("This is Info message from logger1")

logger2.debug(
    "This is Debug message from logger2"
)  # -> This would not be propagated due to log level
logger2.info("This is Info message from logger2")
