import logging.config


configuration_dictionary = {
    "version": 1,
    "formatters": {
        "formatter1": {"format": "%(asctime)s - %(levelname)s - %(message)s"},
        "formatter2": {"format": "%(levelname)s: %(message)s @ %(asctime)s"},
    },
    "handlers": {
        "handler1": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "formatter1",
            "stream": "ext://sys.stdout",
        },
        "handler2": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "formatter2",
            "filename": "logger2_with_dict_config.log",
        },
    },
    "loggers": {
        "logger1": {"level": "DEBUG", "handlers": ["handler1"]},
        "logger2": {"level": "INFO", "handlers": ["handler2"]},
    },
}
logging.config.dictConfig(configuration_dictionary)


logger1 = logging.getLogger("logger1")
logger2 = logging.getLogger("logger2")

logger1.debug("This is Debug message from logger1")
logger1.info("This is Info message from logger1")

logger2.debug("This is Debug message from logger2")
logger2.info("This is Info message from logger2")
