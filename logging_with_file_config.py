import logging.config
import yaml

with open("./logging_config.yaml", "r") as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

logger1 = logging.getLogger("logger1")
logger2 = logging.getLogger("logger2")

logger1.debug("This is Debug message from logger1")
logger1.info("This is Info message from logger1")

logger2.debug("This is Debug message from logger2")
logger2.info("This is Info message from logger2")
